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

    // Preload & map 5 distinctly framed contextual dashboard images for each decision step
    const stepImages = {
        0: 'style-guide/assets/acrekey_construction_vs_ready.jpg?v=2',        // Step 1: Wide kitchen & dining perspective
        1: 'style-guide/assets/acrekey_property_comparison_dashboard.jpg?v=2',// Step 2: Mid-angle side consultation perspective
        2: 'style-guide/assets/acrekey_corridor_growth_map.jpg?v=2',          // Step 3: Centered corridor map perspective
        3: 'style-guide/assets/acrekey_floor_view_comparison.jpg?v=2',        // Step 4: Wide balcony window perspective
        4: 'style-guide/assets/acrekey_investment_analysis.jpg?v=2'          // Step 5: Intimate close-up table perspective
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
            // Crossfade laptop dashboard image synchronized with active card
            updateStepVisual(index);
        }

        function advanceStep() {
            if (isUserHovering) return;
            highlightStep(currentStep);
            currentStep = (currentStep + 1) % processCards.length; // Modulo 5 continuous loop
        }

        function startLoop() {
            if (!stepTimer) {
                advanceStep();
                stepTimer = setInterval(advanceStep, 2200); // 2.2 seconds per step continuous loop
            }
        }

        function stopLoop() {
            if (stepTimer) {
                clearInterval(stepTimer);
                stepTimer = null;
            }
        }

        // Add interactive hover & click listeners
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

        // Trigger continuous loop when section scrolls into view
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

    // 6. Framework Cards Highlight Sequence for "69 Due Diligence Checks" section
    const frameworkCards = document.querySelectorAll('.framework-card');
    const frameworkSection = document.getElementById('services');

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
                frameworkTimer = setInterval(advanceFrameworkStep, 2200); // 2.2 seconds per step continuous loop
            }
        }

        function stopFrameworkLoop() {
            if (frameworkTimer) {
                clearInterval(frameworkTimer);
                frameworkTimer = null;
            }
        }

        // Add interactive hover & click listeners
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

        // Trigger continuous loop when section scrolls into view
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
});
