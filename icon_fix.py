import re

file_path = "/Users/patidar/Desktop/AnK website/home-loan-emi-calculator/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Replacements
content = content.replace('.ak-trust-badge-icon svg {', '.ak-trust-badge-icon .material-symbols-outlined { font-size: 32px; color: var(--refined-brass); } /*')
content = content.replace('fill: rgba(140, 103, 52, 0.1);\n    }', '*/')

content = content.replace('.ak-panel-header svg {', '.ak-panel-header .material-symbols-outlined {')
content = content.replace('.ak-new-input-label svg {', '.ak-new-input-label .material-symbols-outlined {')

content = content.replace('.ak-fcard-icon svg {', '.ak-fcard-icon .material-symbols-outlined { font-size: 40px; } /*')
content = content.replace('width: 100%; height: 100%;\n    }', '*/')

content = content.replace('.ak-fcard-icon.green svg', '.ak-fcard-icon.green .material-symbols-outlined')
content = content.replace('.ak-fcard-icon.purple svg', '.ak-fcard-icon.purple .material-symbols-outlined')
content = content.replace('.ak-fcard-icon.blue svg', '.ak-fcard-icon.blue .material-symbols-outlined')
content = content.replace('.ak-fcard-icon.orange svg', '.ak-fcard-icon.orange .material-symbols-outlined')
content = content.replace('stroke: #2ECC71;', 'color: #2ECC71;')
content = content.replace('stroke: #9B59B6;', 'color: #9B59B6;')
content = content.replace('stroke: #3498DB;', 'color: #3498DB;')
content = content.replace('stroke: #E67E22;', 'color: #E67E22;')

content = content.replace('.ak-tc-icon-box svg {', '.ak-tc-icon-box .material-symbols-outlined {')
content = content.replace('stroke: var(--refined-brass);', 'color: var(--refined-brass);')

# HTML Replacements
svg_map = {
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>': '<span class="material-symbols-outlined">workspace_premium</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>': '<span class="material-symbols-outlined">home</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>': '<span class="material-symbols-outlined">info</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>': '<span class="material-symbols-outlined">account_balance_wallet</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect><circle cx="12" cy="12" r="2"></circle><path d="M6 12h.01M18 12h.01"></path></svg>': '<span class="material-symbols-outlined">payments</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>': '<span class="material-symbols-outlined">percent</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>': '<span class="material-symbols-outlined">calendar_month</span>',
    
    '<svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>': '<span class="material-symbols-outlined" style="font-size:16px;">expand_more</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="var(--refined-brass)" stroke-width="2" style="width:18px;height:18px;"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>': '<span class="material-symbols-outlined" style="font-size:20px; color:var(--refined-brass);">calculate</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="var(--refined-brass)" stroke-width="2" style="width:12px;height:12px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>': '<span class="material-symbols-outlined" style="font-size:14px; color:var(--refined-brass);">lock</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>': '<span class="material-symbols-outlined" style="font-size:16px;">info</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"></path><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"></path><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"></path></svg>': '<span class="material-symbols-outlined">account_balance_wallet</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg>': '<span class="material-symbols-outlined">tune</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>': '<span class="material-symbols-outlined">trending_up</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>': '<span class="material-symbols-outlined">currency_rupee</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>': '<span class="material-symbols-outlined">receipt_long</span>',
    
    '<svg style="width:12px;height:12px;stroke:var(--muted-slate);vertical-align:middle;margin-bottom:2px;" viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>': '<span class="material-symbols-outlined" style="font-size:14px; vertical-align:middle; margin-bottom:2px; color:var(--muted-slate);">help</span>',
    
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>': '<span class="material-symbols-outlined">home</span>',
}

for svg, span in svg_map.items():
    content = content.replace(svg, span)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
