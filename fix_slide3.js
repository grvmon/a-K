const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

const oldSlide3Text = '<div class="frame-overlay">\n            <h1 class="frame-text">Find. Check. Inspect. Negotiate.</h1>\n        </div>';
const newSlide3Text = `<div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="white-space: normal; text-align: center; line-height: 1.25;">
                Find.<br>
                Check.<br>
                Inspect.<br>
                Negotiate.<br>
                Decide.
            </h1>
        </div>`;

// If exact match fails due to whitespace, let's use regex
html = html.replace(/<div class="frame-overlay">\s*<h1 class="frame-text">Find\. Check\. Inspect\. Negotiate\.<\/h1>\s*<\/div>/g, newSlide3Text);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slide 3 stacked and centered.');
