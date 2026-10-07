import re
import os

EVERGREEN_PATH = "/Users/patidar/Desktop/Ank New Website V1/property/prestige-evergreen-raintree-park/index.html"
GRANADA_PATH = "/Users/patidar/Desktop/Ank New Website V1/property/brigade-granada/index.html"

with open(EVERGREEN_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace core property identifiers
html = html.replace("prestige-evergreen-raintree-park", "brigade-granada")
html = html.replace("Prestige Evergreen", "Brigade Granada")
html = html.replace("Evergreen at Prestige Raintree Park", "Brigade Granada")
html = html.replace("Prestige Raintree Park", "Brigade Granada")
html = html.replace("Prestige Group", "Brigade Group")

# Update titles and meta tags
html = re.sub(r'<title>.*?</title>', '<title>Brigade Granada on Whitefield-Kadugodi Road, Bangalore | 2.5, 3 & 4 BHK Apartments</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="2.5, 3 & 4 BHK in Brigade Granada, Whitefield-Kadugodi Road, Bangalore. Get floor plans, independent buyer advisory, exact pricing starting from ₹1.45 Cr.">', html)
html = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Brigade Granada | Price, Floor Plans, RERA & Review | Acre&Key">', html)
html = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Independent buyer intelligence for Brigade Granada on Whitefield-Kadugodi Road, Bengaluru. 2.5–4 BHK luxury residences across a 5.5-acre boutique high-rise precinct by Brigade Group.">', html)
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://acrenkey.com/property/brigade-granada/">', html)

# Replace location & pricing values
html = html.replace("Varthur Junction, Whitefield Precinct, Bengaluru", "Whitefield - Kadugodi Main Road, Whitefield Precinct, Bengaluru")
html = html.replace("SH 35, Varthur Main Road, Opposite Varthur Lake, Whitefield Precinct, Bengaluru, Karnataka 560087", "Whitefield - Kadugodi Main Road, Near Hope Farm Junction, Whitefield Precinct, Bengaluru, Karnataka 560067")
html = html.replace("₹1.07 Cr*", "₹1.45 Cr*")
html = html.replace("₹1.07 – 4.09 Cr", "₹1.45 – 3.25 Cr")
html = html.replace("₹15,500 – 16,300", "₹11,500 – 12,800")
html = html.replace("PRM/KA/RERA/1251/446/PR/010126/008374", "PRM/KA/RERA/1251/446/PR/181124/007231")
html = html.replace("30 June 2030", "31 December 2028")

# Metrics replacement
html = html.replace("24-Acre Precinct | 14 Towers (2B+G+19) | ~86,000 sq.ft. Clubhouse | 70% Open Area", "5.5-Acre Precinct | 4 High-Rise Towers (2B+G+19) | ~35,000 sq.ft. Clubhouse | 70% Open Area")
html = html.replace("24 Acres (Precinct)", "5.5 Acres")
html = html.replace("14 Towers", "4 Towers")
html = html.replace("~2,000 Residences", "~450 Residences")
html = html.replace("~86,000 sq.ft.", "~35,000 sq.ft.")
html = html.replace("Kadugodi / Hope Farm Metro (~8.0 km)", "Hope Farm / Kadugodi Metro (~1.2 km)")

# Update Breadcrumb text
html = html.replace('<span class="current">Prestige Evergreen</span>', '<span class="current">Brigade Granada</span>')

# Save output to brigade-granada/index.html
with open(GRANADA_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Brigade Granada HTML successfully generated from Prestige Evergreen template!")
