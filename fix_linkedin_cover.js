const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/linkedin-cover.html';
let html = fs.readFileSync(file, 'utf8');

html = html.replace(/padding-top: 30px;/, '');
html = html.replace(/padding-bottom: 16px;/, '');
html = html.replace(/padding-left: 100px;/, 'padding-left: 100px;');

fs.writeFileSync(file, html, 'utf8');
