css_addition = """
/* Desktop default for hero-promise-card */
.hero-promise-card {
    display: none;
}

@media (max-width: 768px) {
    .hero-content {
        display: flex;
        flex-direction: column;
    }
    .hero-content .hero-kicker { order: 1; margin-bottom: 0.5rem; }
    .hero-content .hero-title { order: 2; margin-bottom: 1rem; }
    .hero-content .hero-subtitle { order: 3; margin-bottom: 1.5rem; }
    .hero-content .hero-cta-group { 
        order: 4; 
        margin-bottom: 2.5rem; 
        width: 100%; 
        justify-content: flex-start; 
    }
    
    .hero-content .hero-trust-bar { 
        order: 5; 
        flex-direction: row; 
        flex-wrap: nowrap;
        width: 100%;
        justify-content: space-between;
        border-top: 1px solid var(--divider);
        padding-top: 1.25rem;
        margin-bottom: 0;
        gap: 0;
        align-items: center;
    }
    
    .hero-title .highlight-brass {
        display: block;
        font-family: var(--font-heading);
        font-style: italic;
        font-weight: 400;
        margin-top: 0.35rem;
    }

    .hero-trust-bar .trust-item {
        flex: 1;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .hero-trust-bar .trust-number {
        font-size: 1rem;
    }
    .hero-trust-bar .trust-label {
        font-size: 0.55rem;
        text-align: center;
        margin-top: 4px;
        line-height: 1.2;
    }
    .hero-trust-bar .trust-divider {
        display: block !important;
        height: 30px;
        background: var(--divider);
        width: 1px;
        align-self: center;
    }

    /* Promise Card Styling */
    .hero-promise-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--warm-ivory);
        border: 1px solid rgba(184, 142, 82, 0.2);
        border-radius: 8px;
        padding: 1.25rem 1.5rem;
        margin-top: 1.5rem; 
        position: relative;
        z-index: 10;
        box-shadow: 0 4px 12px rgba(31, 43, 56, 0.05);
    }
    .promise-kicker {
        font-size: 0.65rem;
        font-weight: 700;
        color: var(--refined-brass);
        letter-spacing: 0.1em;
        margin-bottom: 0.35rem;
    }
    .promise-text {
        font-family: var(--font-heading);
        font-size: 1.2rem;
        color: var(--deep-navy);
        line-height: 1.3;
        font-weight: 400;
    }
    .promise-icon {
        color: var(--refined-brass);
    }
    .promise-icon svg {
        width: 32px;
        height: 32px;
        stroke-width: 1.5;
    }
}
"""

with open("/Users/gauravmongia/.gemini/antigravity/scratch/a-K/website.css", "a") as f:
    f.write(css_addition)
    
print("CSS appended successfully.")
