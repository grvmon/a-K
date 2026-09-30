const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// Find the last frame (Slide 4) and remove "You Decide."
// Using a precise regex to target only the last occurrence or just a global replace if it's unique enough (it isn't, but wait, there is only one "You Decide" now since we removed the 3 identical slides and made it a 4-slide sequence!)
// Ah! In the 4-slide sequence, Slide 4 is the ONLY one with "You Decide."
html = html.replace(/<h1 class="frame-text" style="font-size: 5\.5cqw; margin-bottom: 2\.5rem;">You Decide\.<\/h1>\s*/g, '');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ "You Decide." removed from the last slide.');
