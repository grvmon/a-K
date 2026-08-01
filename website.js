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

    // 5. Walkthrough Step Highlight Sequence & Synced Laptop Image Crossfade for "The Process" section
    const processCards = document.querySelectorAll('.market-lens-card');
    const processSection = document.getElementById('bengaluru-market-lens');
    const processImg = document.getElementById('process-visual-img');

    // Preload & map 5 distinct contextual dashboard images for each decision step
    const stepImages = {
        0: 'style-guide/assets/acrekey_construction_vs_ready.jpg',        // Step 1: Construction Timeline vs Ready-to-Move
        1: 'style-guide/assets/acrekey_property_comparison_dashboard.jpg',// Step 2: Builder A vs Builder B Evaluation
        2: 'style-guide/assets/acrekey_corridor_growth_map.jpg',          // Step 3: Bangalore Micro-Market & Corridor Growth Map
        3: 'style-guide/assets/acrekey_floor_view_comparison.jpg',        // Step 4: Floor & View Premium Evaluation
        4: 'style-guide/assets/acrekey_investment_analysis.jpg'          // Step 5: Investment & ROI Yield Analysis
    };

    function updateStepVisual(stepIndex) {
        if (!processImg) return;
        const targetSrc = stepImages[stepIndex] || stepImages[0];
        
        // If image source changes, perform a subtle crossfade transition
        if (processImg.getAttribute('src') !== targetSrc) {
            processImg.classList.add('fade-out');
            setTimeout(function () {
                processImg.setAttribute('src', targetSrc);
                processImg.classList.remove('fade-out');
            }, 180);
        }
    }

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

                // Crossfade laptop dashboard image synchronized with active card
                updateStepVisual(step);

                step++;
                if (step < processCards.length) {
                    setTimeout(highlightNextCard, 2000); // 2 seconds per card transition
                }
            }

            highlightNextCard();
        }

        // Allow user hover to highlight card and update synced laptop screen
        processCards.forEach(function (card, idx) {
            card.addEventListener('mouseenter', function () {
                processCards.forEach(c => c.classList.remove('active-step'));
                card.classList.add('active-step');
                updateStepVisual(idx);
            });
        });

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
