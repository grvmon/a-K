const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

const newContent = `
        <div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="font-size: 5.5cqw; margin-bottom: 2.5rem;">You Decide.</h1>
            <div class="brand-logo-josefin">acre&key</div>
            <div class="brand-sub">Independent home-buying concierge.</div>
        </div>`;

// Replace Slide 4 overlay
html = html.replace(
    /<div class="frame-overlay">\s*<h1 class="frame-text">You Decide\.<\/h1>\s*<\/div>/,
    newContent
);

// Replace Slide 5 overlay
html = html.replace(
    /<div class="frame-overlay center-overlay">\s*<div class="brand-logo-josefin">acre&key<\/div>\s*<\/div>/,
    newContent
);

// Replace Slide 6 overlay
html = html.replace(
    /<div class="frame-overlay center-overlay">\s*<h1 class="frame-text"[^>]*>Independent home-buying concierge\.<\/h1>\s*<\/div>/,
    newContent
);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slides 4, 5, 6 synchronized.');
