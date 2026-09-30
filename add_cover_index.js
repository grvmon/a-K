const fs = require('fs');
const indexFile = '/Users/gauravmongia/Desktop/a&k Website/style-guide/index.html';
let indexHtml = fs.readFileSync(indexFile, 'utf8');

const linkedinButton = '<a href="linkedin-ads-moodboard.html" target="_blank" class="ds-button ds-button-secondary" style="margin-top:1rem; border: 1px solid var(--neutral-grey); padding: 0.75rem 1.5rem; color: var(--titanium-frost); text-decoration: none; border-radius: 4px; display: inline-block;">View LinkedIn Feed Presentation (1:1)</a>';
const coverButton = '<a href="linkedin-cover.html" target="_blank" class="ds-button ds-button-secondary" style="margin-top:1rem; border: 1px solid var(--neutral-grey); padding: 0.75rem 1.5rem; color: var(--titanium-frost); text-decoration: none; border-radius: 4px; display: inline-block;">View LinkedIn Company Page Cover (1128x191)</a>';

if (!indexHtml.includes('View LinkedIn Company Page Cover')) {
    indexHtml = indexHtml.replace(linkedinButton, `${linkedinButton}<br>${coverButton}`);
    fs.writeFileSync(indexFile, indexHtml, 'utf8');
}
