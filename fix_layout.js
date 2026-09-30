const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/moodboard_final.html';
let html = fs.readFileSync(file, 'utf8');

// Update CSS for safe areas and 1 line text
const newStyles = `
        body {
            margin: 0;
            background-color: var(--obsidian-black);
            font-family: 'Manrope', sans-serif;
            color: var(--titanium-frost);
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            gap: 4rem;
            padding: 4rem 2rem;
        }
        .frame {
            position: relative;
            /* 1200 x 1600 canvas */
            width: 100%;
            max-width: 1200px;
            aspect-ratio: 1200 / 1600;
            overflow: hidden;
            background: #000;
            container-type: inline-size;
        }
        .frame-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: saturate(0.85) contrast(1.05);
        }
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
        .frame-text {
            font-family: 'Marcellus', serif;
            font-size: 6.5cqw; /* Scales perfectly with width to stay on 1 line */
            font-weight: 400;
            color: var(--titanium-frost);
            margin: 0;
            line-height: 1.1;
            letter-spacing: -0.02em;
            white-space: nowrap; /* Force one line */
        }
        .center-overlay {
            justify-content: center;
            align-items: center;
            text-align: center;
            background: rgba(10, 10, 11, 0.75);
        }
        .brand-logo {
            font-family: 'Marcellus', serif;
            font-size: 8cqw;
            color: var(--titanium-frost);
            margin-bottom: 0.5rem;
        }
        .brand-sub {
            font-family: 'Manrope', sans-serif;
            font-size: 2.5cqw;
            color: rgba(250, 250, 250, 0.8);
            text-transform: uppercase;
            letter-spacing: 0.15em;
            font-weight: 600;
        }
`;

html = html.replace(/body {[\s\S]*?\.meta-label {[\s\S]*?}/, newStyles);

// Remove the <br> in Frame 3
html = html.replace('Find. Check. Inspect.<br>Negotiate.', 'Find. Check. Inspect. Negotiate.');

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Safe areas and 1-line text constraints applied.');
