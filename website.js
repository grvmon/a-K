document.addEventListener('DOMContentLoaded', function () {
    // 1. Initialize Feather Icons
    if (typeof feather !== 'undefined') {
        feather.replace();
    }

    // 2. Header Scroll Effect
    const headerNav = document.getElementById('header-nav');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 30) {
            headerNav.classList.add('scrolled');
        } else {
            headerNav.classList.remove('scrolled');
        }
    });

    // 3. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-toggle-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');

    if (mobileBtn && mobileDrawer) {
        mobileBtn.addEventListener('click', function () {
            mobileDrawer.classList.toggle('active');
        });

        // Close mobile menu on link click
        const drawerLinks = mobileDrawer.querySelectorAll('a');
        drawerLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                mobileDrawer.classList.remove('active');
            });
        });
    }

    // 4. Scroll Triggered Animation for Buyer Ecosystem Hub Diagram
    const hubGridMatrix = document.querySelector('.hub-grid-matrix');
    if (hubGridMatrix) {
        const observerOptions = {
            root: null,
            threshold: 0.2
        };

        const observer = new IntersectionObserver(function (entries, observerInstance) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observerInstance.unobserve(entry.target);
                }
            });
        }, observerOptions);

        observer.observe(hubGridMatrix);
    }

    // 5. Sequential Step Auto-Loop Animation for "The Process" section cards (01 -> 02 -> 03 -> 04 -> 05)
    const stepCards = document.querySelectorAll('.market-lens-card');
    if (stepCards.length > 0) {
        let currentStep = 0;
        let stepTimer = null;
        let isUserHovering = false;

        function highlightStep(index) {
            stepCards.forEach(function (card, i) {
                if (i === index) {
                    card.classList.add('active-step');
                } else {
                    card.classList.remove('active-step');
                }
            });
        }

        function advanceStep() {
            if (isUserHovering) return;
            highlightStep(currentStep);
            currentStep = (currentStep + 1) % stepCards.length;
        }

        function startLoop() {
            if (!stepTimer) {
                advanceStep();
                stepTimer = setInterval(advanceStep, 2400); // Smooth 2.4s per step transition
            }
        }

        function stopLoop() {
            if (stepTimer) {
                clearInterval(stepTimer);
                stepTimer = null;
            }
        }

        // Add interactive hover & click listeners
        stepCards.forEach(function (card, idx) {
            card.addEventListener('mouseenter', function () {
                isUserHovering = true;
                stopLoop();
                highlightStep(idx);
            });

            card.addEventListener('mouseleave', function () {
                isUserHovering = false;
                currentStep = (idx + 1) % stepCards.length;
                startLoop();
            });

            card.addEventListener('click', function () {
                highlightStep(idx);
            });
        });

        // Trigger auto-loop when section scrolls into view
        const processSection = document.getElementById('bengaluru-market-lens');
        if (processSection) {
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
        } else {
            startLoop();
        }
    }
});
