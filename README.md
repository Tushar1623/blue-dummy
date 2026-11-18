# Godrej Blue Kolkata - Full Stack Landing Page & Admin Portal

A faithful, fully responsive replica of the [Godrej Blue Kolkata Landing Page](https://www.godrejproperties.com/landing-page/kolkata/residential/godrej-blue/) featuring an integrated Express.js server, MongoDB database connectivity, resilient local backup storage, and an **Executive Admin Panel** for lead management.

---

## 🚀 Key Features

1. **Exact Visual Replica & Curated Visual Gallery**: Complete layout matching the official Godrej Blue website with hero banner, quick ribbon, project overview, **"Designed with Precision – Explore BLUE’s Floor Plans"** (featuring the Master Layout Plan, 3 BHK, 4 BHK, and 4 BHK + Servant pricing cards with high-res architectural plans), **"Gallery: A Glimpse into the World of BLUE"** (featuring 13 high-res architectural & interior visuals from `assets/blue image` + video walkthrough with GLightbox fullscreen zoom), **Location Advantage & Strategic Landmarks** (Hospitals, Transit Connectivity, Schools & Institutions, Malls), amenities, connectivity, reviews, and interactive enquiry popups.
2. **Mandatory Lead Capture**:
   - **Brochure Download**: Prompts the user to fill the lead form first, saves the lead to the database, redirects to `thankyou.html`, and automatically downloads the official 38-page brochure PDF (`godrej_blue_brochure.pdf`).
   - **Enquiry / Site Visit**: Prompts the lead form, stores lead details, and confirms submission on `thankyou.html`.
3. **Database Integration**:
   - **MongoDB Atlas**: Configure your own cluster connection string in `.env`.
   - **Offline / Local Backup (`leads.json`)**: Leads are never lost; automatically saved locally and auto-synced to MongoDB Atlas once connected.
4. **Executive Admin Panel (`/admin`)**:
   - Login credentials are configured through environment variables.
   - Real-time KPIs: Total Leads, Brochure Downloads, Enquiries, Today's count, MongoDB status.
   - **Duplicate IP Detection & Red Marking**: Automatically detects repeated submissions from the same IP address, marking the Lead Number (`#`) and Lead ID in bright red with an alert badge (`Same IP`), a dedicated 1-click filter pill, and full details modal warnings.
   - Lead Search & Filtering (by Type, Date, Status, or query).
   - Direct 1-Click WhatsApp (`https://wa.me/`) & Call (`tel:`) buttons.
   - Live Pipeline Status updates (New, Contacted, In Follow-Up, Site Visit Scheduled, Booked, Not Interested).
   - Inline notes & remarks auto-saving.
   - Comprehensive Lead Details modal with marketing UTM attribution, IP, and timestamps.
   - 1-Click CSV / Excel export.
5. **Mobile Responsiveness**: Custom responsive styles (`mobile-custom.css`) with sticky action bar, touch-friendly inputs, and hidden desktop-only side tabs.
6. **14 Targeted SEO Keywords**: Fully integrated across meta tags, headings, content, and the 10-point FAQ accordion.

---

## 🔑 Accessing the Admin Panel

- **URL**: [http://localhost:8080/admin](http://localhost:8080/admin)
- Set `ADMIN_USER` and `ADMIN_PASS` in `.env` before logging in. The admin panel is unavailable until both are configured.

---

## 🛠️ How to Run

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment variables**:
   Copy `.env.example` to `.env`, then set your MongoDB connection string and unique admin credentials:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-host>/<database>
   DB_NAME=godrej_blue
   PORT=8080
   ADMIN_USER=admin
   ADMIN_PASS=replace-with-a-strong-unique-password
   ```

3. **Start the Web Server**:
   ```bash
   node server.js
   ```

4. **Available URLs**:
   - Landing Page: [http://localhost:8080/](http://localhost:8080/)
   - Admin Panel: [http://localhost:8080/admin](http://localhost:8080/admin)
   - Status & Health: [http://localhost:8080/api/status](http://localhost:8080/api/status)
   - Export CSV: [http://localhost:8080/api/admin/export](http://localhost:8080/api/admin/export)
   - Brochure PDF: [http://localhost:8080/godrej_blue_brochure.pdf](http://localhost:8080/godrej_blue_brochure.pdf)
