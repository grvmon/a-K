const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Add Cinematic Animations and Text Shadows
const newCSS = `
        .frame-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: saturate(0.85) contrast(1.05);
            /* Cinematic Slow Zoom */
            transform: scale(1.01);
            transition: transform 1s ease-out;
            animation: slowPan 25s ease-in-out infinite alternate;
        }
        @keyframes slowPan {
            0% { transform: scale(1.0); }
            100% { transform: scale(1.08); }
        }
        .frame-text, .brand-logo-josefin, .brand-sub {
            /* Editorial Crispness */
            text-shadow: 0 4px 32px rgba(0,0,0,0.5);
        }
`;
html = html.replace(/\.frame-img \{[\s\S]*?filter: saturate\(0\.85\) contrast\(1\.05\);\n        \}/, newCSS);


// 2. Add JavaScript to make the Arrows functional
const jsSnippet = `
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
</body>`;
html = html.replace(/<\/body>/, jsSnippet);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Slides upgraded with cinematic motion and interactivity.');
