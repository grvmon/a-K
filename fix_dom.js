const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

const headPart = html.substring(0, html.indexOf('<body>') + 6);

let newBody = '\n';
const frames = [
    { label: '01 — The Decision', title: 'Buying a home?' },
    { label: '02 — Clarity', title: 'We help you buy right.' },
    { label: '03 — The Process', title: 'Find. Check. Inspect. Negotiate.' },
    { label: '04 — Control', title: 'You Decide.' },
    { label: '05 — The Brand', isBrand: true },
    { label: '06 — The Positioning', isBrand: true }
];

frames.forEach((f, i) => {
    let overlayContent = '';
    
    if (i < 3) {
        overlayContent = `<div class="frame-overlay">
            <h1 class="frame-text">${f.title}</h1>
        </div>`;
    } else {
        // Slides 4, 5, 6 share the same centered content
        overlayContent = `<div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="font-size: 5.5cqw; margin-bottom: 2.5rem;">You Decide.</h1>
            <div class="brand-logo-josefin">acre&key</div>
            <div class="brand-sub">Independent home-buying concierge.</div>
        </div>`;
    }

    const dots = Array.from({length: 6}, (_, idx) => 
        `<div class="carousel-dot ${idx === i ? 'active' : ''}"></div>`
    ).join('');

    const arrow = i < 5 ? `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>
    ` : '';

    newBody += `
    <!-- 0${i + 1} -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/frame${i + 1}_3x4.jpg" alt="0${i + 1}">
        ${overlayContent}
        <div class="carousel-dots">
            ${dots}
        </div>
        ${arrow}
    </div>\n`;
});

newBody += '\n</body>\n</html>';

fs.writeFileSync(file, headPart + newBody, 'utf8');
console.log('✅ DOM completely rebuilt to fix layout corruption.');
