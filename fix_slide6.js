const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /<!-- 06 -->[\s\S]*?<\/div>\s*<\/div>/;
const newSlide6 = `<!-- 06 -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/frame6_3x4.jpg" alt="06">
        <div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="white-space: normal; text-align: center; font-size: 5.5cqw;">Independent home-buying concierge.</h1>
        </div>
    </div>`;

html = html.replace(regex, newSlide6);
fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slide 6 forced.');
