const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Add CSS for carousel navigation
const navCSS = `
        /* Carousel Navigation */
        .carousel-nav {
            position: absolute;
            bottom: 7.5%; /* Place it neatly in the bottom safe area */
            left: 8.33%; /* Align with left text margin */
            display: flex;
            align-items: center;
            gap: 1.5rem;
            z-index: 10;
            color: rgba(255, 255, 255, 0.9);
        }
        .carousel-dots {
            display: flex;
            align-items: center;
            gap: 0.6rem;
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
        .carousel-arrow {
            width: 24px;
            height: 24px;
            opacity: 0.9;
        }
`;
html = html.replace(/<\/style>/, navCSS + '\n    </style>');

// 2. Generate HTML block for each frame
const generateNav = (activeIndex, total = 6) => {
    let dotsHtml = '';
    for (let i = 0; i < total; i++) {
        dotsHtml += `<div class="carousel-dot ${i === activeIndex ? 'active' : ''}"></div>`;
    }
    
    // Only show right arrow if it's not the last slide
    const arrowHtml = activeIndex < total - 1 ? `
        <svg class="carousel-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="2" y1="12" x2="21" y2="12"></line>
            <polyline points="14 5 21 12 14 19"></polyline>
        </svg>
    ` : '';

    return `
        <div class="carousel-nav">
            <div class="carousel-dots">${dotsHtml}</div>
            ${arrowHtml}
        </div>
    `;
};

// 3. Inject into each frame
for (let i = 0; i < 6; i++) {
    const navHtml = generateNav(i);
    // Find the end of the .frame-overlay div for this slide and inject before its closing tag
    // Or just inject right before the end of the .frame div
    
    // We will inject it before the closing </div> of <div class="frame">
    const slideMarker = `<!-- 0${i + 1} -->`;
    const nextSlideMarker = i < 5 ? `<!-- 0${i + 2} -->` : '</body>';
    
    // Find the block between current marker and next marker
    let blockStart = html.indexOf(slideMarker);
    let blockEnd = html.indexOf(nextSlideMarker);
    
    let block = html.substring(blockStart, blockEnd);
    
    // Replace the last </div> in this block (which is the frame closing div) with navHtml + </div>
    const lastDivIndex = block.lastIndexOf('</div>');
    block = block.substring(0, lastDivIndex) + navHtml + '\n    </div>' + block.substring(lastDivIndex + 6);
    
    html = html.substring(0, blockStart) + block + html.substring(blockEnd);
}

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Carousel navigation added to all slides.');
