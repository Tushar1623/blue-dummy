const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { MongoClient } = require('mongodb');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 8080;
const DB_NAME = process.env.DB_NAME || 'godrej_blue';
const MONGODB_URI = process.env.MONGODB_URI || '';
const ADMIN_USER = process.env.ADMIN_USER || '';
const ADMIN_PASS = process.env.ADMIN_PASS || '';

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Local backup file for offline / development resilience
const LEADS_BACKUP_FILE = path.join(__dirname, 'leads.json');

// Helper to get local leads
function getLocalLeads() {
  try {
    if (fs.existsSync(LEADS_BACKUP_FILE)) {
      const data = fs.readFileSync(LEADS_BACKUP_FILE, 'utf-8');
      return JSON.parse(data || '[]');
    }
  } catch (err) {
    console.error('Error reading local leads:', err.message);
  }
  return [];
}

// Helper to save backup lead locally
function saveLocalBackup(lead) {
  try {
    const leads = getLocalLeads();
    leads.unshift(lead);
    fs.writeFileSync(LEADS_BACKUP_FILE, JSON.stringify(leads, null, 2), 'utf-8');
  } catch (err) {
    console.error('Error saving local lead backup:', err.message);
  }
}

// Helper to update a local lead
function updateLocalLead(id, updates) {
  try {
    const leads = getLocalLeads();
    const idx = leads.findIndex(l => l._id === id);
    if (idx !== -1) {
      leads[idx] = { ...leads[idx], ...updates, updatedAt: new Date() };
      fs.writeFileSync(LEADS_BACKUP_FILE, JSON.stringify(leads, null, 2), 'utf-8');
      return leads[idx];
    }
  } catch (err) {
    console.error('Error updating local lead:', err.message);
  }
  return null;
}

// Helper to delete a local lead
function deleteLocalLead(id) {
  try {
    let leads = getLocalLeads();
    const initialLen = leads.length;
    leads = leads.filter(l => l._id !== id);
    if (leads.length !== initialLen) {
      fs.writeFileSync(LEADS_BACKUP_FILE, JSON.stringify(leads, null, 2), 'utf-8');
      return true;
    }
  } catch (err) {
    console.error('Error deleting local lead:', err.message);
  }
  return false;
}

// MongoDB Client & State
let dbClient = null;
let db = null;
let isConnected = false;

async function syncLocalLeadsToMongo() {
  try {
    if (!isConnected || !db || !fs.existsSync(LEADS_BACKUP_FILE)) return;
    const data = fs.readFileSync(LEADS_BACKUP_FILE, 'utf-8');
    const localLeads = JSON.parse(data || '[]');
    if (localLeads.length === 0) return;

    const collection = db.collection('leads');
    for (const lead of localLeads) {
      await collection.updateOne(
        { _id: lead._id },
        { $set: lead },
        { upsert: true }
      );
    }
    console.log(`🔄 [MongoDB] Synced ${localLeads.length} local leads to MongoDB Atlas.`);
  } catch (syncErr) {
    console.warn('⚠️ [MongoDB] Local leads sync error:', syncErr.message);
  }
}

async function connectToMongo() {
  // Reload .env if updated
  require('dotenv').config();
  const currentUri = process.env.MONGODB_URI || MONGODB_URI;

  if (!currentUri || currentUri.includes('<db_password>')) {
    console.log('\n========================================================================');
    console.log('⚠️  [MongoDB] No usable connection string is configured.');
    console.log('👉 Set MONGODB_URI in the .env file to enable live Atlas storage.');
    console.log('   In the meantime, leads will be safely saved locally to leads.json.');
    console.log('========================================================================\n');
    return;
  }

  try {
    console.log('⏳ [MongoDB] Connecting to MongoDB Atlas...');
    dbClient = new MongoClient(currentUri, {
      serverSelectionTimeoutMS: 8000,
    });
    await dbClient.connect();
    db = dbClient.db(DB_NAME);
    isConnected = true;
    console.log(`✅ [MongoDB] Successfully connected to database: "${DB_NAME}"`);

    // Ensure index on createdAt and email
    const collection = db.collection('leads');
    await collection.createIndex({ createdAt: -1 });
    await collection.createIndex({ email: 1 });

    // Sync any existing offline leads
    await syncLocalLeadsToMongo();
  } catch (err) {
    isConnected = false;
    console.error('❌ [MongoDB] Connection error:', err.message);
    console.log('ℹ️  Will retry connecting in 30 seconds. Local backup is active.');
    setTimeout(connectToMongo, 30000);
  }
}

connectToMongo();

// ==========================================
// API Endpoints
// ==========================================

// 1. Submit Inquiry / Brochure Request
app.post('/api/enquiry', async (req, res) => {
  try {
    const body = req.body || {};
    const fd = body.formData || {};
    
    // Normalize fields from form or nested formData
    const name = (body.name || (fd.firstName ? `${fd.firstName} ${fd.lastName || ''}`.trim() : '') || body.txt_firstname || '').trim();
    const email = (body.email || fd.email || body.txt_email || '').trim();
    const rawMobile = (body.mobile || fd.phone || body.txt_mobile || '').toString().trim();
    const countryCode = (body.countryCode || fd.countryCode || body.txt_countrycode || '+91').toString().trim();
    const country = (body.country || fd.country || body.txt_country || 'India').trim();
    const downloadFileType = (body.download_file_type || body.actionType || body.download || fd.download_file_type || '').toString().trim().toLowerCase();
    const isBrochure = downloadFileType === 'brochure' || body.brochure === 'brochure' || body.isBrochure === true;
    const actionType = isBrochure ? 'brochure' : 'enquiry';

    // Validation
    if (!name) {
      return res.status(400).json({ success: false, message: 'Name is required' });
    }
    if (!email || !email.includes('@')) {
      return res.status(400).json({ success: false, message: 'Valid email is required' });
    }
    if (!rawMobile || rawMobile.length < 6) {
      return res.status(400).json({ success: false, message: 'Valid mobile number is required' });
    }

    const leadId = 'LEAD_' + Date.now() + '_' + Math.floor(1000 + Math.random() * 9000);

    const leadDoc = {
      _id: leadId,
      name,
      email,
      phone: `${countryCode} ${rawMobile}`,
      countryCode,
      rawMobile,
      country,
      actionType,
      downloadBrochure: isBrochure,
      whatsappConsent: body.whatsapp_check === 'on' || body.whatsapp_check === true || fd.optIn === 'Yes' || body.optIn === 'Yes',
      campaignId: body.Campaign_ID || fd.property?.addCode || '95458',
      projId: body.projid || fd.property?.projCode || 'a1lId000000TNMwIAO',
      gclid: body.gclid || fd.googleGCLID || '',
      utmTerm: body.utm_term || '',
      utmContent: body.utm_content || '',
      referrer: body.referrer_client || '',
      webUrl: body.WEB_URL || fd.property?.url || fd.landingPageURL || req.headers.referer || '',
      ip: fd.userIPAddress || req.headers['x-forwarded-for'] || req.socket.remoteAddress,
      userAgent: req.headers['user-agent'] || '',
      status: 'New',
      notes: '',
      createdAt: new Date(),
      updatedAt: new Date()
    };

    // Always save local backup
    saveLocalBackup(leadDoc);

    // Save to MongoDB if connected
    let savedToMongo = false;
    if (isConnected && db) {
      try {
        await db.collection('leads').insertOne(leadDoc);
        savedToMongo = true;
        console.log(`📥 [Lead Captured] ${leadDoc.actionType.toUpperCase()}: ${leadDoc.name} (${leadDoc.phone}) -> Saved to MongoDB Atlas`);
      } catch (dbErr) {
        console.error('⚠️ [MongoDB] Insert error:', dbErr.message);
      }
    } else {
      console.log(`📥 [Lead Captured] ${leadDoc.actionType.toUpperCase()}: ${leadDoc.name} (${leadDoc.phone}) -> Saved to local backup (MongoDB waiting for password/connection)`);
    }

    // Response matching SFDC / custom lead format expected by frontend
    return res.status(200).json({
      success: true,
      Id: leadId,
      leadId: leadId,
      actionType,
      downloadBrochure: isBrochure,
      savedToDatabase: savedToMongo,
      message: isBrochure ? 'Brochure request received' : 'Enquiry submitted successfully'
    });

  } catch (error) {
    console.error('Server error processing lead:', error);
    return res.status(500).json({
      success: false,
      message: 'Internal server error processing enquiry'
    });
  }
});

// 2. Status & DB Health Check
app.get('/api/status', (req, res) => {
  res.json({
    status: 'online',
    database: isConnected ? 'connected' : 'waiting_for_credentials_or_offline',
    mongoUriConfigured: Boolean(MONGODB_URI && !MONGODB_URI.includes('<db_password>')),
    dbName: DB_NAME,
    timestamp: new Date()
  });
});

// 3. View Leads (API / Dashboard Endpoint)
app.get('/api/leads', async (req, res) => {
  try {
    let leads = [];
    if (isConnected && db) {
      leads = await db.collection('leads').find().sort({ createdAt: -1 }).limit(100).toArray();
    } else if (fs.existsSync(LEADS_BACKUP_FILE)) {
      leads = JSON.parse(fs.readFileSync(LEADS_BACKUP_FILE, 'utf-8') || '[]');
    }

    res.json({
      success: true,
      count: leads.length,
      source: isConnected ? 'mongodb_atlas' : 'local_backup',
      leads
    });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

// ==========================================
// Admin Panel Endpoints
// ==========================================

// Route to Admin Panel HTML
app.get('/admin', (req, res) => {
  res.sendFile(path.join(__dirname, 'admin.html'));
});

// Admin Login
app.post('/api/admin/login', (req, res) => {
  const { username, password } = req.body || {};
  const adminUser = process.env.ADMIN_USER || ADMIN_USER;
  const adminPass = process.env.ADMIN_PASS || ADMIN_PASS;
  if (adminUser && adminPass && username === adminUser && password === adminPass) {
    const token = 'tok_' + Buffer.from(`${username}:${Date.now()}`).toString('base64');
    return res.json({
      success: true,
      token,
      user: { username, role: 'Administrator' },
      message: 'Authentication successful'
    });
  }
  return res.status(401).json({
    success: false,
    message: 'Invalid username or password'
  });
});

// Admin Metrics & Stats
app.get('/api/admin/stats', async (req, res) => {
  try {
    let leads = [];
    if (isConnected && db) {
      leads = await db.collection('leads').find().toArray();
    } else {
      leads = getLocalLeads();
    }

    const todayStart = new Date();
    todayStart.setHours(0, 0, 0, 0);

    const total = leads.length;
    const brochures = leads.filter(l => l.downloadBrochure || l.actionType === 'brochure').length;
    const enquiries = leads.filter(l => !l.downloadBrochure && l.actionType !== 'brochure').length;
    const today = leads.filter(l => new Date(l.createdAt) >= todayStart).length;
    const siteVisits = leads.filter(l => l.status === 'Site Visit Scheduled').length;
    const booked = leads.filter(l => l.status === 'Booked' || l.status === 'Converted').length;

    res.json({
      success: true,
      total,
      brochures,
      enquiries,
      today,
      siteVisits,
      booked,
      dbStatus: isConnected ? 'Connected (MongoDB Atlas)' : 'Local Storage Active (Awaiting MongoDB Password)',
      dbConnected: isConnected
    });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

// Admin Leads List (with search, filter, status)
app.get('/api/admin/leads', async (req, res) => {
  try {
    let leads = [];
    if (isConnected && db) {
      leads = await db.collection('leads').find().sort({ createdAt: -1 }).toArray();
    } else {
      leads = getLocalLeads();
    }

    const { search, filter, status } = req.query;

    if (search) {
      const q = search.toLowerCase().trim();
      leads = leads.filter(l => 
        (l.name && l.name.toLowerCase().includes(q)) ||
        (l.email && l.email.toLowerCase().includes(q)) ||
        (l.phone && l.phone.toLowerCase().includes(q)) ||
        (l._id && l._id.toLowerCase().includes(q)) ||
        (l.notes && l.notes.toLowerCase().includes(q))
      );
    }

    if (filter === 'brochure') {
      leads = leads.filter(l => l.downloadBrochure || l.actionType === 'brochure');
    } else if (filter === 'enquiry') {
      leads = leads.filter(l => !l.downloadBrochure && l.actionType !== 'brochure');
    } else if (filter === 'today') {
      const todayStart = new Date();
      todayStart.setHours(0, 0, 0, 0);
      leads = leads.filter(l => new Date(l.createdAt) >= todayStart);
    } else if (filter === 'same_ip') {
      const ipCounts = {};
      leads.forEach(l => {
        const ip = (l.ip || '').trim();
        if (ip) ipCounts[ip] = (ipCounts[ip] || 0) + 1;
      });
      leads = leads.filter(l => {
        const ip = (l.ip || '').trim();
        return ip && ipCounts[ip] > 1;
      });
    }

    if (status && status !== 'all') {
      leads = leads.filter(l => (l.status || 'New').toLowerCase() === status.toLowerCase());
    }

    res.json({
      success: true,
      count: leads.length,
      source: isConnected ? 'mongodb_atlas' : 'local_backup',
      leads
    });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

// Admin Update Lead (Status & Notes)
app.patch('/api/admin/leads/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { status, notes } = req.body;
    const updates = { updatedAt: new Date() };
    if (status !== undefined) updates.status = status;
    if (notes !== undefined) updates.notes = notes;

    // Update locally
    const updatedLead = updateLocalLead(id, updates);

    // Update in MongoDB if connected
    if (isConnected && db) {
      await db.collection('leads').updateOne(
        { _id: id },
        { $set: updates }
      );
    }

    res.json({
      success: true,
      message: 'Lead updated successfully',
      lead: updatedLead
    });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

// Admin Delete Lead
app.delete('/api/admin/leads/:id', async (req, res) => {
  try {
    const { id } = req.params;

    deleteLocalLead(id);

    if (isConnected && db) {
      await db.collection('leads').deleteOne({ _id: id });
    }

    res.json({
      success: true,
      message: 'Lead deleted successfully'
    });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

// Admin Export Leads as CSV
app.get('/api/admin/export', async (req, res) => {
  try {
    let leads = [];
    if (isConnected && db) {
      leads = await db.collection('leads').find().sort({ createdAt: -1 }).toArray();
    } else {
      leads = getLocalLeads();
    }

    const headers = [
      'Lead ID',
      'Date & Time',
      'Action Type',
      'Brochure Downloaded',
      'Name',
      'Email',
      'Phone',
      'Country',
      'WhatsApp Consent',
      'Status',
      'Notes',
      'Campaign ID',
      'Project Code',
      'IP Address',
      'Referrer'
    ];

    const escapeCsv = (str) => {
      if (str === null || str === undefined) return '""';
      return `"${String(str).replace(/"/g, '""')}"`;
    };

    const rows = leads.map(l => [
      escapeCsv(l._id),
      escapeCsv(new Date(l.createdAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })),
      escapeCsv(l.actionType || 'enquiry'),
      escapeCsv(l.downloadBrochure ? 'Yes' : 'No'),
      escapeCsv(l.name),
      escapeCsv(l.email),
      escapeCsv(l.phone),
      escapeCsv(l.country),
      escapeCsv(l.whatsappConsent ? 'Yes' : 'No'),
      escapeCsv(l.status || 'New'),
      escapeCsv(l.notes || ''),
      escapeCsv(l.campaignId || ''),
      escapeCsv(l.projId || ''),
      escapeCsv(l.ip || ''),
      escapeCsv(l.referrer || '')
    ]);

    const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\r\n');
    const filename = `godrej_blue_leads_${new Date().toISOString().slice(0, 10)}.csv`;

    res.setHeader('Content-Type', 'text/csv; charset=utf-8');
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    res.send(csvContent);
  } catch (err) {
    res.status(500).send('Error generating export: ' + err.message);
  }
});

// Serve Static Frontend Files
app.use(express.static(__dirname));

// Fallback to index.html for root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start Server
app.listen(PORT, () => {
  console.log(`\n🚀 Godrej Blue Web Server is running live on: http://localhost:${PORT}`);
  console.log(`🔐 Admin Panel: http://localhost:${PORT}/admin`);
  console.log(`📊 Leads API Endpoint: http://localhost:${PORT}/api/enquiry`);
  console.log(`📋 View Leads Dashboard: http://localhost:${PORT}/api/leads`);
  console.log(`🔍 Status Check: http://localhost:${PORT}/api/status\n`);
});
