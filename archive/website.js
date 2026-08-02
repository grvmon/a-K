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

    // 3. Luxury Mobile Navigation Drawer & Interactions
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

    // Close mobile drawer on ESC key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('is-active')) {
            closeMobileDrawer();
        }
    });

    // Close mobile drawer when any link inside drawer is clicked
    if (mobileDrawer) {
        const drawerLinks = mobileDrawer.querySelectorAll('a');
        drawerLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                closeMobileDrawer();
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
    const processSection = document.getElementById('buyers-checklist');
    const processImg = document.getElementById('process-visual-img');

    // Preload & map 5 distinctly framed contextual dashboard images for each decision step
    const stepImages = {
        0: 'style-guide/assets/acrekey_construction_vs_ready.webp?v=2',        // Step 1: Wide kitchen & dining perspective
        1: 'style-guide/assets/acrekey_property_comparison_dashboard.webp?v=2',// Step 2: Mid-angle side consultation perspective
        2: 'style-guide/assets/acrekey_corridor_growth_map.webp?v=2',          // Step 3: Centered corridor map perspective
        3: 'style-guide/assets/acrekey_floor_view_comparison.webp?v=2',        // Step 4: Wide balcony window perspective
        4: 'style-guide/assets/acrekey_investment_analysis.webp?v=2'          // Step 5: Intimate close-up table perspective
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

    // 7. Who Are We — Scroll Reveal Animations
    const wawRevealEls = document.querySelectorAll('.waw-reveal');
    if (wawRevealEls.length > 0) {
        var wawDelay = 0;
        const wawObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    // Stagger each element's reveal by 80ms
                    var el = entry.target;
                    var d = wawDelay;
                    wawDelay += 80;
                    setTimeout(function () {
                        el.classList.add('is-visible');
                    }, d);
                    wawObserver.unobserve(el);
                }
            });
        }, { threshold: 0.15 });

        wawRevealEls.forEach(function (el) {
            wawObserver.observe(el);
        });
    }

    // 8. Mobile Swipe Carousel for Decision Framework Cards
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
            }, 6500); // 6.5 seconds auto-scroll
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
            }, 8500); // Resume auto-scroll after 8.5s inactivity
        }

        // Touch & Mouse Event Listeners for Instant Pause & Delayed Resume
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

        // Detect Scroll Position for Live Dot Indicators
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

        // Dot Click Listeners
        dots.forEach((dot, idx) => {
            dot.addEventListener('click', () => {
                handleUserInteractionStart();
                scrollToCard(idx);
                handleUserInteractionEnd();
            });
        });

        // Initialize Carousel Auto-Scroll on Load
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

    // 9. Mobile Swipe Carousel for Customer Speak / Testimonial Cards
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
            }, 6500); // 6.5s auto scroll
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
            }, 8500); // Resume auto-scroll after 8.5s inactivity
        }

        // Event listeners
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

        // Scroll listener for live dot indicators
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

        // Dot Click Listeners
        testimonialDots.forEach((dot, idx) => {
            dot.addEventListener('click', () => {
                handleTUserStart();
                scrollToTestimonial(idx);
                handleTUserEnd();
            });
        });

        // Initialize Carousel Auto-Scroll on Load
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

    // Premium Scroll Reveal Observer
    const premiumRevealElements = document.querySelectorAll('.premium-reveal');
    const premiumObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const el = entry.target;
            if (entry.isIntersecting) {
                // If the element specifies staggering for its children via data attributes
                if (el.dataset.staggerChildren) {
                    const children = el.querySelectorAll(el.dataset.staggerChildren);
                    children.forEach((child, index) => {
                        child.style.transitionDelay = `${index * 70}ms`;
                        child.classList.add('revealed');
                    });
                }
                el.classList.add('revealed');
            } else {
                // Reset states when scrolled out of fold to ensure they are visible only on fold
                el.classList.remove('revealed');
                if (el.dataset.staggerChildren) {
                    const children = el.querySelectorAll(el.dataset.staggerChildren);
                    children.forEach(child => {
                        child.classList.remove('revealed');
                        child.style.transitionDelay = '';
                    });
                }
            }
        });
    }, {
        root: null,
        threshold: 0.02,
        rootMargin: '-5% 0px -5% 0px' // Keep active precisely within the viewport fold
    });
    
    premiumRevealElements.forEach(el => {
        premiumObserver.observe(el);
    });
});

