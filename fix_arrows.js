const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// The HTML currently looks like this:
// <div class="carousel-nav-container">
//     <div></div>
//     </div>
//     <svg class="carousel-arrow-right" ...>...</svg>
// 
// Or for slide 4:
// <div class="carousel-nav-container">
//     <div></div>
//     </div>
//     <div></div>

// Let's just regex out everything from <div class="carousel-nav-container"> to the end of the frame, and rebuild the nav containers correctly.
html = html.replace(/<div class="carousel-nav-container">[\s\S]*?<\/div>\s*<\/div>/g, (match, offset, string) => {
    // This is dangerous, so let's just do a string split by frame
    return match;
});

// Safer approach: rebuild the body one last time, this is bulletproof.
const headPart = html.substring(0, html.indexOf('<body>') + 6);

let newBody = '\n';
const frames = [
    { image: 'frame1_3x4.jpg', title: 'Buying a home?' },
    { image: 'frame2_3x4.jpg', title: 'We help you buy right.' },
    { image: 'frame3_3x4.jpg', isSlide3: true },
    { image: 'frame5_3x4.jpg', isBrand: true }
];

frames.forEach((f, i) => {
    let overlayContent = '';
    
    if (f.isBrand) {
        overlayContent = `<div class="frame-overlay">
            <h1 class="frame-text" style="font-size: 5.5cqw; margin-bottom: 2.5rem;">acre&key<br><span class="brand-sub" style="font-size: 3cqw; display: block; margin-top: 0.5rem;">Home-buying concierge.</span></h1>
        </div>`;
    } else if (f.isSlide3) {
        overlayContent = `<div class="frame-overlay center-overlay">
            <h1 class="frame-text" style="white-space: normal; text-align: left; line-height: 1.25; display: inline-block; margin: 0 auto;">
                Find.<br>
                Check.<br>
                Inspect.<br>
                Negotiate.<br>
                Decide.
            </h1>
        </div>`;
    } else {
        overlayContent = `<div class="frame-overlay">
            <h1 class="frame-text">${f.title}</h1>
        </div>`;
    }

    // We only want the right arrow on slides 1, 2, 3
    const arrow = i < 3 ? `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>
    ` : '<div></div>';

    // Slide 4 brand block is just acre&key and Home-buying concierge.
    if (f.isBrand) {
        overlayContent = `<div class="frame-overlay">
            <div class="brand-logo-josefin">acre&key</div>
            <div class="brand-sub">Home-buying concierge.</div>
        </div>`;
    }

    newBody += `
    <!-- 0${i + 1} -->
    <div class="frame">
        <img class="frame-img" src="/Users/gauravmongia/.gemini/antigravity/brain/65b24d7e-1543-41a1-bb3a-a3103a0e449b/${f.image}" alt="0${i + 1}">
        ${overlayContent}
        <div class="carousel-nav-container">
            <div></div> <!-- empty div to push arrow to the right -->
            ${arrow}
        </div>
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
console.log('✅ Nav container fully fixed. Arrows are strictly on Slides 1, 2, 3.');
