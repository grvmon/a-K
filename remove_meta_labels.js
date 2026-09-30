const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// Remove all meta-label divs
html = html.replace(/<div class="meta-label">.*?<\/div>\n/g, '');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Meta labels removed.');
