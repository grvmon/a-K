from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

cards = soup.find_all('div', class_='framework-card')

data = [
    {
        'title': 'LOCATION',
        'sub': 'Connectivity, Livability & Demand',
        'bullets': ['IT hubs & connectivity', 'Metro, roads & infrastructure', 'Water & everyday essentials'],
        'questions': ['Will demand hold up?', 'Is infrastructure keeping pace?']
    },
    {
        'title': 'DEVELOPER',
        'sub': 'Strength, Delivery & Quality',
        'bullets': ['Past projects & delivery', 'Financial strength', 'Build quality & defects'],
        'questions': ['Can they deliver on time?', 'How good is the build?']
    },
    {
        'title': 'PROPERTY',
        'sub': 'Layout, Legal & True Cost',
        'bullets': ['Total cost & hidden charges', 'Space & layout efficiency', 'Title, approvals & RERA'],
        'questions': ['Is everything legally in place?', 'Is the price justified?']
    },
    {
        'title': 'YOU',
        'sub': 'Lifestyle, Priorities & Resale',
        'bullets': ['Light, ventilation & comfort', 'Space for work & family', 'Commute & resale potential'],
        'questions': ['Does this fit your life?', 'Will it hold its value?']
    }
]

for i, card in enumerate(cards):
    if i >= len(data):
        break
    
    d = data[i]
    
    # Update Title (leave badge alone)
    title_el = card.find('h3', class_='framework-card-title')
    if title_el:
        title_el.string = d['title']
        
    sub_el = card.find('div', class_='framework-card-sub')
    if sub_el:
        sub_el.string = d['sub']
        
    bullet_list = card.find('ul', class_='framework-bullets')
    if bullet_list:
        lis = bullet_list.find_all('li')
        for j, li in enumerate(lis):
            if j < len(d['bullets']):
                # Find the SVG
                svg = li.find('svg')
                # Clear content
                li.clear()
                # Append SVG back if exists
                if svg:
                    li.append(svg)
                # Append new text
                li.append(" " + d['bullets'][j])
                
    q_list = card.find('ul', class_='framework-questions-list')
    if q_list:
        lis = q_list.find_all('li')
        for j, li in enumerate(lis):
            if j < len(d['questions']):
                li.string = d['questions'][j]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
