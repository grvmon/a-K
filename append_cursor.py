import sys

cursor_css = """
/* ========================================= */
/* PREMIUM PRECISION FRAME CURSOR SYSTEM     */
/* ========================================= */
@media (min-width: 992px) {
    body, html, a, button, .sd-btn-gold, .premium-inline-cta, .nav-cta-btn {
        cursor: none !important;
    }
    
    #custom-cursor {
        position: fixed;
        top: 0;
        left: 0;
        width: 32px;
        height: 32px;
        pointer-events: none;
        z-index: 999999;
        transform: translate(-50%, -50%);
        mix-blend-mode: difference;
        color: #F7F5F0;
        transition: color 0.3s ease;
    }

    .cursor-dot {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 3px;
        height: 3px;
        background-color: #9B6248;
        border-radius: 50%;
        transition: opacity 0.25s ease;
    }

    .cursor-frame {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
                    width 0.25s cubic-bezier(0.16, 1, 0.3, 1), 
                    height 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .cursor-frame .bracket {
        position: absolute;
        width: 8px;
        height: 8px;
        border-color: currentColor;
        border-style: solid;
        transition: border-width 0.25s ease, width 0.25s ease, height 0.25s ease;
    }

    .cursor-frame .bracket.tl { top: 0; left: 0; border-width: 1px 0 0 1px; }
    .cursor-frame .bracket.tr { top: 0; right: 0; border-width: 1px 1px 0 0; }
    .cursor-frame .bracket.bl { bottom: 0; left: 0; border-width: 0 0 1px 1px; }
    .cursor-frame .bracket.br { bottom: 0; right: 0; border-width: 0 1px 1px 0; }

    .cursor-label {
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 9px;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: currentColor;
        opacity: 0;
        white-space: nowrap;
        transition: opacity 0.2s ease, bottom 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        font-family: var(--font-heading, 'Marcellus', serif);
    }

    /* HOVER STATES */
    #custom-cursor.hover-inspect .cursor-frame { transform: scale(1.3); }
    #custom-cursor.hover-inspect .cursor-label { opacity: 1; bottom: -24px; }
    
    #custom-cursor.hover-explore .cursor-frame { transform: scale(1.15); }
    #custom-cursor.hover-explore .cursor-label { opacity: 1; bottom: -22px; }
    
    #custom-cursor.hover-discover .cursor-frame { transform: scale(0.9) rotate(45deg); }
    #custom-cursor.hover-discover .bracket { width: 10px; height: 10px; }
    #custom-cursor.hover-discover .cursor-label { opacity: 1; bottom: -26px; }
    
    #custom-cursor.hover-drag .cursor-frame { width: 60px; height: 20px; left: 50%; top: 50%; transform: translate(-50%, -50%); }
    #custom-cursor.hover-drag .cursor-dot { opacity: 0.3; }
    #custom-cursor.hover-drag .cursor-label { opacity: 1; bottom: -18px; }
}
@media (max-width: 991px) {
    #custom-cursor { display: none !important; }
}
"""

cursor_js = """
/* ========================================= */
/* PREMIUM PRECISION FRAME CURSOR SYSTEM     */
/* ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    // Only init on desktop
    if (window.innerWidth < 992) return;

    const cursorDiv = document.createElement('div');
    cursorDiv.id = 'custom-cursor';
    cursorDiv.innerHTML = `
        <div class="cursor-frame">
            <div class="bracket tl"></div>
            <div class="bracket tr"></div>
            <div class="bracket bl"></div>
            <div class="bracket br"></div>
        </div>
        <div class="cursor-dot"></div>
        <div class="cursor-label" id="cursor-label"></div>
    `;
    document.body.appendChild(cursorDiv);

    const cursor = cursorDiv;
    const label = document.getElementById('cursor-label');
    
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let cursorX = mouseX;
    let cursorY = mouseY;
    const speed = 0.2;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animate() {
        cursorX += (mouseX - cursorX) * speed;
        cursorY += (mouseY - cursorY) * speed;
        cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
        requestAnimationFrame(animate);
    }
    animate();

    // Map elements to states automatically
    const discoverSelectors = 'a, button, .sd-btn-gold, .premium-inline-cta, .nav-cta-btn';
    const exploreSelectors = '.market-lens-card, .framework-card, .waw-story-card, .waw-founder-card';
    const inspectSelectors = 'img, .hero-visual-card, .market-lens-image-wrapper';
    
    document.querySelectorAll(discoverSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { label.textContent = 'Discover'; cursor.classList.add('hover-discover'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-discover'); });
    });

    document.querySelectorAll(exploreSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { label.textContent = 'Explore'; cursor.classList.add('hover-explore'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-explore'); });
    });
    
    document.querySelectorAll(inspectSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { label.textContent = 'Inspect'; cursor.classList.add('hover-inspect'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-inspect'); });
    });
});
"""

# Append to CSS
with open('website.css', 'a', encoding='utf-8') as f:
    f.write(cursor_css)

with open('website.min.css', 'a', encoding='utf-8') as f:
    f.write(cursor_css)

# Append to JS
with open('website.js', 'a', encoding='utf-8') as f:
    f.write(cursor_js)

print("Injected into CSS and JS.")
