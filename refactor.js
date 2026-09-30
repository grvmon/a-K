const fs = require('fs');
const path = require('path');

const prestigePath = 'property/prestige-evergreen-raintree-park/index.html';
const alembicPath = 'property/alembic-cloud-forest-alembic-city/index.html';

let prestigeHTML = fs.readFileSync(prestigePath, 'utf8');
let alembicHTML = fs.readFileSync(alembicPath, 'utf8');

// 1. We need to implement the grid CSS since it doesn't exist.
const gridCSS = `
<style>
.prop-content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  gap: 2rem;
  align-items: start;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}
.prop-sidebar-column {
  position: sticky;
  top: 140px;
}
@media (max-width: 1024px) {
  .prop-content-grid { grid-template-columns: 1fr; }
  .prop-sidebar-column { position: static; margin-top: 2rem; }
}
</style>
`;

// Insert gridCSS before </head>
alembicHTML = alembicHTML.replace('</head>', gridCSS + '\n</head>');

// We are going to replace the hero grid of Alembic.
// Wait, Alembic has <div class="prop-hero-grid" style="align-items: stretch; gap: 36px;">
// We will change it to Prestige's style.
let prestigeHeroStart = prestigeHTML.indexOf('<div class="prop-hero-grid"');
let prestigeHeroEnd = prestigeHTML.indexOf('<div class="prop-snapshot-strip-v2">');
let prestigeHero = prestigeHTML.substring(prestigeHeroStart, prestigeHeroEnd);

// Actually, this is getting complex to do via Regex for HTML.
// Let's use Python's html parser? No, Python is fine for string replace.
