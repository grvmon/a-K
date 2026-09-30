const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// Wipe all carousel-dot classes
html = html.replace(/<div class="carousel-dot.*?<\/div>/g, '');
html = html.replace(/<div class="carousel-dots">[\s\S]*?<\/div>/g, '');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Dots wiped for real.');
