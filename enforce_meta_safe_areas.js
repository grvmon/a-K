const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Update text padding to 12.5% (150px on 1200, 200px on 1600)
// 2. Update nav container to 10% bottom and left/right (160px bottom, 120px left/right)
// 3. Make sure the typography respects this completely.

const oldCSS = `
        .frame-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, rgba(10, 10, 11, 0.95) 0%, rgba(10, 10, 11, 0.85) 35%, rgba(10, 10, 11, 0) 70%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            /* Safe Margins based on 1200x1600 */
            padding-top: 7.5%; /* 120px */
            padding-bottom: 11.25%; /* 180px */
            padding-left: 8.33%; /* 100px */
            padding-right: 8.33%; /* 100px */
            box-sizing: border-box;
        }
`;

const newOverlayCSS = `
        .frame-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, rgba(10, 10, 11, 0.95) 0%, rgba(10, 10, 11, 0.85) 35%, rgba(10, 10, 11, 0) 70%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            /* Typography Safe Zone (150px/200px) */
            padding-top: 12.5%;
            padding-bottom: 12.5%;
            padding-left: 12.5%;
            padding-right: 12.5%;
            box-sizing: border-box;
        }
`;

html = html.replace(/\.frame-overlay \{[\s\S]*?box-sizing: border-box;\n        \}/, newOverlayCSS);

const oldNavCSS = `
        /* Carousel Navigation */
        .carousel-nav-container {
            position: absolute;
            bottom: 7.5%; /* 120px from bottom */
            left: 8.33%; /* 100px from left */
            right: 8.33%; /* 100px from right */
`;

const newNavCSS = `
        /* Carousel Navigation */
        .carousel-nav-container {
            position: absolute;
            bottom: 10%; /* 160px from bottom (Critical Safe Area) */
            left: 10%; /* 120px from left */
            right: 10%; /* 120px from right */
`;

html = html.replace(/\/\* Carousel Navigation \*\/[\s\S]*?right: 8\.33%; \/\* 100px from right \*\//, newNavCSS);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Meta strict safe areas enforced.');
