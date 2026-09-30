const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// Replace "Independent home-buying concierge." with "Home-buying concierge."
html = html.replace(/Independent home-buying concierge\./g, 'Home-buying concierge.');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ "Independent" removed.');
