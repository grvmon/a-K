const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

const headPart = html.substring(0, html.indexOf('<body>') + 6);

let newBody = '\n';
const frames = [
    { image: 'frame1_3x4.jpg', title: 'Buying a home?' },
    { image: 'frame2_3x4.jpg', title: 'We help you buy right.' },
    { image: 'frame3_3x4.jpg', title: 'Find. Check. Inspect. Negotiate.' },
    { image: 'frame5_3x4.jpg', isBrand: true } // Originally frame 5
];

frames.forEach((f, i) => {
    let overlayContent = '';
    
    if (!f.isBrand) {
        overlayContent = `<div class="frame-overlay">
            <h1 class="frame-text">${f.title}</h1>
        </div>`;
    } else {
        overlayContent = `<div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="font-size: 5.5cqw; margin-bottom: 2.5rem;">You Decide.</h1>
            <div class="brand-logo-josefin">acre&key</div>
            <div class="brand-sub">Home-buying concierge.</div>
        </div>`;
    }

    const totalDots = 4;
    const dots = Array.from({length: totalDots}, (_, idx) => 
        `<div class="carousel-dot ${idx === i ? 'active' : ''}"></div>`
    ).join('');

    const arrow = i < (totalDots - 1) ? `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>
    ` : '<div></div>';

    newBody += `
    <!-- 0${i + 1} -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/${f.image}" alt="0${i + 1}">
        ${overlayContent}
        <div class="carousel-nav-container">
            <div class="carousel-dots">
                ${dots}
            </div>
            ${arrow}
        </div>
    </div>\n`;
});

newBody += '\n</body>\n</html>';

fs.writeFileSync(file, headPart + newBody, 'utf8');
console.log('✅ Sequence updated to 4 frames.');
