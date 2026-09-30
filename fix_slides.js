const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Add Josefin Sans to Google Fonts
html = html.replace(
    /family=Marcellus&display=swap/,
    'family=Marcellus&family=Josefin+Sans:wght@400;500;600&display=swap'
);

// 2. Add Josefin Sans CSS class
const newCSS = `
        .brand-logo-josefin {
            font-family: 'Josefin Sans', sans-serif;
            font-size: 8cqw;
            color: var(--titanium-frost);
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }
`;
html = html.replace(/\.brand-logo \{/, newCSS + '\n        .brand-logo {');

// 3. Update Slide 5
const slide5Old = `<div class="brand-logo">acre&key</div>`;
const slide5New = `<div class="brand-logo-josefin">acre&key</div>`;
html = html.replace(slide5Old, slide5New);

// 4. Update Slide 6
const slide6Old = `<!-- 06 -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/frame6_3x4.jpg" alt="06">
        <div class="frame-overlay center-overlay">
            <div class="brand-sub" style="margin-bottom:1rem;">Independent home-buying concierge.</div>
            <div class="brand-logo">acrenkey.com</div>
        </div>
    </div>`;
const slide6New = `<!-- 06 -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/frame6_3x4.jpg" alt="06">
        <div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="white-space: normal; text-align: center; font-size: 5cqw;">Independent home-buying concierge.</h1>
        </div>
    </div>`;
html = html.replace(slide6Old, slide6New);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slides 4, 5, 6 updated.');
