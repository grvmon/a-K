document.addEventListener('DOMContentLoaded', function () {
if (typeof feather !== 'undefined') {
feather.replace();
}
const headerNav = document.getElementById('header-nav');
const hasHero = document.querySelector('.hero-section');

window.addEventListener('scroll', function () {
    if (headerNav) {
        if (window.scrollY > 30) {
            headerNav.classList.add('scrolled');
        } else {
            headerNav.classList.remove('scrolled');
        }
    }
});
const mobileBtn = document.getElementById('mobile-toggle-btn');
const mobileDrawer = document.getElementById('mobile-drawer');
const mobileNavOverlay = document.getElementById('mobile-nav-overlay');
const mobileDrawerClose = document.getElementById('mobile-drawer-close');
function openMobileDrawer() {
if (mobileDrawer) mobileDrawer.classList.add('is-active');
if (mobileNavOverlay) mobileNavOverlay.classList.add('is-active');
if (mobileBtn) {
mobileBtn.classList.add('is-active');
mobileBtn.setAttribute('aria-expanded', 'true');
}
document.body.classList.add('drawer-open');
}
function closeMobileDrawer() {
if (mobileDrawer) mobileDrawer.classList.remove('is-active');
if (mobileNavOverlay) mobileNavOverlay.classList.remove('is-active');
if (mobileBtn) {
mobileBtn.classList.remove('is-active');
mobileBtn.setAttribute('aria-expanded', 'false');
}
document.body.classList.remove('drawer-open');
}
if (mobileBtn) {
mobileBtn.addEventListener('click', function (e) {
e.stopPropagation();
if (mobileDrawer && mobileDrawer.classList.contains('is-active')) {
closeMobileDrawer();
} else {
openMobileDrawer();
}
});
}
if (mobileDrawerClose) {
mobileDrawerClose.addEventListener('click', function () {
closeMobileDrawer();
});
}
if (mobileNavOverlay) {
mobileNavOverlay.addEventListener('click', function () {
closeMobileDrawer();
});
}
document.addEventListener('keydown', function (e) {
if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('is-active')) {
closeMobileDrawer();
}
});
if (mobileDrawer) {
const drawerLinks = mobileDrawer.querySelectorAll('a');
drawerLinks.forEach(function (link) {
link.addEventListener('click', function () {
closeMobileDrawer();
});
});
}
const hubGridMatrix = document.querySelector('.hub-grid-matrix');
if (hubGridMatrix) {
const observerOptions = {
root: null,
threshold: 0.2
};
const observer = new IntersectionObserver(function (entries) {
entries.forEach(function (entry) {
if (entry.isIntersecting) {
entry.target.classList.add('animated');
} else {
entry.target.classList.remove('animated');
}
});
}, observerOptions);
observer.observe(hubGridMatrix);
}
const processCards = document.querySelectorAll('.market-lens-card');
const processSection = document.getElementById('buyers-checklist');
const processImg = document.getElementById('process-visual-img');
const stepImages = {
0: 'style-guide/assets/market_lens_ready_vs_uc.webp?v=20260816_flush_cache_v62',
1: 'style-guide/assets/market_lens_builder.webp?v=20260816_flush_cache_v62',
2: 'style-guide/assets/market_lens_corridor.webp?v=20260816_flush_cache_v62',
3: 'style-guide/assets/market_lens_floor.webp?v=20260816_flush_cache_v62',
4: 'style-guide/assets/market_lens_home_inv.webp?v=20260816_flush_cache_v62'
};
function updateStepVisual(stepIndex) {
if (!processImg) return;
const targetSrc = stepImages[stepIndex] || stepImages[0];
if (processImg.getAttribute('src') !== targetSrc) {
processImg.classList.add('fade-out');
setTimeout(function () {
processImg.setAttribute('src', targetSrc);
processImg.classList.remove('fade-out');
}, 180);
}
}
if (processCards.length > 0 && processSection) {
let currentStep = 0;
let stepTimer = null;
let isUserHovering = false;
function highlightStep(index) {
processCards.forEach(function (card, i) {
if (i === index) {
card.classList.add('active-step');
} else {
card.classList.remove('active-step');
}
});
updateStepVisual(index);
}
function advanceStep() {
if (isUserHovering) return;
highlightStep(currentStep);
currentStep = (currentStep + 1) % processCards.length;
}
function startLoop() {
if (!stepTimer) {
advanceStep();
stepTimer = setInterval(advanceStep, 2200);
}
}
function stopLoop() {
if (stepTimer) {
clearInterval(stepTimer);
stepTimer = null;
}
}
processCards.forEach(function (card, idx) {
card.addEventListener('mouseenter', function () {
isUserHovering = true;
stopLoop();
highlightStep(idx);
});
card.addEventListener('mouseleave', function () {
isUserHovering = false;
currentStep = (idx + 1) % processCards.length;
startLoop();
});
card.addEventListener('click', function () {
highlightStep(idx);
});
});
const processObserver = new IntersectionObserver(function (entries) {
entries.forEach(function (entry) {
if (entry.isIntersecting) {
startLoop();
} else {
stopLoop();
}
});
}, { threshold: 0.2 });
processObserver.observe(processSection);
}
const frameworkCards = document.querySelectorAll('.framework-card');
const frameworkSection = document.getElementById('framework');
if (frameworkCards.length > 0 && frameworkSection) {
let currentFrameworkStep = 0;
let frameworkTimer = null;
let isFrameworkHovering = false;
function highlightFrameworkStep(index) {
frameworkCards.forEach(function (card, i) {
if (i === index) {
card.classList.add('active-step');
} else {
card.classList.remove('active-step');
}
});
}
function advanceFrameworkStep() {
if (isFrameworkHovering) return;
highlightFrameworkStep(currentFrameworkStep);
currentFrameworkStep = (currentFrameworkStep + 1) % frameworkCards.length;
}
function startFrameworkLoop() {
if (!frameworkTimer) {
advanceFrameworkStep();
frameworkTimer = setInterval(advanceFrameworkStep, 2200);
}
}
function stopFrameworkLoop() {
if (frameworkTimer) {
clearInterval(frameworkTimer);
frameworkTimer = null;
}
}
frameworkCards.forEach(function (card, idx) {
card.addEventListener('mouseenter', function () {
isFrameworkHovering = true;
stopFrameworkLoop();
highlightFrameworkStep(idx);
});
card.addEventListener('mouseleave', function () {
isFrameworkHovering = false;
currentFrameworkStep = (idx + 1) % frameworkCards.length;
startFrameworkLoop();
});
card.addEventListener('click', function () {
highlightFrameworkStep(idx);
});
});
const frameworkObserver = new IntersectionObserver(function (entries) {
entries.forEach(function (entry) {
if (entry.isIntersecting) {
startFrameworkLoop();
} else {
stopFrameworkLoop();
}
});
}, { threshold: 0.2 });
frameworkObserver.observe(frameworkSection);
}
const wawRevealEls = document.querySelectorAll('.waw-reveal');
if (wawRevealEls.length > 0) {
var wawDelay = 0;
const wawObserver = new IntersectionObserver(function (entries) {
entries.forEach(function (entry) {
if (entry.isIntersecting) {
entry.target.classList.add('is-visible');
} else {
entry.target.classList.remove('is-visible');
}
});
}, { threshold: 0.15 });
wawRevealEls.forEach(function (el) {
wawObserver.observe(el);
});
}
const frameworkGrid = document.querySelector('.framework-grid');
const dots = document.querySelectorAll('.framework-carousel-dots .dot-btn');
if (frameworkGrid && dots.length > 0) {
let currentCardIndex = 0;
let autoScrollInterval = null;
let inactivityTimeout = null;
let isUserInteracting = false;
function updateDots(index) {
dots.forEach((dot, idx) => {
if (idx === index) {
dot.classList.add('active');
} else {
dot.classList.remove('active');
}
});
}
function scrollToCard(index) {
if (window.innerWidth > 991) return;
const wrappers = frameworkGrid.querySelectorAll('.framework-card-wrapper');
if (wrappers[index]) {
const targetCard = wrappers[index];
const scrollLeftPos = targetCard.offsetLeft - frameworkGrid.offsetLeft - 20;
frameworkGrid.scrollTo({
left: scrollLeftPos,
behavior: 'smooth'
});
currentCardIndex = index;
updateDots(index);
}
}
function startAutoScroll() {
if (isUserInteracting || window.innerWidth > 991) return;
stopAutoScroll();
autoScrollInterval = setInterval(() => {
const wrappers = frameworkGrid.querySelectorAll('.framework-card-wrapper');
currentCardIndex = (currentCardIndex + 1) % wrappers.length;
scrollToCard(currentCardIndex);
}, 6500);
}
function stopAutoScroll() {
if (autoScrollInterval) {
clearInterval(autoScrollInterval);
autoScrollInterval = null;
}
}
function handleUserInteractionStart() {
isUserInteracting = true;
stopAutoScroll();
if (inactivityTimeout) {
clearTimeout(inactivityTimeout);
inactivityTimeout = null;
}
}
function handleUserInteractionEnd() {
if (inactivityTimeout) clearTimeout(inactivityTimeout);
inactivityTimeout = setTimeout(() => {
isUserInteracting = false;
startAutoScroll();
}, 8500);
}
frameworkGrid.addEventListener('touchstart', handleUserInteractionStart, { passive: true });
frameworkGrid.addEventListener('touchend', handleUserInteractionEnd, { passive: true });
frameworkGrid.addEventListener('mousedown', handleUserInteractionStart);
frameworkGrid.addEventListener('mouseup', handleUserInteractionEnd);
frameworkGrid.addEventListener('mouseenter', handleUserInteractionStart);
frameworkGrid.addEventListener('mouseleave', handleUserInteractionEnd);
let cardWidth = 0;
function updateCardWidth() {
const wrappers = frameworkGrid.querySelectorAll('.framework-card-wrapper');
if (wrappers.length > 0) {
cardWidth = wrappers[0].offsetWidth + 16;
}
}
updateCardWidth();
window.addEventListener('resize', updateCardWidth);
let isScrollDebouncing = false;
frameworkGrid.addEventListener('scroll', () => {
if (!isScrollDebouncing) {
window.requestAnimationFrame(() => {
const wrappers = frameworkGrid.querySelectorAll('.framework-card-wrapper');
if (wrappers.length > 0) {
const scrollLeft = frameworkGrid.scrollLeft;
if (!cardWidth) updateCardWidth();
const calculatedIndex = Math.round(scrollLeft / (cardWidth || 1));
const clampedIndex = Math.max(0, Math.min(wrappers.length - 1, calculatedIndex));
if (clampedIndex !== currentCardIndex) {
currentCardIndex = clampedIndex;
updateDots(clampedIndex);
}
}
isScrollDebouncing = false;
});
isScrollDebouncing = true;
}
}, { passive: true });
dots.forEach((dot, idx) => {
dot.addEventListener('click', () => {
handleUserInteractionStart();
scrollToCard(idx);
handleUserInteractionEnd();
});
});
if (window.innerWidth <= 991) {
startAutoScroll();
}
window.addEventListener('resize', () => {
if (window.innerWidth <= 991) {
startAutoScroll();
} else {
stopAutoScroll();
}
});
}
const testimonialsContainer = document.querySelector('.credentials-col');
const testimonialDots = document.querySelectorAll('.testimonials-carousel-dots .dot-btn');
if (testimonialsContainer && testimonialDots.length > 0) {
let currentTestimonialIndex = 0;
let tAutoScrollInterval = null;
let tInactivityTimeout = null;
let isTUserInteracting = false;
function updateTestimonialDots(index) {
testimonialDots.forEach((dot, idx) => {
if (idx === index) {
dot.classList.add('active');
} else {
dot.classList.remove('active');
}
});
}
function scrollToTestimonial(index) {
if (window.innerWidth > 991) return;
const tCards = testimonialsContainer.querySelectorAll('.testimonial-card');
if (tCards[index]) {
const targetCard = tCards[index];
const scrollLeftPos = targetCard.offsetLeft - testimonialsContainer.offsetLeft - 20;
testimonialsContainer.scrollTo({
left: scrollLeftPos,
behavior: 'smooth'
});
currentTestimonialIndex = index;
updateTestimonialDots(index);
}
}
function startTestimonialAutoScroll() {
if (isTUserInteracting || window.innerWidth > 991) return;
stopTestimonialAutoScroll();
tAutoScrollInterval = setInterval(() => {
const tCards = testimonialsContainer.querySelectorAll('.testimonial-card');
currentTestimonialIndex = (currentTestimonialIndex + 1) % tCards.length;
scrollToTestimonial(currentTestimonialIndex);
}, 6500);
}
function stopTestimonialAutoScroll() {
if (tAutoScrollInterval) {
clearInterval(tAutoScrollInterval);
tAutoScrollInterval = null;
}
}
function handleTUserStart() {
isTUserInteracting = true;
stopTestimonialAutoScroll();
if (tInactivityTimeout) {
clearTimeout(tInactivityTimeout);
tInactivityTimeout = null;
}
}
function handleTUserEnd() {
if (tInactivityTimeout) clearTimeout(tInactivityTimeout);
tInactivityTimeout = setTimeout(() => {
isTUserInteracting = false;
startTestimonialAutoScroll();
}, 8500);
}
testimonialsContainer.addEventListener('touchstart', handleTUserStart, { passive: true });
testimonialsContainer.addEventListener('touchend', handleTUserEnd, { passive: true });
testimonialsContainer.addEventListener('mousedown', handleTUserStart);
testimonialsContainer.addEventListener('mouseup', handleTUserEnd);
testimonialsContainer.addEventListener('mouseenter', handleTUserStart);
testimonialsContainer.addEventListener('mouseleave', handleTUserEnd);
let tCardWidth = 0;
function updateTCardWidth() {
const tCards = testimonialsContainer.querySelectorAll('.testimonial-card');
if (tCards.length > 0) {
tCardWidth = tCards[0].offsetWidth + 16;
}
}
updateTCardWidth();
window.addEventListener('resize', updateTCardWidth);
let isTScrollDebouncing = false;
testimonialsContainer.addEventListener('scroll', () => {
if (!isTScrollDebouncing) {
window.requestAnimationFrame(() => {
const tCards = testimonialsContainer.querySelectorAll('.testimonial-card');
if (tCards.length > 0) {
const scrollLeft = testimonialsContainer.scrollLeft;
if (!tCardWidth) updateTCardWidth();
const calculatedIndex = Math.round(scrollLeft / (tCardWidth || 1));
const clampedIndex = Math.max(0, Math.min(tCards.length - 1, calculatedIndex));
if (clampedIndex !== currentTestimonialIndex) {
currentTestimonialIndex = clampedIndex;
updateTestimonialDots(clampedIndex);
}
}
isTScrollDebouncing = false;
});
isTScrollDebouncing = true;
}
}, { passive: true });
testimonialDots.forEach((dot, idx) => {
dot.addEventListener('click', () => {
handleTUserStart();
scrollToTestimonial(idx);
handleTUserEnd();
});
});
if (window.innerWidth <= 991) {
startTestimonialAutoScroll();
}
window.addEventListener('resize', () => {
if (window.innerWidth <= 991) {
startTestimonialAutoScroll();
} else {
stopTestimonialAutoScroll();
}
});
}
const premiumRevealElements = document.querySelectorAll('.premium-reveal');
const premiumObserver = new IntersectionObserver((entries) => {
entries.forEach(entry => {
const el = entry.target;
if (entry.isIntersecting) {
if (el.dataset.staggerChildren) {
const children = el.querySelectorAll(el.dataset.staggerChildren);
children.forEach((child, index) => {
child.style.transitionDelay = `${index * 80}ms`;
child.classList.add('revealed');
});
}
el.classList.add('revealed');
} else {
if (el.dataset.staggerChildren) {
const children = el.querySelectorAll(el.dataset.staggerChildren);
children.forEach((child) => {
child.style.transitionDelay = '0ms';
child.classList.remove('revealed');
});
}
el.classList.remove('revealed');
}
});
}, {
root: null,
threshold: 0.08,
rootMargin: '0px 0px -40px 0px'
});
    premiumRevealElements.forEach(el => {
        premiumObserver.observe(el);
    });

    // Editorial & Long-Form Reading Progress Bar
    const hasLongContent = document.querySelector('.blog-article-content, .privacy-body, .prop-container, .editorial-layout, .blog-post-content');
    if (hasLongContent) {
        let track = document.querySelector('.reading-progress-track');
        if (!track) {
            track = document.createElement('div');
            track.className = 'reading-progress-track';
            track.innerHTML = '<div class="reading-progress-fill"></div>';
            document.body.appendChild(track);
        }
        const fill = track.querySelector('.reading-progress-fill');
        window.addEventListener('scroll', function () {
            const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
            if (totalHeight > 0 && fill) {
                const progress = (window.scrollY / totalHeight) * 100;
                fill.style.width = Math.min(100, Math.max(0, progress)) + '%';
            }
        }, { passive: true });
    }
});
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

    const heroImage = document.querySelector('.hero-visual-card img');

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animate() {
        cursorX += (mouseX - cursorX) * speed;
        cursorY += (mouseY - cursorY) * speed;
        cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
        
        if (heroImage) {
            const centerX = window.innerWidth / 2;
            const centerY = window.innerHeight / 2;
            const offsetX = ((cursorX - centerX) / centerX) * -16; 
            const offsetY = ((cursorY - centerY) / centerY) * -16;
            heroImage.style.transform = `scale(0.75) translate(${offsetX}px, ${offsetY}px)`;
        }
        
        requestAnimationFrame(animate);
    }
    animate();

    // Map elements to states automatically
    const discoverSelectors = 'a, button, .sd-btn-gold, .premium-inline-cta, .nav-cta-btn';
    const exploreSelectors = '.market-lens-card, .framework-card, .waw-story-card, .waw-founder-card';
    const inspectSelectors = 'img, .hero-visual-card, .market-lens-image-wrapper';
    
    document.querySelectorAll(discoverSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { cursor.classList.add('hover-discover'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-discover'); });
    });

    document.querySelectorAll(exploreSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { cursor.classList.add('hover-explore'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-explore'); });
    });
    
    document.querySelectorAll(inspectSelectors).forEach(el => {
        el.addEventListener('mouseenter', () => { cursor.classList.add('hover-inspect'); });
        el.addEventListener('mouseleave', () => { cursor.classList.remove('hover-inspect'); });
    });
});

/* ========================================= */
/* MOBILE-ONLY WHATSAPP CHATBOT ENTRY POINT  */
/* ========================================= */
(function () {
    function initWhatsAppCTA() {
        if (document.getElementById('ank-wa-float')) return;

        // 1. Capture & Store UTM Parameters
        var params = new URLSearchParams(window.location.search);
        var utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
        var capturedUtms = {};

        // Retrieve existing UTMs from storage if present
        try {
            var stored = sessionStorage.getItem('ank_utm_params') || localStorage.getItem('ank_utm_params');
            if (stored) {
                capturedUtms = JSON.parse(stored);
            }
        } catch (e) {}

        // Check current URL for new UTM parameters
        var hasNewUtms = false;
        utmKeys.forEach(function (key) {
            var val = params.get(key);
            if (val) {
                capturedUtms[key] = val.trim();
                hasNewUtms = true;
            }
        });

        // Save updated UTM parameters to storage
        if (hasNewUtms) {
            try {
                sessionStorage.setItem('ank_utm_params', JSON.stringify(capturedUtms));
                localStorage.setItem('ank_utm_params', JSON.stringify(capturedUtms));
            } catch (e) {}
        }

        // 2. Generate Compact Tracking Token
        function getRefToken() {
            var parts = [];
            if (capturedUtms.utm_source) parts.push(capturedUtms.utm_source);
            if (capturedUtms.utm_medium) parts.push(capturedUtms.utm_medium);
            if (capturedUtms.utm_campaign) parts.push(capturedUtms.utm_campaign);

            if (parts.length === 0) return '';
            return parts.join('-').replace(/[^a-zA-Z0-9\-_]/g, '').substring(0, 45);
        }

        // 3. Build WhatsApp Prefilled URL
        function getWhatsAppUrl() {
            var token = getRefToken();
            var msg = "Hi, I'm interested in buying a property.";
            if (token) {
                msg += " Ref: " + token;
            }
            return "https://wa.me/916360981986?text=" + encodeURIComponent(msg);
        }

        // 4. Create Floating Button Element
        var waBtn = document.createElement('a');
        waBtn.id = 'ank-wa-float';
        waBtn.className = 'ank-wa-float';
        waBtn.href = getWhatsAppUrl();
        waBtn.target = '_blank';
        waBtn.rel = 'noopener noreferrer';
        waBtn.setAttribute('aria-label', 'Chat with AcreNKey Home Buyer Concierge on WhatsApp');

        waBtn.innerHTML = 
            '<span class="ank-wa-icon-bubble" aria-hidden="true">' +
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="18" height="18">' +
                    '<path fill="#FFFFFF" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3 18.6-68.1-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>' +
                '</svg>' +
            '</span>' +
            '<span class="ank-wa-label">' +
                '<span class="ank-wa-label-long">Chat with our Home Buyer Concierge</span>' +
                '<span class="ank-wa-label-short">Chat Concierge</span>' +
            '</span>';

        // 5. Fire Analytics Event on Click
        waBtn.addEventListener('click', function () {
            try {
                waBtn.href = getWhatsAppUrl();

                var eventPayload = {
                    event: 'whatsapp_chat_started',
                    utm_source: capturedUtms.utm_source || '',
                    utm_medium: capturedUtms.utm_medium || '',
                    utm_campaign: capturedUtms.utm_campaign || '',
                    utm_content: capturedUtms.utm_content || '',
                    utm_term: capturedUtms.utm_term || ''
                };

                if (typeof window.dataLayer !== 'undefined' && Array.isArray(window.dataLayer)) {
                    window.dataLayer.push(eventPayload);
                }
                if (typeof window.gtag === 'function') {
                    window.gtag('event', 'whatsapp_chat_started', eventPayload);
                }
            } catch (err) {
                // Silently ignore analytics error so WhatsApp link is never blocked
            }
        });

        document.body.appendChild(waBtn);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initWhatsAppCTA);
    } else {
        initWhatsAppCTA();
    }
})();

/* ========================================= */
/* MOBILE-ONLY WHATSAPP CHATBOT ENTRY POINT  */
/* ========================================= */
(function () {
    function initWhatsAppCTA() {
        if (document.getElementById('ank-wa-float')) return;

        // 1. Capture & Store UTM Parameters
        var params = new URLSearchParams(window.location.search);
        var utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
        var capturedUtms = {};

        // Retrieve existing UTMs from storage if present
        try {
            var stored = sessionStorage.getItem('ank_utm_params') || localStorage.getItem('ank_utm_params');
            if (stored) {
                capturedUtms = JSON.parse(stored);
            }
        } catch (e) {}

        // Check current URL for new UTM parameters
        var hasNewUtms = false;
        utmKeys.forEach(function (key) {
            var val = params.get(key);
            if (val) {
                capturedUtms[key] = val.trim();
                hasNewUtms = true;
            }
        });

        // Save updated UTM parameters to storage
        if (hasNewUtms) {
            try {
                sessionStorage.setItem('ank_utm_params', JSON.stringify(capturedUtms));
                localStorage.setItem('ank_utm_params', JSON.stringify(capturedUtms));
            } catch (e) {}
        }

        // 2. Generate Compact Tracking Token
        function getRefToken() {
            var parts = [];
            if (capturedUtms.utm_source) parts.push(capturedUtms.utm_source);
            if (capturedUtms.utm_medium) parts.push(capturedUtms.utm_medium);
            if (capturedUtms.utm_campaign) parts.push(capturedUtms.utm_campaign);

            if (parts.length === 0) return '';
            return parts.join('-').replace(/[^a-zA-Z0-9\-_]/g, '').substring(0, 45);
        }

        // 3. Build WhatsApp Prefilled URL
        function getWhatsAppUrl() {
            var token = getRefToken();
            var msg = "Hi, I'm interested in buying a property.";
            if (token) {
                msg += " Ref: " + token;
            }
            return "https://wa.me/916360981986?text=" + encodeURIComponent(msg);
        }

        // 4. Create Floating Button Element
        var waBtn = document.createElement('a');
        waBtn.id = 'ank-wa-float';
        waBtn.className = 'ank-wa-float';
        waBtn.href = getWhatsAppUrl();
        waBtn.target = '_blank';
        waBtn.rel = 'noopener noreferrer';
        waBtn.setAttribute('aria-label', 'Chat with AcreNKey Home Buyer Concierge on WhatsApp');

        waBtn.innerHTML = 
            '<span class="ank-wa-icon-bubble" aria-hidden="true">' +
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="18" height="18">' +
                    '<path fill="#FFFFFF" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3 18.6-68.1-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>' +
                '</svg>' +
            '</span>' +
            '<span class="ank-wa-label">' +
                '<span class="ank-wa-label-long">Chat with our Home Buyer Concierge</span>' +
                '<span class="ank-wa-label-short">Chat Concierge</span>' +
            '</span>';

        // 5. Fire Analytics Event on Click
        waBtn.addEventListener('click', function () {
            try {
                waBtn.href = getWhatsAppUrl();

                var eventPayload = {
                    event: 'whatsapp_chat_started',
                    utm_source: capturedUtms.utm_source || '',
                    utm_medium: capturedUtms.utm_medium || '',
                    utm_campaign: capturedUtms.utm_campaign || '',
                    utm_content: capturedUtms.utm_content || '',
                    utm_term: capturedUtms.utm_term || ''
                };

                if (typeof window.dataLayer !== 'undefined' && Array.isArray(window.dataLayer)) {
                    window.dataLayer.push(eventPayload);
                }
                if (typeof window.gtag === 'function') {
                    window.gtag('event', 'whatsapp_chat_started', eventPayload);
                }
            } catch (err) {
                // Silently ignore analytics error so WhatsApp link is never blocked
            }
        });

        document.body.appendChild(waBtn);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initWhatsAppCTA);
    } else {
        initWhatsAppCTA();
    }
})();
