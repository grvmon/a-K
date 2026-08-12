import os

file_path = "/Users/patidar/Desktop/AnK website/home-loan-emi-calculator/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_h1 = """    .ak-calc-header-left .ak-calc-h1 {
        font-family: var(--font-heading);
        font-size: clamp(28px, 4vw, 42px);
        color: var(--deep-navy-100);
        margin: 0 0 0.5rem 0;
        font-weight: 400;
        letter-spacing: -0.02em;
    }"""
new_h1 = """    .ak-calc-header-left .ak-calc-h1 {
        font-family: var(--font-heading);
        font-size: clamp(1.5rem, 1.25rem + 1vw, 2rem);
        line-height: 1.25;
        color: var(--deep-navy);
        margin: 0 0 0.5rem 0;
        font-weight: 400;
        letter-spacing: -0.01em;
    }"""

old_sub = """    .ak-calc-sub-text {
        font-size: 1.1rem;
        color: var(--deep-slate);
        margin: 0 0 0.25rem 0;
    }"""
new_sub = """    .ak-calc-sub-text {
        font-size: 18px;
        line-height: 1.85rem;
        color: var(--deep-slate);
        margin: 0 0 0.25rem 0;
        font-weight: 200;
    }"""

old_tc_title = """    .ak-tc-title {
        font-family: var(--font-heading);
        font-size: 1.6rem;
        color: var(--deep-navy-100);
        margin: 0 0 0.2rem 0;
    }"""
new_tc_title = """    .ak-tc-title {
        font-family: var(--font-heading);
        font-size: clamp(20px, 6vw, 30px);
        color: var(--deep-navy);
        margin: 0 0 0.2rem 0;
        line-height: 1.04em;
        letter-spacing: -0.02em;
        font-weight: 400;
    }"""

content = content.replace(old_h1, new_h1)
content = content.replace(old_sub, new_sub)
content = content.replace(old_tc_title, new_tc_title)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
