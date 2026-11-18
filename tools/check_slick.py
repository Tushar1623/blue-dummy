import re
import urllib.request
import os

with open('landing_page/assets/vendors/slick/slick.css', 'r', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'url\(([^)]+)\)', text)
print("slick urls:", urls)
