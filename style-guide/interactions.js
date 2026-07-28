document.addEventListener('DOMContentLoaded', () => {
    const staggerElements = document.querySelectorAll('.stagger-1, .stagger-2, .stagger-3');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
        staggerElements.forEach(el => el.classList.add('is-visible'));
        return;
    }

    // 1. Magnetic Buttons
    const magneticBtns = document.querySelectorAll('.sd-btn--magnetic');

    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;
            const distX = e.clientX - x;
            const distY = e.clientY - y;
            const pullX = distX * 0.2;
            const pullY = distY * 0.2;
            btn.style.transform = `translate(${pullX}px, ${pullY}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = `translate(0px, 0px)`;
        });
    });

    // 2. Staggered Scroll Orchestration
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);

    staggerElements.forEach(el => observer.observe(el));
});
