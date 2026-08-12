import os
import re

file_path = "/Users/patidar/Desktop/AnK website/home-loan-emi-calculator/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace everything between <style> and </style>
# And everything between <main class="ak-calc-section"> and </main>
# And everything between <script> and </script> (the EMI engine script)

css_new = """
    /* --- NEW CALCULATOR CSS --- */
    body {
        background-color: #F8F9FA;
    }
    
    .ak-calc-wrapper {
        max-width: 1200px;
        margin: 140px auto 4rem auto;
        padding: 0 1.5rem;
        font-family: 'Manrope', sans-serif;
    }

    /* Header Row */
    .ak-calc-header-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        gap: 1.5rem;
    }

    .ak-calc-header-left .ak-calc-h1 {
        font-family: 'Marcellus', serif;
        font-size: clamp(28px, 4vw, 42px);
        color: var(--ak-navy);
        margin: 0 0 0.5rem 0;
        font-weight: 400;
        letter-spacing: -0.02em;
    }

    .ak-calc-sub-text {
        font-size: 1.1rem;
        color: var(--ak-slate);
        margin: 0 0 0.25rem 0;
    }

    .ak-calc-kicker {
        font-size: 1.05rem;
        color: var(--ak-gold);
        font-weight: 600;
        margin: 0;
    }

    .ak-trust-badge-header {
        display: flex;
        align-items: center;
        background: #FDF9F3;
        border: 1px solid rgba(140, 103, 52, 0.2);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        gap: 1rem;
    }

    .ak-trust-badge-icon svg {
        width: 32px;
        height: 32px;
        stroke: var(--ak-gold);
        fill: rgba(140, 103, 52, 0.1);
    }

    .ak-trust-badge-title {
        font-weight: 800;
        color: var(--ak-navy);
        font-size: 0.95rem;
        margin-bottom: 0.2rem;
    }

    .ak-trust-badge-sub {
        font-size: 0.85rem;
        color: var(--ak-slate-light);
    }

    /* Main Grid */
    .ak-calc-main-grid {
        display: grid;
        grid-template-columns: 400px 1fr;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    @media (max-width: 950px) {
        .ak-calc-main-grid {
            grid-template-columns: 1fr;
        }
    }

    /* Left Panel (White) */
    .ak-calc-left-panel {
        background: #FFFFFF;
        border: 1px solid #EAEFF5;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.02);
    }

    .ak-panel-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 2rem;
    }

    .ak-panel-header h2 {
        font-size: 1.15rem;
        font-weight: 800;
        color: var(--ak-navy);
        margin: 0;
    }

    .ak-panel-header svg {
        width: 20px;
        height: 20px;
        stroke: var(--ak-gold);
    }

    /* Input Rows */
    .ak-new-input-row {
        margin-bottom: 1.8rem;
    }

    .ak-new-input-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .ak-new-input-label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--ak-navy);
    }

    .ak-new-input-label svg {
        width: 16px;
        height: 16px;
        stroke: var(--ak-slate-light);
        cursor: help;
    }

    .ak-new-input-box-wrapper {
        position: relative;
        width: 140px;
    }

    .ak-new-input-box-wrapper .prefix {
        position: absolute;
        left: 12px;
        top: 50%;
        transform: translateY(-50%);
        font-weight: 600;
        color: var(--ak-navy);
    }

    .ak-new-input-box-wrapper .suffix {
        position: absolute;
        right: 12px;
        top: 50%;
        transform: translateY(-50%);
        font-weight: 600;
        color: var(--ak-navy);
    }

    .ak-new-input {
        width: 100%;
        border: 1px solid #EAEFF5;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-family: 'Manrope', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--ak-navy);
        box-sizing: border-box;
        text-align: right;
    }

    .ak-new-input.has-prefix { padding-left: 28px; }
    .ak-new-input.has-suffix { padding-right: 28px; }
    
    .ak-new-input:focus {
        outline: none;
        border-color: var(--ak-gold);
        box-shadow: 0 0 0 3px rgba(140, 103, 52, 0.1);
    }

    .ak-new-input.readonly {
        background: #F8F9FA;
        border-color: transparent;
    }

    /* Slider styling */
    .ak-new-slider-container {
        position: relative;
        padding: 0 8px;
    }

    .ak-new-slider {
        -webkit-appearance: none;
        appearance: none;
        width: 100%;
        height: 4px;
        border-radius: 2px;
        background: #EAEFF5;
        outline: none;
        cursor: pointer;
        display: block;
    }

    .ak-new-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: var(--ak-gold);
        border: 3px solid #FFF;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        cursor: pointer;
    }

    .ak-new-slider-fill {
        position: absolute;
        top: 0;
        left: 8px;
        height: 4px;
        background: var(--ak-gold);
        border-radius: 2px;
        pointer-events: none;
        z-index: 1;
    }

    .ak-slider-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.75rem;
        color: var(--ak-slate-light);
        margin-top: 0.5rem;
        font-weight: 600;
    }

    .ak-calc-emi-btn {
        width: 100%;
        background: #182A3D;
        color: #FFF;
        border: none;
        border-radius: 8px;
        padding: 1rem;
        font-family: 'Manrope', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        margin-top: 1rem;
        transition: background 0.2s;
    }

    .ak-calc-emi-btn:hover {
        background: #0F1F3D;
    }

    .ak-secure-text {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.4rem;
        font-size: 0.8rem;
        color: var(--ak-slate-light);
        margin-top: 1rem;
    }

    /* Right Panel (Dark) */
    .ak-calc-right-panel {
        background: #1E232B;
        border-radius: 16px;
        padding: 2.5rem;
        color: #FFF;
        display: flex;
        flex-direction: column;
    }

    .ak-right-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: rgba(255,255,255,0.9);
        margin-bottom: 0.5rem;
    }

    .ak-emi-highlight-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 2.5rem;
    }

    .ak-emi-huge {
        font-family: 'Marcellus', serif;
        font-size: 3.5rem;
        color: var(--ak-gold);
        line-height: 1;
    }

    .ak-emi-month {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.7);
    }

    .ak-affordable-badge {
        background: rgba(39, 174, 96, 0.15);
        color: #2ECC71;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
    }

    /* Middle Section Right Panel (Stats + Donut) */
    .ak-right-middle-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    @media (max-width: 600px) {
        .ak-right-middle-grid {
            grid-template-columns: 1fr;
        }
    }

    .ak-3-stats {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 1.5rem;
    }

    .ak-stat-item {
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
    }

    .ak-stat-label {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.6);
        font-weight: 600;
    }

    .ak-stat-val {
        font-size: 1.2rem;
        font-weight: 800;
        color: #FFF;
    }

    .ak-donut-container {
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .ak-donut-wrapper-new {
        position: relative;
        width: 140px;
        height: 140px;
    }

    .ak-donut-svg {
        width: 100%;
        height: 100%;
        transform: rotate(-90deg);
    }

    .ak-donut-center {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .ak-donut-center-val {
        font-size: 1.5rem;
        font-weight: 800;
        color: #FFF;
        line-height: 1;
    }

    .ak-donut-center-label {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.6);
    }

    .ak-legend-new {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }

    .ak-legend-item-new {
        display: flex;
        flex-direction: column;
        gap: 0.2rem;
    }

    .ak-legend-label-row {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.7);
    }

    .ak-legend-dot-new {
        width: 12px;
        height: 12px;
        border-radius: 2px;
    }

    .ak-legend-dot-new.principal { background: #D4AF37; }
    .ak-legend-dot-new.interest { background: #8B6508; }

    .ak-legend-val-new {
        font-size: 1rem;
        font-weight: 700;
        color: #FFF;
    }
    .ak-legend-pct {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.5);
    }

    /* Stacked Bar */
    .ak-stacked-bar-container {
        margin-top: auto;
    }

    .ak-stacked-bar-title {
        font-size: 0.9rem;
        color: #FFF;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .ak-stacked-bar {
        display: flex;
        height: 32px;
        border-radius: 6px;
        overflow: hidden;
    }

    .ak-bar-principal {
        background: #D4AF37;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
        color: rgba(0,0,0,0.7);
        transition: width 0.3s ease;
    }

    .ak-bar-interest {
        background: #8B6508;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
        color: rgba(255,255,255,0.9);
        transition: width 0.3s ease;
    }

    /* 4 Feature Cards Grid */
    .ak-feature-cards {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    @media (max-width: 1000px) {
        .ak-feature-cards { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
        .ak-feature-cards { grid-template-columns: 1fr; }
    }

    .ak-fcard {
        background: #FFF;
        border: 1px solid #EAEFF5;
        border-radius: 12px;
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        box-shadow: 0 4px 12px rgba(0,0,0,0.015);
    }

    .ak-fcard-icon {
        width: 40px;
        height: 40px;
        margin-bottom: 1rem;
    }
    
    .ak-fcard-icon svg {
        width: 100%; height: 100%;
    }
    .ak-fcard-icon.green svg { stroke: #2ECC71; }
    .ak-fcard-icon.purple svg { stroke: #9B59B6; }
    .ak-fcard-icon.blue svg { stroke: #3498DB; }
    .ak-fcard-icon.orange svg { stroke: #E67E22; }

    .ak-fcard-title {
        font-size: 1rem;
        font-weight: 800;
        color: var(--ak-navy);
        margin-bottom: 0.5rem;
    }

    .ak-fcard-desc {
        font-size: 0.85rem;
        color: var(--ak-slate-light);
        margin-bottom: 1.5rem;
        line-height: 1.5;
        flex-grow: 1;
    }

    .ak-fcard-link {
        font-size: 0.9rem;
        font-weight: 700;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }
    .ak-fcard-link.green { color: #2ECC71; }
    .ak-fcard-link.purple { color: #9B59B6; }
    .ak-fcard-link.blue { color: #3498DB; }
    .ak-fcard-link.orange { color: #E67E22; }

    /* True Cost Section */
    .ak-true-cost-strip {
        background: #FDF9F3;
        border: 1px solid rgba(140, 103, 52, 0.2);
        border-radius: 16px;
        padding: 2rem;
    }

    .ak-tc-header {
        margin-bottom: 1.5rem;
    }

    .ak-tc-title {
        font-family: 'Marcellus', serif;
        font-size: 1.6rem;
        color: var(--ak-navy);
        margin: 0 0 0.2rem 0;
    }
    .ak-tc-sub {
        font-size: 0.9rem;
        color: var(--ak-slate-light);
    }

    .ak-tc-math-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .ak-tc-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }

    .ak-tc-icon-box {
        width: 48px;
        height: 48px;
        background: #F7EAD7;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .ak-tc-icon-box svg {
        width: 24px;
        height: 24px;
        stroke: var(--ak-gold);
    }

    .ak-tc-text {
        display: flex;
        flex-direction: column;
        gap: 0.2rem;
    }
    .ak-tc-label {
        font-size: 0.8rem;
        color: var(--ak-slate-light);
        font-weight: 600;
    }
    .ak-tc-val {
        font-size: 1.1rem;
        font-weight: 800;
        color: var(--ak-navy);
    }

    .ak-tc-operator {
        font-size: 1.5rem;
        color: var(--ak-slate-light);
        font-weight: 400;
    }

    .ak-tc-result-box {
        background: #F7EAD7;
        border: 1px solid var(--ak-gold);
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        min-width: 200px;
    }
    
    .ak-tc-result-label {
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--ak-navy);
        margin-bottom: 0.4rem;
    }
    .ak-tc-result-val {
        font-size: 1.75rem;
        font-weight: 800;
        color: var(--ak-navy);
        margin-bottom: 0.2rem;
    }
    .ak-tc-result-sub {
        font-size: 0.75rem;
        color: var(--ak-slate-light);
    }
"""

html_new = """
    <main class="ak-calc-wrapper">
        <!-- Header -->
        <div class="ak-calc-header-row">
            <div class="ak-calc-header-left">
                <h1 class="ak-calc-h1">Home Loan EMI Calculator</h1>
                <p class="ak-calc-sub-text">Calculate your EMI, total interest and the true cost of your home.</p>
                <p class="ak-calc-kicker">Plan better. Borrow smarter. Buy with confidence.</p>
            </div>
            <div class="ak-calc-header-right">
                <div class="ak-trust-badge-header">
                    <div class="ak-trust-badge-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                    </div>
                    <div class="ak-trust-badge-text">
                        <div class="ak-trust-badge-title">100% Free &bull; No Sign Up Required</div>
                        <div class="ak-trust-badge-sub">Trusted by home buyers across Bangalore</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Grid -->
        <div class="ak-calc-main-grid">
            
            <!-- Left Panel -->
            <div class="ak-calc-left-panel">
                <div class="ak-panel-header">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <h2>Your Loan Details</h2>
                </div>

                <!-- Input: Property Price -->
                <div class="ak-new-input-row">
                    <div class="ak-new-input-top">
                        <div class="ak-new-input-label">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
                            Property Price
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        </div>
                        <div class="ak-new-input-box-wrapper">
                            <span class="prefix">₹</span>
                            <input type="text" id="propValueInputNew" class="ak-new-input has-prefix" value="1,00,00,000" onchange="onPropChangeInput(this.value)">
                        </div>
                    </div>
                    <div class="ak-new-slider-container">
                        <input type="range" id="propValueSliderNew" class="ak-new-slider" min="1000000" max="100000000" step="500000" value="10000000" oninput="onPropChangeSlider(this.value)">
                    </div>
                    <div class="ak-slider-labels">
                        <span>10L</span>
                        <span>10Cr</span>
                    </div>
                </div>

                <!-- Input: Down Payment -->
                <div class="ak-new-input-row">
                    <div class="ak-new-input-top">
                        <div class="ak-new-input-label">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                            Down Payment
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        </div>
                        <div class="ak-new-input-box-wrapper">
                            <span class="prefix">₹</span>
                            <input type="text" id="downPayInputNew" class="ak-new-input has-prefix" value="20,00,000" onchange="onDownChangeInput(this.value)">
                        </div>
                    </div>
                    <div class="ak-new-slider-container">
                        <input type="range" id="downPaySliderNew" class="ak-new-slider" min="0" max="50" step="1" value="20" oninput="onDownChangeSlider(this.value)">
                    </div>
                    <div class="ak-slider-labels">
                        <span>0%</span>
                        <span>50%</span>
                    </div>
                </div>

                <!-- Input: Loan Amount (Readonly) -->
                <div class="ak-new-input-row">
                    <div class="ak-new-input-top">
                        <div class="ak-new-input-label">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect><circle cx="12" cy="12" r="2"></circle><path d="M6 12h.01M18 12h.01"></path></svg>
                            Loan Amount
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        </div>
                        <div class="ak-new-input-box-wrapper">
                            <span class="prefix">₹</span>
                            <input type="text" id="loanAmountInputNew" class="ak-new-input has-prefix readonly" value="80,00,000" readonly>
                        </div>
                    </div>
                </div>

                <!-- Input: Interest Rate -->
                <div class="ak-new-input-row">
                    <div class="ak-new-input-top">
                        <div class="ak-new-input-label">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                            Interest Rate (p.a.)
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        </div>
                        <div class="ak-new-input-box-wrapper">
                            <input type="text" id="interestInputNew" class="ak-new-input has-suffix" value="8.50" onchange="onInterestChangeInput(this.value)">
                            <span class="suffix">%</span>
                        </div>
                    </div>
                    <div class="ak-new-slider-container">
                        <input type="range" id="interestSliderNew" class="ak-new-slider" min="6.0" max="12.0" step="0.1" value="8.5" oninput="onInterestChangeSlider(this.value)">
                    </div>
                    <div class="ak-slider-labels">
                        <span>6%</span>
                        <span>12%</span>
                    </div>
                </div>

                <!-- Input: Loan Tenure -->
                <div class="ak-new-input-row" style="margin-bottom: 1rem;">
                    <div class="ak-new-input-top">
                        <div class="ak-new-input-label">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                            Loan Tenure
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                        </div>
                        <div class="ak-new-input-box-wrapper">
                            <input type="text" id="tenureInputNew" class="ak-new-input has-suffix readonly" value="20 Years" readonly>
                            <span class="suffix" style="pointer-events:none;"><svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
                        </div>
                    </div>
                    <div class="ak-new-slider-container">
                        <input type="range" id="tenureSliderNew" class="ak-new-slider" min="5" max="30" step="1" value="20" oninput="onTenureChangeSlider(this.value)">
                    </div>
                    <div class="ak-slider-labels">
                        <span>5 yrs</span>
                        <span>30 yrs</span>
                    </div>
                </div>

                <button class="ak-calc-emi-btn" onclick="scrollToResults()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="var(--ak-gold)" stroke-width="2" style="width:18px;height:18px;"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>
                    Calculate EMI
                </button>
                <div class="ak-secure-text">
                    <svg viewBox="0 0 24 24" fill="none" stroke="var(--ak-gold)" stroke-width="2" style="width:12px;height:12px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                    Your data is secure and will not be shared.
                </div>
            </div>

            <!-- Right Panel -->
            <div class="ak-calc-right-panel" id="resultsPanel">
                <div class="ak-right-header">Your Estimated EMI</div>
                <div class="ak-emi-highlight-row">
                    <div class="ak-emi-huge" id="resultEmi">₹ 69,428</div>
                    <div class="ak-emi-month">/month</div>
                    <div class="ak-affordable-badge">Affordable</div>
                </div>

                <div class="ak-3-stats">
                    <div class="ak-stat-item">
                        <div class="ak-stat-label">Loan Amount</div>
                        <div class="ak-stat-val" id="resultLoan">₹ 80,00,000</div>
                    </div>
                    <div class="ak-stat-item">
                        <div class="ak-stat-label">Total Interest</div>
                        <div class="ak-stat-val" id="resultInterest">₹ 86,62,720</div>
                    </div>
                    <div class="ak-stat-item">
                        <div class="ak-stat-label">Total Repayment</div>
                        <div class="ak-stat-val" id="resultRepay">₹ 1,66,62,720</div>
                    </div>
                </div>

                <div style="flex-grow:1; margin-top:2rem;">
                    <div class="ak-right-middle-grid">
                        <div style="display:flex; justify-content:center; align-items:center;">
                            <div class="ak-donut-wrapper-new">
                                <svg viewBox="0 0 36 36" class="ak-donut-svg">
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#D4AF37" stroke-width="4.2" id="donutPrincipal"/>
                                    <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#8B6508" stroke-width="4.2" stroke-dasharray="52, 100" stroke-dashoffset="-48" id="donutInterest"/>
                                </svg>
                                <div class="ak-donut-center">
                                    <div class="ak-donut-center-val" id="donutTenure">20</div>
                                    <div class="ak-donut-center-label">Years<br>Tenure</div>
                                </div>
                            </div>
                        </div>
                        <div style="display:flex; align-items:center;">
                            <div class="ak-legend-new">
                                <div class="ak-legend-item-new">
                                    <div class="ak-legend-label-row">
                                        <div class="ak-legend-dot-new principal"></div>
                                        <span>Principal</span>
                                    </div>
                                    <div class="ak-legend-val-new" id="legendPrincipalVal">₹ 80,00,000</div>
                                    <div class="ak-legend-pct" id="legendPrincipalPct">(48.0%)</div>
                                </div>
                                <div class="ak-legend-item-new">
                                    <div class="ak-legend-label-row">
                                        <div class="ak-legend-dot-new interest"></div>
                                        <span>Interest</span>
                                    </div>
                                    <div class="ak-legend-val-new" id="legendInterestVal">₹ 86,62,720</div>
                                    <div class="ak-legend-pct" id="legendInterestPct">(52.0%)</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="ak-stacked-bar-container">
                    <div class="ak-stacked-bar-title">Break-up of your total payment <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg></div>
                    <div class="ak-stacked-bar">
                        <div class="ak-bar-principal" id="barPrincipal" style="width: 48%;">48.0% (Principal)</div>
                        <div class="ak-bar-interest" id="barInterest" style="width: 52%;">52.0% (Interest)</div>
                    </div>
                </div>

            </div>
        </div>

        <!-- 4 Feature Cards -->
        <div class="ak-feature-cards">
            <div class="ak-fcard">
                <div class="ak-fcard-icon green"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"></path><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"></path><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"></path></svg></div>
                <div class="ak-fcard-title">Can You Afford This EMI?</div>
                <div class="ak-fcard-desc">Based on your income and existing commitments</div>
                <a href="#" class="ak-fcard-link green">Check Affordability &rarr;</a>
            </div>
            <div class="ak-fcard">
                <div class="ak-fcard-icon purple"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg></div>
                <div class="ak-fcard-title">Compare Tenures</div>
                <div class="ak-fcard-desc">See how EMI and total interest change with tenure</div>
                <a href="#" class="ak-fcard-link purple">Compare Now &rarr;</a>
            </div>
            <div class="ak-fcard">
                <div class="ak-fcard-icon blue"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg></div>
                <div class="ak-fcard-title">Interest Rate Impact</div>
                <div class="ak-fcard-desc">See how changes in interest rate affect your EMI</div>
                <a href="#" class="ak-fcard-link blue">View Impact &rarr;</a>
            </div>
            <div class="ak-fcard">
                <div class="ak-fcard-icon orange"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
                <div class="ak-fcard-title">Prepayment Savings</div>
                <div class="ak-fcard-desc">See how prepayments can save you interest</div>
                <a href="#" class="ak-fcard-link orange">Calculate Savings &rarr;</a>
            </div>
        </div>

        <!-- True Cost Strip -->
        <div class="ak-true-cost-strip">
            <div class="ak-tc-header">
                <h2 class="ak-tc-title">The True Cost of Your Home</h2>
                <div class="ak-tc-sub">Beyond the property price and EMI</div>
            </div>
            <div class="ak-tc-math-row">
                <div class="ak-tc-item">
                    <div class="ak-tc-icon-box"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg></div>
                    <div class="ak-tc-text">
                        <span class="ak-tc-label">Property Price</span>
                        <span class="ak-tc-val" id="tcPropVal">₹ 1,00,00,000</span>
                    </div>
                </div>
                <div class="ak-tc-operator">+</div>
                <div class="ak-tc-item">
                    <div class="ak-tc-icon-box"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
                    <div class="ak-tc-text">
                        <span class="ak-tc-label">Down Payment</span>
                        <span class="ak-tc-val" id="tcDownVal">₹ 20,00,000</span>
                    </div>
                </div>
                <div class="ak-tc-operator">+</div>
                <div class="ak-tc-item">
                    <div class="ak-tc-icon-box"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
                    <div class="ak-tc-text">
                        <span class="ak-tc-label">Stamp Duty &amp; Registration</span>
                        <span class="ak-tc-val" id="tcStampVal">₹ 6,50,000</span>
                    </div>
                </div>
                <div class="ak-tc-operator">+</div>
                <div class="ak-tc-item">
                    <div class="ak-tc-icon-box"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg></div>
                    <div class="ak-tc-text">
                        <span class="ak-tc-label">Other Costs <svg style="width:12px;height:12px;stroke:var(--ak-slate-light);vertical-align:middle;margin-bottom:2px;" viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg></span>
                        <span class="ak-tc-val" id="tcOtherVal">₹ 2,50,000</span>
                    </div>
                </div>
                <div class="ak-tc-operator">=</div>
                <div class="ak-tc-result-box">
                    <div class="ak-tc-result-label">Total Cash Required</div>
                    <div class="ak-tc-result-val" id="tcTotalVal">₹ 29,00,000</div>
                    <div class="ak-tc-result-sub">(Excluding loan amount)</div>
                </div>
            </div>
        </div>
    </main>
"""

js_new = """
    <!-- INTERACTIVE CALCULATOR ENGINE SCRIPT -->
    <script>
    // State
    var state = {
        propVal: 10000000,
        downPct: 20,
        interest: 8.5,
        tenure: 20
    };

    function parseRupees(str) {
        return parseInt(str.replace(/[^0-9]/g, '')) || 0;
    }

    function formatIndian(amount) {
        if (isNaN(amount) || amount === null) return '0';
        var x = Math.round(amount).toString();
        var lastThree = x.substring(x.length-3);
        var otherNumbers = x.substring(0, x.length-3);
        if (otherNumbers != '') lastThree = ',' + lastThree;
        return otherNumbers.replace(/\\B(?=(\\d{2})+(?!\\d))/g, ",") + lastThree;
    }

    function syncUI() {
        var downVal = (state.propVal * state.downPct) / 100;
        var loanVal = state.propVal - downVal;

        // Update Inputs
        document.getElementById('propValueInputNew').value = formatIndian(state.propVal);
        document.getElementById('propValueSliderNew').value = state.propVal;
        updateSliderFill('propValueSliderNew');

        document.getElementById('downPayInputNew').value = formatIndian(downVal);
        document.getElementById('downPaySliderNew').value = state.downPct;
        updateSliderFill('downPaySliderNew');

        document.getElementById('loanAmountInputNew').value = formatIndian(loanVal);

        document.getElementById('interestInputNew').value = state.interest.toFixed(2);
        document.getElementById('interestSliderNew').value = state.interest;
        updateSliderFill('interestSliderNew');

        document.getElementById('tenureInputNew').value = state.tenure + " Years";
        document.getElementById('tenureSliderNew').value = state.tenure;
        updateSliderFill('tenureSliderNew');
        document.getElementById('donutTenure').innerText = state.tenure;

        // Calculate EMI
        var monthlyRate = state.interest / 12 / 100;
        var totalMonths = state.tenure * 12;
        var emi = 0;
        if (loanVal > 0 && monthlyRate > 0 && totalMonths > 0) {
            var factor = Math.pow(1 + monthlyRate, totalMonths);
            emi = (loanVal * monthlyRate * factor) / (factor - 1);
        }
        var totalRepayment = emi * totalMonths;
        var totalInterest = Math.max(0, totalRepayment - loanVal);

        // Update Result Cards
        document.getElementById('resultEmi').innerText = "₹ " + formatIndian(emi);
        document.getElementById('resultLoan').innerText = "₹ " + formatIndian(loanVal);
        document.getElementById('resultInterest').innerText = "₹ " + formatIndian(totalInterest);
        document.getElementById('resultRepay').innerText = "₹ " + formatIndian(totalRepayment);

        // Update Legends & Bar
        var total = loanVal + totalInterest;
        var pPct = total > 0 ? (loanVal / total) * 100 : 50;
        var iPct = total > 0 ? (totalInterest / total) * 100 : 50;

        document.getElementById('legendPrincipalVal').innerText = "₹ " + formatIndian(loanVal);
        document.getElementById('legendInterestVal').innerText = "₹ " + formatIndian(totalInterest);
        document.getElementById('legendPrincipalPct').innerText = "(" + pPct.toFixed(1) + "%)";
        document.getElementById('legendInterestPct').innerText = "(" + iPct.toFixed(1) + "%)";

        document.getElementById('barPrincipal').style.width = pPct + "%";
        document.getElementById('barPrincipal').innerText = pPct.toFixed(1) + "% (Principal)";
        document.getElementById('barInterest').style.width = iPct + "%";
        document.getElementById('barInterest').innerText = iPct.toFixed(1) + "% (Interest)";

        // Donut Chart
        var dP = document.getElementById('donutPrincipal');
        var dI = document.getElementById('donutInterest');
        if (dP && dI) {
            dP.setAttribute('stroke-dasharray', pPct.toFixed(1) + ', 100');
            dI.setAttribute('stroke-dasharray', iPct.toFixed(1) + ', 100');
            dI.setAttribute('stroke-dashoffset', '-' + pPct.toFixed(1));
        }

        // True Cost Logic (Static % for demo)
        var stampDuty = state.propVal * 0.065; // 6.5%
        var otherCosts = state.propVal * 0.025; // 2.5%
        var totalCash = downVal + stampDuty + otherCosts;

        document.getElementById('tcPropVal').innerText = "₹ " + formatIndian(state.propVal);
        document.getElementById('tcDownVal').innerText = "₹ " + formatIndian(downVal);
        document.getElementById('tcStampVal').innerText = "₹ " + formatIndian(stampDuty);
        document.getElementById('tcOtherVal').innerText = "₹ " + formatIndian(otherCosts);
        document.getElementById('tcTotalVal').innerText = "₹ " + formatIndian(totalCash);
    }

    function updateSliderFill(id) {
        var el = document.getElementById(id);
        if(!el) return;
        var min = parseFloat(el.min || 0);
        var max = parseFloat(el.max || 100);
        var val = parseFloat(el.value);
        var pct = ((val - min) / (max - min)) * 100;
        // Create or update fill element
        var wrap = el.parentElement;
        var fill = wrap.querySelector('.ak-new-slider-fill');
        if(!fill) {
            fill = document.createElement('div');
            fill.className = 'ak-new-slider-fill';
            wrap.appendChild(fill);
        }
        fill.style.width = pct + '%';
    }

    // Input Handlers
    function onPropChangeInput(val) {
        var num = parseRupees(val);
        if (num < 1000000) num = 1000000;
        if (num > 100000000) num = 100000000;
        state.propVal = num;
        syncUI();
    }
    function onPropChangeSlider(val) {
        state.propVal = parseFloat(val);
        syncUI();
    }
    function onDownChangeInput(val) {
        var num = parseRupees(val);
        if (num > state.propVal) num = state.propVal;
        state.downPct = (num / state.propVal) * 100;
        syncUI();
    }
    function onDownChangeSlider(val) {
        state.downPct = parseFloat(val);
        syncUI();
    }
    function onInterestChangeInput(val) {
        var num = parseFloat(val.replace('%', ''));
        if (isNaN(num)) num = 8.5;
        if (num < 1) num = 1;
        if (num > 20) num = 20;
        state.interest = num;
        syncUI();
    }
    function onInterestChangeSlider(val) {
        state.interest = parseFloat(val);
        syncUI();
    }
    function onTenureChangeSlider(val) {
        state.tenure = parseInt(val);
        syncUI();
    }

    function scrollToResults() {
        if(window.innerWidth <= 950) {
            document.getElementById('resultsPanel').scrollIntoView({behavior: 'smooth'});
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        syncUI();
    });
    </script>
"""

# Regex replacements
content = re.sub(r'<style>.*?</style>', lambda _: '<style>' + css_new + '</style>', content, flags=re.DOTALL)
content = re.sub(r'<main class="ak-calc-section">.*?</main>', lambda _: html_new, content, flags=re.DOTALL)
content = re.sub(r'<!-- INTERACTIVE CALCULATOR ENGINE SCRIPT -->.*?</script>', lambda _: js_new, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
