const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// For slide 3, we want the block centered, but the text left-aligned inside the block.
// Currently it is:
// <h1 class="frame-text" style="white-space: normal; text-align: center; line-height: 1.25;">

const oldText = '<h1 class="frame-text" style="white-space: normal; text-align: center; line-height: 1.25;">';
const newText = '<h1 class="frame-text" style="white-space: normal; text-align: left; line-height: 1.25; display: inline-block; margin: 0 auto;">';

html = html.replace(oldText, newText);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slide 3 block centered but text left-aligned.');
