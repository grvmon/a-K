/**
 * Acre&Key Ecosystem Storytelling Interactive Component
 * 60 FPS Lightweight Vanilla ES6 & Intersection Observer
 */

document.addEventListener('DOMContentLoaded', () => {
    const ecosystemSection = document.getElementById('ecosystem');
    if (!ecosystemSection) return;

    // Check accessibility reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const mainTitle = document.getElementById('storyTitle');
    const mainSub = document.getElementById('storySub');
    const centerNode = document.getElementById('storyCenterNode');
    const goldRing = document.getElementById('storyGoldRing');
    const centerLabel = document.getElementById('storyCenterLabel');
    const centerSub = document.getElementById('storyCenterSub');
    const benefitsRow = document.getElementById('storyBenefitsRow');
    const finalBanner = document.getElementById('storyFinalBanner');

    const cards = {
        builder: document.getElementById('cardBuilder'),
        seller: document.getElementById('cardSeller'),
        broker: document.getElementById('cardBroker'),
        bank: document.getElementById('cardBank'),
        lawyer: document.getElementById('cardLawyer')
    };

    const wires = {
        builder: document.getElementById('wireBuilder'),
        seller: document.getElementById('wireSeller'),
        broker: document.getElementById('wireBroker'),
        bank: document.getElementById('wireBank'),
        lawyer: document.getElementById('wireLawyer')
    };

    let animationTriggered = false;

    if (prefersReducedMotion) {
        // Render Final State Immediately for Reduced Motion
        renderFinalState();
        return;
    }

    // Intersection Observer to trigger animation once
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationTriggered) {
                animationTriggered = true;
                observer.unobserve(entry.target);
                startStorySequence();
            }
        });
    }, { threshold: 0.25 });

    observer.observe(ecosystemSection);

    function startStorySequence() {
        // Scene 1 (0-1s): Show BUYER node in center
        setTimeout(() => {
            centerNode.classList.add('visible');
        }, 100);

        // Scene 2 (1-3s): Animate stakeholder cards one by one (300ms each, 150ms delay)
        // Order: Builder, Seller, Broker, Bank, Lawyer
        const order = ['builder', 'seller', 'broker', 'bank', 'lawyer'];
        order.forEach((key, index) => {
            setTimeout(() => {
                if (cards[key]) cards[key].classList.add('visible');
            }, 1000 + (index * 400));
        });

        // Scene 3 (3-6s): Highlight each stakeholder individually with caption
        setTimeout(() => {
            highlightStakeholdersSequentially(order);
        }, 3200);

        // Scene 4 (6-8s): Draw animated connector lines, pulse buyer, show headline
        setTimeout(() => {
            order.forEach(key => {
                if (wires[key]) wires[key].classList.add('active');
            });
            centerNode.classList.add('pulse');
            
            if (mainTitle) {
                mainTitle.innerHTML = 'Everyone has advice.';
            }
            setTimeout(() => {
                if (mainSub) {
                    mainSub.innerHTML = 'No one represents the buyer.';
                }
            }, 1000);
        }, 6200);

        // Scene 5 (8-10s): Fade stakeholder cards to 35% opacity
        setTimeout(() => {
            order.forEach(key => {
                if (cards[key]) cards[key].classList.add('faded');
            });
        }, 8200);

        // Scene 6 (10-13s): Expand gold ring, display Acre&Key logo beside buyer, reconnect
        setTimeout(() => {
            goldRing.classList.add('active');
            if (centerLabel) centerLabel.textContent = 'ACRE & KEY';
            if (centerSub) centerSub.textContent = 'PROTECTS THE BUYER';

            order.forEach(key => {
                if (wires[key]) wires[key].classList.add('gold');
            });

            if (mainTitle) mainTitle.innerHTML = 'Everyone in the transaction has a goal.';
            if (mainSub) mainSub.innerHTML = 'Except for the buyer.';
        }, 10200);

        // Scene 7 (13-16s): Show Benefit Chips
        setTimeout(() => {
            order.forEach(key => {
                if (cards[key]) cards[key].classList.remove('faded');
            });
            if (benefitsRow) benefitsRow.classList.add('visible');
        }, 13200);

        // Scene 8 (16s+ Final State)
        setTimeout(() => {
            if (finalBanner) finalBanner.classList.add('visible');
        }, 15200);
    }

    function highlightStakeholdersSequentially(order) {
        let step = 0;
        const interval = setInterval(() => {
            if (step >= order.length) {
                clearInterval(interval);
                // Reset glows
                order.forEach(k => {
                    if (cards[k]) {
                        cards[k].classList.remove('glowing');
                        cards[k].classList.remove('faded');
                    }
                });
                return;
            }

            const currentKey = order[step];
            order.forEach(k => {
                if (cards[k]) {
                    if (k === currentKey) {
                        cards[k].classList.add('glowing');
                        cards[k].classList.remove('faded');
                    } else {
                        cards[k].classList.remove('glowing');
                        cards[k].classList.add('faded');
                    }
                }
            });

            step++;
        }, 600);
    }

    function renderFinalState() {
        if (centerNode) centerNode.classList.add('visible');
        if (goldRing) goldRing.classList.add('active');
        if (centerLabel) centerLabel.textContent = 'ACRE & KEY';
        if (centerSub) centerSub.textContent = 'PROTECTS THE BUYER';
        if (benefitsRow) benefitsRow.classList.add('visible');
        if (finalBanner) finalBanner.classList.add('visible');

        Object.keys(cards).forEach(key => {
            if (cards[key]) cards[key].classList.add('visible');
            if (wires[key]) {
                wires[key].classList.add('active');
                wires[key].classList.add('gold');
            }
        });
    }
});
