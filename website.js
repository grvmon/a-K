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

    // 5. Walkthrough Step Highlight Sequence for "The Process" section (Card 1 -> 2 -> 3 -> 4 -> 5 -> STOPS)
    const processCards = document.querySelectorAll('.market-lens-card');
    const processSection = document.getElementById('bengaluru-market-lens');

    if (processCards.length > 0 && processSection) {
        let hasAnimated = false;

        function runWalkthroughSequence() {
            if (hasAnimated) return;
            hasAnimated = true;

            let step = 0;
            
            function highlightNextCard() {
                processCards.forEach(function (card, i) {
                    if (i === step) {
                        card.classList.add('active-step');
                    } else {
                        card.classList.remove('active-step');
                    }
                });

                step++;
                if (step < processCards.length) {
                    setTimeout(highlightNextCard, 2000); // 2 seconds per card transition
                }
            }

            highlightNextCard();
        }

        // Trigger 1-time walkthrough when section scrolls into view
        const processObserver = new IntersectionObserver(function (entries, observerInstance) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    runWalkthroughSequence();
                    observerInstance.unobserve(entry.target);
                }
            });
        }, { threshold: 0.25 });

        processObserver.observe(processSection);
    }
});
