const fs = require('fs');

const metaFile = '/Users/gauravmongia/Desktop/a&k Website/style-guide/meta-ads-moodboard.html';
const linkedinFile = '/Users/gauravmongia/Desktop/a&k Website/style-guide/linkedin-ads-moodboard.html';
const indexFile = '/Users/gauravmongia/Desktop/a&k Website/style-guide/index.html';

let metaHtml = fs.readFileSync(metaFile, 'utf8');

// 1. Change aspect ratio to 1:1 (1200x1200px)
let linkedinHtml = metaHtml.replace(/aspect-ratio: 1200 \/ 1600;/, 'aspect-ratio: 1200 / 1200;');

// 2. Adjust padding to 10% on all sides for square (120px)
linkedinHtml = linkedinHtml.replace(/padding-top: 12\.5%;/g, 'padding-top: 10%;');
linkedinHtml = linkedinHtml.replace(/padding-bottom: 12\.5%;/g, 'padding-bottom: 10%;');
linkedinHtml = linkedinHtml.replace(/padding-left: 12\.5%;/g, 'padding-left: 10%;');
linkedinHtml = linkedinHtml.replace(/padding-right: 12\.5%;/g, 'padding-right: 10%;');

// 3. Since the canvas is shorter (1200px height instead of 1600px), 10% bottom padding is 120px from bottom.
// We should put the nav container closer, maybe 6% from bottom.
linkedinHtml = linkedinHtml.replace(/bottom: 10%; \/\* 160px from bottom \(Critical Safe Area\) \*\//, 'bottom: 5%; /* 60px from bottom */');
linkedinHtml = linkedinHtml.replace(/left: 10%; \/\* 120px from left \*\//, 'left: 10%;');
linkedinHtml = linkedinHtml.replace(/right: 10%; \/\* 120px from right \*\//, 'right: 10%;');

// 4. Update the title
linkedinHtml = linkedinHtml.replace(/<title>.*?<\/title>/, '<title>Acre&Key — LinkedIn Moodboard</title>');

fs.writeFileSync(linkedinFile, linkedinHtml, 'utf8');

// 5. Update index.html to include the new button
let indexHtml = fs.readFileSync(indexFile, 'utf8');
const metaButton = '<a href="meta-ads-moodboard.html" target="_blank" class="ds-button ds-button-primary" style="margin-top:2rem;">View Final Meta Ads Presentation</a>';
const linkedinButton = '<a href="linkedin-ads-moodboard.html" target="_blank" class="ds-button ds-button-secondary" style="margin-top:1rem; border: 1px solid var(--neutral-grey); padding: 0.75rem 1.5rem; color: var(--titanium-frost); text-decoration: none; border-radius: 4px; display: inline-block;">View LinkedIn Feed Presentation (1:1)</a>';

if (!indexHtml.includes('View LinkedIn Feed Presentation')) {
    indexHtml = indexHtml.replace(metaButton, `${metaButton}<br>${linkedinButton}`);
    fs.writeFileSync(indexFile, indexHtml, 'utf8');
}

console.log('✅ LinkedIn Moodboard Created and added to Index.');
