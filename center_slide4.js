const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// Find slide 4 block
const marker = '<!-- 04 -->';
const blockStart = html.indexOf(marker);
let block = html.substring(blockStart);

// Replace the first <div class="frame-overlay"> in this block with <div class="frame-overlay center-overlay">
block = block.replace('<div class="frame-overlay">', '<div class="frame-overlay center-overlay">');

html = html.substring(0, blockStart) + block;

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slide 4 centered again.');
