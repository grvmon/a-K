import re

def fix_css(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace the peach gradient on CTA hovers with a solid copper or a darker gradient, or just dim it.
    # We will replace linear-gradient(...) with var(--text-copper-aaa) for CTA backgrounds on hover to ensure AAA contrast with white text.
    content = re.sub(r'background:\s*linear-gradient\([^)]+var\(--highlight-peach\)[^)]+\)\s*!important;', r'background: var(--text-copper-aaa) !important;', content)
    
    # Remove transform: translateY(-1px) !important
    content = re.sub(r'transform:\s*translateY\(-1px\)\s*!important;?', '', content)

    # Make sure text-copper-aaa is defined properly.
    
    # Let's fix inline links in paragraphs. The user didn't mention this, but I should apply Rule 13:
    # "Inline Link Behavior... Luxury Underlines: Inline links must use `--text-copper-aaa` with a `1px` thick underline that is offset by `text-underline-offset: 4px;` or `6px;`.
    # Hover State: The underline should be slightly transparent (`rgba(128,69,38,0.3)`) and turn fully solid on hover over `0.4s`."
    # Let's append this to the end of the CSS to safely override inline links in the body.
    
    inline_link_css = """
/* Rule 13: Inline Link Behavior */
p a, li a, .editorial-text a {
    color: var(--text-copper-aaa);
    text-decoration: underline;
    text-decoration-color: rgba(128,69,38,0.3);
    text-decoration-thickness: 1px;
    text-underline-offset: 4px;
    transition: text-decoration-color 0.4s ease;
}
p a:hover, li a:hover, .editorial-text a:hover {
    text-decoration-color: var(--text-copper-aaa);
}
"""
    # Append if not exists
    if "/* Rule 13" not in content:
        content += inline_link_css

    with open(filepath, 'w') as f:
        f.write(content)

fix_css('website.css')
print("Done")
