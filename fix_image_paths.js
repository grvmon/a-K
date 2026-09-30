const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

html = html.replace(/\/Users\/gauravmongia\/\.gemini\/antigravity\/brain\/[^\/]+\//g, 'assets/images/moodboard/');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Image paths made relative.');
