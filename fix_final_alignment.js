const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Make Slide 4 text exactly aligned to the bottom-left like Slides 1, 2, 3
html = html.replace(/<div class="frame-overlay center-overlay">/g, '<div class="frame-overlay">');

// Since we removed center-overlay, the text in Slide 4 might still be center aligned if it has text-align center, but we want it left aligned.
// Let's remove any inline text-align center if it exists. (I didn't add it inline to the brand block divs, so they will inherit text-align: left).
// Wait, the brand-sub and brand-logo-josefin should be left aligned now.

// 2. Remove the carousel dots from the HTML
html = html.replace(/<div class="carousel-dots">[\s\S]*?<\/div>/g, '<div></div>'); 
// Replaced with <div></div> so justify-content: space-between still pushes the arrow to the right!

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Text aligned consistently on all slides. Dots removed.');
