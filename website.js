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
0: 'style-guide/assets/market_lens_ready_vs_uc.jpg?v=44260811_flush_cache_v20',
1: 'style-guide/assets/market_lens_builder.jpg?v=44260811_flush_cache_v20',
2: 'style-guide/assets/market_lens_corridor.jpg?v=44260811_flush_cache_v20',
3: 'style-guide/assets/market_lens_floor.jpg?v=44260811_flush_cache_v20',
4: 'style-guide/assets/market_lens_home_inv.jpg?v=44260811_flush_cache_v20'
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