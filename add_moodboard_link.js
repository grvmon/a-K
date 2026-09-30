const fs = require('fs');
const file = '/Users/gauravmongia/Desktop/a&k Website/style-guide/index.html';
let html = fs.readFileSync(file, 'utf8');

// Add to sidebar
const newSidebarLink = '<a href="#imagery">8. Art Direction</a>\n            <a href="moodboard_final.html" target="_blank" style="font-size: 0.8rem; color: var(--text-copper-aaa); font-weight: 600;">↳ View Cinematic Moodboard</a>';
html = html.replace('<a href="#imagery">8. Art Direction</a>', newSidebarLink);

// Add to Imagery Section
const newSectionLink = `<h2 class="ds-section-title">8. Photographic Art Direction</h2>
            <p class="ds-section-desc">Builder 3D renders natively look cheap and hyper-saturated. We enforce a global <code>filter: saturate(0.85) contrast(1.05);</code> to establish a cohesive, moody, high-end editorial grade.</p>
            <div style="margin-bottom: 2rem;">
                <a href="moodboard_final.html" target="_blank" class="ak-btn-primary" style="display:inline-flex; align-items:center; gap:0.5rem;">
                    View Cinematic Moodboard (6 Frames)
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
            </div>`;
html = html.replace(
    /<h2 class="ds-section-title">8\. Photographic Art Direction<\/h2>\s*<p class="ds-section-desc">Builder 3D renders natively look cheap and hyper-saturated\. We enforce a global <code>filter: saturate\(0\.85\) contrast\(1\.05\);<\/code> to establish a cohesive, moody, high-end editorial grade\.<\/p>/,
    newSectionLink
);

fs.writeFileSync(file, html, 'utf8');
console.log('✅ Moodboard link added to Style Guide.');
