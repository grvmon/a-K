const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// Update CSS for dots and arrows
const newCSS = `
        /* Carousel Navigation */
        .carousel-nav-container {
            position: absolute;
            bottom: 7.5%; /* 120px from bottom */
            left: 8.33%; /* 100px from left */
            right: 8.33%; /* 100px from right */
            height: 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 10;
        }
        .carousel-dots {
            display: flex;
            align-items: center;
            gap: 1.25rem;
        }
        .carousel-dot {
            width: 14px;
            height: 14px;
            border-radius: 50%;
            border: 2px solid rgba(255, 255, 255, 0.9);
            box-sizing: border-box;
        }
        .carousel-dot.active {
            background-color: rgba(255, 255, 255, 0.9);
        }
        .carousel-arrow-right {
            width: 48px;
            height: 48px;
            color: rgba(255, 255, 255, 0.9);
            transition: transform 0.4s ease;
            cursor: pointer;
        }
        .carousel-arrow-right:hover {
            transform: translateX(5px);
        }
`;
html = html.replace(/\/\* Carousel Navigation \*\/[\s\S]*?\.carousel-arrow-right:hover \{[\s\S]*?\}/, newCSS);

// We need to replace the floating <div class="carousel-dots"> and <svg> with the container.
// Since we generated them predictably in fix_dom.js, we can replace them securely.
html = html.replace(/<div class="carousel-dots">([\s\S]*?)<\/div>\s*(<svg class="carousel-arrow-right"[\s\S]*?<\/svg>)?/g, (match, dots, arrow) => {
    return `
        <div class="carousel-nav-container">
            <div class="carousel-dots">${dots}</div>
            ${arrow ? arrow : '<div></div>'}
        </div>`;
});

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Nav container aligned.');
