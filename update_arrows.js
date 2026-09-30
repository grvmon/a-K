const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Update CSS
const newCSS = `
        /* Carousel Navigation */
        .carousel-dots {
            position: absolute;
            bottom: 7.5%;
            left: 8.33%;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            z-index: 10;
        }
        .carousel-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.9);
            box-sizing: border-box;
        }
        .carousel-dot.active {
            background-color: rgba(255, 255, 255, 0.9);
        }
        .carousel-arrow-right {
            position: absolute;
            bottom: 7.5%;
            right: 8.33%;
            width: 48px;
            height: 48px;
            color: rgba(255, 255, 255, 0.9);
            z-index: 10;
            transition: transform 0.4s ease;
            cursor: pointer;
        }
        .carousel-arrow-right:hover {
            transform: translateX(5px);
        }
`;
html = html.replace(/\/\* Carousel Navigation \*\/[\s\S]*?\.carousel-arrow \{[\s\S]*?\}/, newCSS);

// 2. We need to update the injected HTML.
// Right now it's:
// <div class="carousel-nav">
//    <div class="carousel-dots">...</div>
//    <svg class="carousel-arrow"...>
// </div>
// Let's replace the whole block with the split layout.

for (let i = 0; i < 6; i++) {
    const dotsHtml = Array.from({length: 6}, (_, idx) => 
        `<div class="carousel-dot ${idx === i ? 'active' : ''}"></div>`
    ).join('');
    
    const arrowHtml = i < 5 ? `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>
    ` : '';

    const newNavHtml = `
        <div class="carousel-dots">${dotsHtml}</div>
        ${arrowHtml}
    `;

    // Regex to match the old carousel-nav block
    const regex = /<div class="carousel-nav">[\s\S]*?<\/div>\s*<\/div>/g;
    // We will do a generic replace but since there are 6, doing it frame by frame is safer.
}

// Actually, let's just regex replace all <div class="carousel-nav">...</div>
// Wait, the SVG is inside it.
html = html.replace(/<div class="carousel-nav">([\s\S]*?)<div class="carousel-dots">([\s\S]*?)<\/div>([\s\S]*?)<\/div>/g, (match, p1, dots, arrow) => {
    // If arrow contains SVG, replace it with new SVG
    let newArrow = '';
    if (arrow.includes('<svg')) {
        newArrow = `
        <svg class="carousel-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <polyline points="15 5 22 12 15 19"></polyline>
        </svg>`;
    }
    return `
        <div class="carousel-dots">${dots}</div>
        ${newArrow}
    `;
});


fs.writeFileSync(file, html, 'utf8');
console.log('✅ Arrows moved to right and made bigger.');
