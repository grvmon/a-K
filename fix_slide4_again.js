const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

const oldBrandBlock = `<div class="frame-overlay">
            <div class="brand-logo-josefin">acre&key</div>
            <div class="brand-sub">Home-buying concierge.</div>
        </div>`;

const newBrandBlock = `<div class="frame-overlay center-overlay">
            <div class="brand-logo-josefin" style="margin-bottom: 0.5rem;">acre&key</div>
            <div class="brand-sub">Home-buying concierge.</div>
        </div>`;

html = html.replace(oldBrandBlock, newBrandBlock);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slide 4 restored to center alignment.');
