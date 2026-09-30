const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

const headPart = html.substring(0, html.indexOf('<body>') + 6);

let newBody = '\n';
const frames = [
    { image: 'frame1_3x4.jpg', title: 'Buying a home?' },
    { image: 'frame2_3x4.jpg', title: 'We help you buy right.' },
    { image: 'frame3_3x4.jpg', isSlide3: true },
    { image: 'frame5_3x4.jpg', isBrand: true }
];

frames.forEach((f, i) => {
    const arrow = i < 3 ? `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: rgba(255, 255, 255, 0.9); cursor: pointer; transition: transform 0.4s ease; margin-bottom: 0.5rem;">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>
    ` : '';

    let overlayContent = '';
    
    if (f.isBrand) {
        overlayContent = `<div class="frame-overlay center-overlay">
            <div class="brand-logo-josefin" style="margin-bottom: 0.5rem;">acre&key</div>
            <div class="brand-sub">Home-buying concierge.</div>
        </div>`;
    } else if (f.isSlide3) {
        overlayContent = `<div class="frame-overlay">
            <h1 class="frame-text" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); white-space: normal; text-align: left; line-height: 1.25; width: fit-content; margin: 0;">
                Find.<br>
                Check.<br>
                Inspect.<br>
                Negotiate.<br>
                Decide.
            </h1>
            <div style="display: flex; justify-content: flex-end; align-items: flex-end; width: 100%;">
                ${arrow}
            </div>
        </div>`;
    } else {
        overlayContent = `<div class="frame-overlay">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; width: 100%;">
                <h1 class="frame-text">${f.title}</h1>
                ${arrow}
            </div>
        </div>`;
    }

    newBody += `
    <!-- 0${i + 1} -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/${f.image}" alt="0${i + 1}">
        ${overlayContent}
    </div>\n`;
});

const scriptPart = `
    <script>
        document.querySelectorAll('.carousel-arrow-right').forEach((arrow, index) => {
            arrow.addEventListener('click', () => {
                const frames = document.querySelectorAll('.frame');
                if (frames[index + 1]) {
                    frames[index + 1].scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    </script>
</body>
</html>`;

fs.writeFileSync(file, headPart + newBody + scriptPart, 'utf8');
console.log('✅ Slide 3 arrow moved to bottom right.');
