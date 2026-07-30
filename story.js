/**
 * Acre&Key Ecosystem Storytelling Component
 * 60 FPS Smooth Seamless Looping Sequence matching Storyboard Scenes 1-8
 */

document.addEventListener('DOMContentLoaded', () => {
    const ecosystemSection = document.getElementById('ecosystem');
    if (!ecosystemSection) return;

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Elements
    const storyTitle = document.getElementById('storyTitle');
    const storySub = document.getElementById('storySub');
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

    let isRunning = false;

    if (prefersReducedMotion) {
        renderFinalState();
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !isRunning) {
                isRunning = true;
                runLoopingStory();
            }
        });
    }, { threshold: 0.25 });

    observer.observe(ecosystemSection);

    function resetAllState() {
        if (storyTitle) storyTitle.textContent = 'Everyone in the transaction has a goal.';
        if (storySub) storySub.textContent = 'Except for the buyer.';
        if (centerLabel) centerLabel.textContent = 'BUYER';
        if (centerSub) centerSub.textContent = 'No Advisory';

        if (centerNode) {
            centerNode.classList.remove('visible', 'pulse', 'shake', 'fast-pulse');
        }
        if (goldRing) goldRing.classList.remove('active');
        if (benefitsRow) benefitsRow.classList.remove('visible');
        if (finalBanner) finalBanner.classList.remove('visible');

        Object.keys(cards).forEach(key => {
            if (cards[key]) {
                cards[key].classList.remove('visible', 'glowing', 'faded', 'stacked');
            }
        });
        Object.keys(wires).forEach(key => {
            if (wires[key]) {
                wires[key].classList.remove('active', 'gold');
            }
        });
    }

    function runLoopingStory() {
        resetAllState();

        // Scene 1 (0 - 1.5s): Fade in BUYER circle scale 90% -> 100%, soft gold pulse
        setTimeout(() => {
            if (centerNode) centerNode.classList.add('visible', 'pulse');
            if (storySub) storySub.textContent = 'The buyer starts the journey.';
        }, 100);

        // Scene 2 (1.5 - 4s): Stakeholders enter individually (Builder top, Seller left, Broker right, Lawyer bottom-left, Bank bottom-right)
        const order = ['builder', 'seller', 'broker', 'lawyer', 'bank'];
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'Advice comes from all sides';
            if (storySub) storySub.textContent = 'Different stakeholders enter the picture.';

            order.forEach((key, index) => {
                setTimeout(() => {
                    if (cards[key]) cards[key].classList.add('visible');
                    if (wires[key]) wires[key].classList.add('active');
                }, index * 250);
            });
        }, 1500);

        // Scene 3 (4 - 9s): One stakeholder highlighted at a time with caption
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'Everyone has their own agenda';
            if (storySub) storySub.textContent = 'Each has a different priority.';

            order.forEach((key, index) => {
                setTimeout(() => {
                    order.forEach(k => {
                        if (cards[k]) {
                            if (k === key) {
                                cards[k].classList.add('glowing');
                                cards[k].classList.remove('faded');
                            } else {
                                cards[k].classList.remove('glowing');
                                cards[k].classList.add('faded');
                            }
                        }
                    });
                }, index * 800);
            });
        }, 4000);

        // Scene 4 (9 - 12s): All stakeholders active, connector lines pulse, buyer shakes, title "Too many voices. Too much pressure."
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'Conflicting advice creates confusion';
            if (storySub) storySub.textContent = 'Too many voices. Too much pressure.';

            order.forEach(k => {
                if (cards[k]) {
                    cards[k].classList.remove('faded');
                    cards[k].classList.add('glowing');
                }
            });

            if (centerNode) centerNode.classList.add('shake', 'fast-pulse');
        }, 9000);

        // Scene 5 (12 - 14s): The noise fades, stakeholder cards reduce to 25% opacity
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'The noise fades';
            if (storySub) storySub.textContent = 'The buyer is left uncertain.';

            if (centerNode) centerNode.classList.remove('shake', 'fast-pulse');

            order.forEach(k => {
                if (cards[k]) {
                    cards[k].classList.remove('glowing');
                    cards[k].classList.add('faded');
                }
            });
        }, 12000);

        // Scene 6 (14 - 18s): Acre&Key steps in. Gold glow expands, Acre&Key logo slides in, wires re-route
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'Acre&Key steps in';
            if (storySub) storySub.textContent = 'Acre&Key connects, coordinates and represents the buyer.';

            if (goldRing) goldRing.classList.add('active');
            if (centerLabel) centerLabel.textContent = 'ACRE & KEY';
            if (centerSub) centerSub.textContent = 'PROTECTS THE BUYER';

            order.forEach(k => {
                if (wires[k]) wires[key => k].classList.add('gold');
                if (cards[k]) cards[k].classList.remove('faded');
            });
        }, 14000);

        // Scene 7 (18 - 22s): Advice is filtered. Stakeholders align, Benefit chips slide in
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'Advice is filtered. You get clarity.';
            if (storySub) storySub.textContent = 'We simplify complexity and align every angle to your best interest.';

            if (benefitsRow) benefitsRow.classList.add('visible');
        }, 18000);

        // Scene 8 (22 - 26s): Final State Banner "One trusted partner. Confident decisions."
        setTimeout(() => {
            if (storyTitle) storyTitle.textContent = 'One trusted partner. Confident decisions.';
            if (storySub) storySub.textContent = 'That’s the Acre&Key advantage.';

            if (finalBanner) finalBanner.classList.add('visible');
        }, 22000);

        // Seamless loop hold 3s and restart sequence
        setTimeout(() => {
            runLoopingStory();
        }, 26000);
    }

    function renderFinalState() {
        if (storyTitle) storyTitle.textContent = 'One trusted partner. Confident decisions.';
        if (storySub) storySub.textContent = 'That’s the Acre&Key advantage.';
        if (centerNode) centerNode.classList.add('visible', 'pulse');
        if (goldRing) goldRing.classList.add('active');
        if (centerLabel) centerLabel.textContent = 'ACRE & KEY';
        if (centerSub) centerSub.textContent = 'PROTECTS THE BUYER';
        if (benefitsRow) benefitsRow.classList.add('visible');
        if (finalBanner) finalBanner.classList.add('visible');

        Object.keys(cards).forEach(key => {
            if (cards[key]) cards[key].classList.add('visible');
            if (wires[key]) wires[key].classList.add('active', 'gold');
        });
    }

    /* ================= SECTION 2 PRECISE 9-STEP CHRONOLOGICAL SEQUENCE ================= */
    const seqSection = document.querySelector('.seq-flow-section');
    if (!seqSection) return;

    const leftCol = document.querySelector('.seq-left-col');
    const leftItems = document.querySelectorAll('.seq-left-item');
    const incomingBeams = document.querySelectorAll('.seq-incoming-beam');
    const incomingParticles = document.querySelectorAll('.seq-incoming-particle');
    const portalNodes = document.querySelectorAll('.seq-portal-node');
    const centerCol = document.querySelector('.seq-center-col');
    const centerHero = document.querySelector('.seq-center-hero');
    const centerMeta = document.querySelectorAll('.seq-center-meta');
    const outgoingBeams = document.querySelectorAll('.seq-outgoing-beam');
    const outgoingParticles = document.querySelectorAll('.seq-outgoing-particle');
    const rightCol = document.querySelector('.seq-right-col');
    const rightItems = document.querySelectorAll('.seq-right-item');
    const payoffMain = document.querySelector('.seq-payoff-main');
    const payoffClosing = document.querySelector('.seq-payoff-closing');

    let seqTriggered = false;

    const seqObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !seqTriggered) {
                seqTriggered = true;
                playSection2Sequence();
            }
        });
    }, { threshold: 0.2 });

    seqObserver.observe(seqSection);

    function playSection2Sequence() {
        // Step 1: Left column appears (0ms)
        if (leftCol) leftCol.classList.add('seq-active');

        // Step 2: Each stakeholder lights up one by one (300ms -> 1100ms)
        leftItems.forEach((item, index) => {
            setTimeout(() => {
                item.classList.add('seq-active');
            }, 300 + index * 200);
        });

        // Step 3: Gold pulse travels toward the center (1400ms)
        setTimeout(() => {
            incomingBeams.forEach(el => el.classList.add('seq-active'));
            incomingParticles.forEach(el => el.classList.add('seq-active'));
        }, 1400);

        // Step 4: Protection layer activates (1900ms)
        setTimeout(() => {
            if (centerCol) centerCol.classList.add('seq-active');
            portalNodes.forEach(el => el.classList.add('seq-active'));
        }, 1900);

        // Step 5: "Only your interests." fades in (2300ms)
        setTimeout(() => {
            if (centerHero) centerHero.classList.add('seq-active');
            centerMeta.forEach(el => el.classList.add('seq-active'));
        }, 2300);

        // Step 6: Outgoing gold pulse travels to the right (2700ms)
        setTimeout(() => {
            outgoingBeams.forEach(el => el.classList.add('seq-active'));
            outgoingParticles.forEach(el => el.classList.add('seq-active'));
        }, 2700);

        // Step 7: Buyer outcomes appear one after another (3100ms -> 3900ms)
        setTimeout(() => {
            if (rightCol) rightCol.classList.add('seq-active');
            rightItems.forEach((item, index) => {
                setTimeout(() => {
                    item.classList.add('seq-active');
                }, index * 200);
            });
        }, 3100);

        // Step 8: Bottom statement fades in (4200ms)
        setTimeout(() => {
            if (payoffMain) payoffMain.classList.add('seq-active');
        }, 4200);

        // Step 9: "We are." appears after a 300ms delay (4500ms)
        setTimeout(() => {
            if (payoffClosing) payoffClosing.classList.add('seq-active');
        }, 4500);
    }
});
