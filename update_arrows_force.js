const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// Strip out ALL existing nav elements
html = html.replace(/<div class="carousel-dots">[\s\S]*?<\/div>/g, '');
html = html.replace(/<svg class="carousel-arrow"[\s\S]*?<\/svg>/g, '');
html = html.replace(/<svg class="carousel-arrow-right"[\s\S]*?<\/svg>/g, '');

// Strip out any empty <div class="carousel-nav">
html = html.replace(/<div class="carousel-nav">\s*<\/div>/g, '');
html = html.replace(/<div class="carousel-nav">\s*<div class="carousel-dot active">\s*<\/div>\s*<\/div>/g, ''); // leftover garbage

// We will inject fresh nav just before the closing </div> of each frame.
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

    const marker = `<!-- 0${i+1} -->`;
    const nextMarker = i < 5 ? `<!-- 0${i+2} -->` : '</body>';
    
    let blockStart = html.indexOf(marker);
    let blockEnd = html.indexOf(nextMarker);
    let block = html.substring(blockStart, blockEnd);
    
    const lastDivIndex = block.lastIndexOf('</div>');
    block = block.substring(0, lastDivIndex) + newNavHtml + '\n    </div>' + block.substring(lastDivIndex + 6);
    
    html = html.substring(0, blockStart) + block + html.substring(blockEnd);
}

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Nav forced.');
