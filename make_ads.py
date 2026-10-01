import re

with open('style-guide/meta-posts-4-5.html', 'r') as f:
    html = f.read()

# Replace the inner HTML of .slider-container
new_frames = """
    <!-- Ad Variation 01: Z-Pattern (Authority) -->
    <div class="frame">
        <img class="frame-img" src="assets/riviera/riviera_villa_exterior.webp" alt="Ad 01">
        <div class="frame-overlay" style="background: linear-gradient(to bottom, rgba(10, 10, 11, 0.85) 0%, rgba(10, 10, 11, 0.2) 30%, rgba(10, 10, 11, 0.4) 60%, rgba(10, 10, 11, 0.95) 100%); justify-content: space-between; padding-top: 10%; padding-bottom: 15%; padding-left: 10%; padding-right: 10%;">
            
            <!-- Top Hook (Z Pattern Top Bar) -->
            <div style="display: flex; justify-content: space-between; align-items: flex-start; width: 100%;">
                <div class="brand-logo-josefin" style="font-size: 5cqw; letter-spacing: 0.05em; margin: 0; text-shadow: none;">acre&key</div>
                <div style="font-family: 'Manrope', sans-serif; font-size: 3cqw; font-weight: 700; color: var(--highlight-peach); text-transform: uppercase; letter-spacing: 0.1em; background: rgba(10, 10, 11, 0.6); padding: 0.8cqw 2cqw; border-radius: 4px; border: 0.5px solid var(--highlight-peach);">Premium Advisory</div>
            </div>

            <!-- Bottom CTA (Z Pattern Bottom Bar) -->
            <div style="display: flex; flex-direction: column; width: 100%; align-items: flex-start; gap: 2cqw;">
                <h1 class="frame-text" style="font-size: 7cqw; line-height: 1.15; white-space: normal; width: 90%; text-shadow: 0 4px 20px rgba(0,0,0,0.8);">
                    Stop relying on<br>developer brochures.
                </h1>
                <p style="font-family: 'Manrope', sans-serif; font-size: 3.2cqw; color: rgba(250, 250, 250, 0.85); margin: 0 0 2cqw 0; line-height: 1.4; text-shadow: 0 2px 10px rgba(0,0,0,0.8);">
                    Get unbiased, data-driven analysis<br>before you invest in Bengaluru real estate.
                </p>
                <div style="display: flex; justify-content: flex-end; width: 100%;">
                    <div style="font-family: 'Manrope', sans-serif; font-size: 3.5cqw; font-weight: 600; background: var(--cta-gradient); color: #FFF; padding: 2cqw 5cqw; border-radius: 4px; display: inline-flex; align-items: center; gap: 1cqw; box-shadow: 0 4px 12px rgba(140, 103, 52, 0.2);">
                        Talk to an Advisor
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Ad Variation 02: F-Pattern (Value Props) -->
    <div class="frame">
        <img class="frame-img" src="assets/images/moodboard/frame3_3x4.jpg" alt="Ad 02">
        <div class="frame-overlay" style="background: linear-gradient(to right, rgba(10, 10, 11, 0.95) 0%, rgba(10, 10, 11, 0.85) 40%, rgba(10, 10, 11, 0) 100%); justify-content: center; align-items: flex-start; padding-left: 10%; padding-right: 15%;">
            
            <h1 class="frame-text" style="font-size: 8cqw; line-height: 1.1; white-space: normal; text-align: left; margin-bottom: 5cqw;">
                <span style="color: var(--highlight-peach);">Independent</span><br>Home Buying.
            </h1>
            
            <div style="display: flex; flex-direction: column; gap: 3cqw; margin-bottom: 8cqw;">
                <div style="display: flex; align-items: center; gap: 2cqw;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--highlight-peach)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <span style="font-family: 'Manrope', sans-serif; font-size: 3.5cqw; font-weight: 500; color: #FAFAFA;">69-Point Due Diligence</span>
                </div>
                <div style="display: flex; align-items: center; gap: 2cqw;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--highlight-peach)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <span style="font-family: 'Manrope', sans-serif; font-size: 3.5cqw; font-weight: 500; color: #FAFAFA;">Asset Fundamentals Analysis</span>
                </div>
                <div style="display: flex; align-items: center; gap: 2cqw;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--highlight-peach)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <span style="font-family: 'Manrope', sans-serif; font-size: 3.5cqw; font-weight: 500; color: #FAFAFA;">₹0 Buyer Advisory Fee</span>
                </div>
            </div>

            <div style="font-family: 'Manrope', sans-serif; font-size: 3.5cqw; font-weight: 600; background: var(--cta-gradient); color: #FFF; padding: 2cqw 5cqw; border-radius: 4px; display: inline-flex; align-items: center; gap: 1cqw; box-shadow: 0 4px 12px rgba(140, 103, 52, 0.2);">
                Get Buyer Analysis
            </div>
            
        </div>
    </div>

    <!-- Ad Variation 03: Editorial Minimal (Hook) -->
    <div class="frame">
        <img class="frame-img" src="assets/images/moodboard/frame5_3x4.jpg" alt="Ad 03">
        <div class="frame-overlay center-overlay" style="background: radial-gradient(circle at center, rgba(10, 10, 11, 0.85) 0%, rgba(10, 10, 11, 0.6) 50%, rgba(10, 10, 11, 0.2) 100%);">
            
            <div style="display: flex; flex-direction: column; align-items: center; gap: 2cqw; margin-bottom: 6cqw;">
                <div class="brand-logo-josefin" style="font-size: 5cqw; opacity: 0.9; margin-bottom: 2cqw;">acre&key</div>
                <h1 class="frame-text" style="font-size: 6.5cqw; white-space: normal; text-align: center; line-height: 1.2;">
                    Anyone can give options.<br>
                    <span style="color: var(--highlight-peach);">We help you buy right.</span>
                </h1>
            </div>

            <div style="font-family: 'Manrope', sans-serif; font-size: 3.2cqw; font-weight: 600; background: transparent; border: 0.5px solid var(--highlight-peach); color: var(--highlight-peach); padding: 1.5cqw 4cqw; border-radius: 4px; display: inline-flex; align-items: center; gap: 1cqw;">
                Book Advisory Call
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </div>
            
        </div>
    </div>
"""

# Extract everything before <div class="slider-container"> and after it
pre = html.split('<div class="slider-container">')[0]
post = html.split('</div>\n\n    </div>\n\n<script>')[1]

# Update the title
pre = pre.replace('Meta Posts Moodboard', 'Meta Ads Campaign (4:5)')
pre = pre.replace('meta-posts-4-5.html', 'meta-ads-campaign.html')

new_html = pre + '<div class="slider-container">\n' + new_frames + '\n    </div>\n\n<script>' + post

with open('style-guide/meta-ads-campaign.html', 'w') as f:
    f.write(new_html)

# Add to index.html
with open('style-guide/index.html', 'r') as f:
    index_html = f.read()

new_link = """            <a href="meta-ads-campaign.html" target="_blank" style="font-size: 0.8rem; color: var(--text-copper-aaa); font-weight: 600;">↳ Meta Ads Campaign (4:5)</a>"""

index_html = index_html.replace('            <a href="meta-posts-4-5.html"', new_link + '\n            <a href="meta-posts-4-5.html"')

new_btn = """                <a href="meta-ads-campaign.html" target="_blank" class="ak-btn-primary" style="display:inline-flex; align-items:center; gap:0.5rem; background: var(--text-copper-aaa); color: white; border: none;">
                    View Meta Ads (4:5)
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>"""

index_html = index_html.replace('                <a href="meta-posts-4-5.html"', new_btn + '\n                <a href="meta-posts-4-5.html"')

with open('style-guide/index.html', 'w') as f:
    f.write(index_html)
