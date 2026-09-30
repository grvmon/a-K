import re

with open('property/alembic-cloud-forest-alembic-city/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for grid
css = """
<style>
/* V2 Grid Layout Classes */
.prop-content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 350px;
  gap: 2rem;
  align-items: start;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}
.prop-sidebar-column {
  position: sticky;
  top: 140px;
}
@media (max-width: 1024px) {
  .prop-content-grid {
    grid-template-columns: 1fr;
  }
  .prop-sidebar-column {
    position: static;
    margin-top: 2rem;
  }
}
</style>
"""
if "prop-content-grid" not in html:
    html = html.replace('</head>', css + '</head>')

# 2. Wrap Sections
start_marker = '<section id="overview"'
end_marker = '<!-- SECTION 8: STILL COMPARING PROPERTIES FOOTER CTA -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1 and 'class="prop-content-grid"' not in html[start_idx-50:start_idx]:
    before = html[:start_idx]
    middle = html[start_idx:end_idx]
    after = html[end_idx:]
    
    sidebar_html = """
<div class="prop-sidebar-column">
  <div style="background:#FFFFFF; border:1px solid #DDD7CF; border-radius: 4px; padding:1.5rem; box-shadow:0 4px 16px rgba(15, 31, 61, 0.04);">
    <h3 style="font-family:'Cormorant Garamond',serif; font-size:1.6rem; font-weight:700; color:#2F3B42; margin:0 0 1rem 0;">Get Official Details</h3>
    <p style="font-size:0.9rem; color:#4A5861; margin-bottom:1.5rem; line-height:1.5;">Download the official brochure, high-res floor plans, and detailed cost sheet.</p>
    <button type="button" onclick="window.openModal();" style="width:100%; background:linear-gradient(135deg, #be7555 0%, #9f5334 100%); color:#FFFFFF; border:none; padding:0.9rem; font-size:0.95rem; font-weight:700; border-radius:4px; cursor:pointer;">Download Brochure →</button>
  </div>
</div>
"""
    wrapped = f'<div class="prop-content-grid">\n<div class="prop-main-column">\n{middle}</div>\n{sidebar_html}</div>\n'
    html = before + wrapped + after

# 3. Port over .prop-glance-grid
glance_grid_html = """
<div class="prop-snapshot-strip-v2" style="background: transparent !important; border: none !important; box-shadow: none !important; border-radius: 0 !important; margin-top: 1rem !important; padding: 0 !important;">
  <div class="prop-glance-header" style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.75rem;">
    <div style="display:flex; align-items:center; gap:1rem;">
      <span class="prop-glance-tag" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.14em; color: #7D442A; text-transform: uppercase;">PROPERTY AT A GLANCE</span>
      <span class="prop-glance-rule" style="width: 80px; height: 1px; background: #D5C7B8;"></span>
    </div>
  </div>

  <div class="prop-glance-grid" style="display: grid; grid-template-columns: repeat(5, 1fr); align-items: center;">
    <div class="prop-glance-item" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0.15rem 0.75rem; position: relative;">
      <span class="prop-glance-num" style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #1F2937; line-height: 1; letter-spacing: -0.02em; margin-bottom: 0.25rem;">~15</span>
      <span class="prop-glance-lbl" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: #4B5563; text-transform: uppercase; line-height: 1.2;">ACRES</span>
    </div>
    <div class="prop-glance-item" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0.15rem 0.75rem; position: relative; border-left: 1px solid #DDD7CF;">
      <span class="prop-glance-num" style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #1F2937; line-height: 1; letter-spacing: -0.02em; margin-bottom: 0.25rem;">3</span>
      <span class="prop-glance-lbl" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: #4B5563; text-transform: uppercase; line-height: 1.2;">TOWERS</span>
    </div>
    <div class="prop-glance-item" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0.15rem 0.75rem; position: relative; border-left: 1px solid #DDD7CF;">
      <span class="prop-glance-num" style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #1F2937; line-height: 1; letter-spacing: -0.02em; margin-bottom: 0.25rem;">1,330</span>
      <span class="prop-glance-lbl" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: #4B5563; text-transform: uppercase; line-height: 1.2;">HOMES</span>
    </div>
    <div class="prop-glance-item" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0.15rem 0.75rem; position: relative; border-left: 1px solid #DDD7CF;">
      <span class="prop-glance-num" style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #1F2937; line-height: 1; letter-spacing: -0.02em; margin-bottom: 0.25rem;">>70%</span>
      <span class="prop-glance-lbl" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: #4B5563; text-transform: uppercase; line-height: 1.2;">OPEN AREA</span>
    </div>
    <div class="prop-glance-item" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0.15rem 0.75rem; position: relative; border-left: 1px solid #DDD7CF;">
      <span class="prop-glance-num" style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #1F2937; line-height: 1; letter-spacing: -0.02em; margin-bottom: 0.25rem;">22</span>
      <span class="prop-glance-lbl" style="font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em; color: #4B5563; text-transform: uppercase; line-height: 1.2;">AMENITIES</span>
    </div>
  </div>
</div>
"""
old_snapshot_pattern = r'<div class="prop-snapshot-strip-v2">.*?</div>\s*</div>\s*</div>\s*</div>'
html = re.sub(old_snapshot_pattern, glance_grid_html, html, flags=re.DOTALL)


# 4. Replace ak-gallery-wrapper with ak-hero-editorial-gallery
editorial_gallery_html = """
<div class="ak-hero-editorial-gallery" id="akHeroGallery" style="position: relative; width: 100%; height: 100%; min-height: clamp(450px, 52vh, 500px); border-radius: 4px; overflow: hidden; background-color: #141B22; box-sizing: border-box;">
  <div class="ak-editorial-media-canvas" onclick="openAkLightbox(window.akGalleryIndex || 0);" style="position: absolute; inset: 0; width: 100%; height: 100%; cursor: pointer;">
    <img id="akMainHeroImage" src="../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1" alt="Alembic City Towers Elevation View" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.4s ease;">
    <video id="akMainHeroVideo" style="display:none; width: 100%; height: 100%; object-fit: cover; display: none;" muted="" loop="" playsinline=""></video>
  </div>

  <div class="ak-editorial-top-left" style="position: absolute; top: 28px; left: 28px; z-index: 5; pointer-events: none; display: flex; flex-direction: column; align-items: flex-start;">
    <div class="ak-editorial-tag" style="font-family: 'Josefin Sans', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: #FFFFFF; line-height: 1; margin-bottom: 8px; text-shadow: 0 1px 4px rgba(0, 0, 0, 0.7);">ALEMBIC CLOUD FOREST</div>
    <div class="ak-editorial-counter" style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 22px; font-weight: 500; letter-spacing: 0.05em; color: #FFFFFF; line-height: 1; text-shadow: 0 1px 4px rgba(0, 0, 0, 0.7);"><span id="akHeroSlideNum">01</span> &nbsp;/&nbsp; <span id="akHeroSlideTotal">04</span></div>
    <div class="ak-editorial-line" style="width: 44px; height: 1.5px; background: #FFFFFF; margin-top: 8px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);"></div>
  </div>

  <div class="ak-editorial-top-right" style="position: absolute; top: 28px; right: 28px; z-index: 5; display: flex; gap: 8px; pointer-events: auto;">
    <button type="button" class="ak-editorial-nav-btn" aria-label="Previous slide" onclick="event.stopPropagation(); akGalleryPrev();" style="width: 36px; height: 36px; background: rgba(18, 26, 32, 0.4); backdrop-filter: blur(4px); border: 1px solid rgba(255, 255, 255, 0.75); border-radius: 4px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #FFF;">&lt;</button>
    <button type="button" class="ak-editorial-nav-btn" aria-label="Next slide" onclick="event.stopPropagation(); akGalleryNext();" style="width: 36px; height: 36px; background: rgba(18, 26, 32, 0.4); backdrop-filter: blur(4px); border: 1px solid rgba(255, 255, 255, 0.75); border-radius: 4px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #FFF;">&gt;</button>
  </div>

  <div class="ak-editorial-bottom-strip" style="position: absolute; bottom: 0; left: 0; right: 0; height: 100px; background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0.45) 60%, transparent 100%); z-index: 5; display: flex; align-items: flex-end; justify-content: space-between; padding: 0 20px 18px 20px; box-sizing: border-box; pointer-events: none; gap: 12px;">
    <div class="ak-editorial-thumbs-row" style="display: flex; gap: 6px; align-items: center; pointer-events: auto; overflow-x: auto; flex: 1; min-width: 0; padding: 8px 4px 6px 4px; margin: -8px -4px -6px -4px;">
      <button type="button" class="ak-editorial-thumb active" onclick="event.stopPropagation(); akGallerySelect(0);" style="width: 52px; height: 38px; border: 1px solid rgba(255, 255, 255, 0.45); border-radius: 4px; overflow: hidden; background: #0F1B24; cursor: pointer; opacity: 0.8; flex-shrink: 0; padding: 0;">
        <img src="../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1" style="width: 100%; height: 100%; object-fit: cover;">
      </button>
      <button type="button" class="ak-editorial-thumb" onclick="event.stopPropagation(); akGallerySelect(1);" style="width: 52px; height: 38px; border: 1px solid rgba(255, 255, 255, 0.45); border-radius: 4px; overflow: hidden; background: #0F1B24; cursor: pointer; opacity: 0.8; flex-shrink: 0; padding: 0;">
        <img src="../../style-guide/assets/alembic/alembic_hero_retail_plaza.webp?v=20260830_v1" style="width: 100%; height: 100%; object-fit: cover;">
      </button>
      <button type="button" class="ak-editorial-thumb" onclick="event.stopPropagation(); akGallerySelect(2);" style="width: 52px; height: 38px; border: 1px solid rgba(255, 255, 255, 0.45); border-radius: 4px; overflow: hidden; background: #0F1B24; cursor: pointer; opacity: 0.8; flex-shrink: 0; padding: 0;">
        <img src="../../style-guide/assets/alembic/alembic_hero_dining_canopy.webp?v=20260830_v1" style="width: 100%; height: 100%; object-fit: cover;">
      </button>
      <button type="button" class="ak-editorial-thumb" onclick="event.stopPropagation(); akGallerySelect(3);" style="width: 52px; height: 38px; border: 1px solid rgba(255, 255, 255, 0.45); border-radius: 4px; overflow: hidden; background: #0F1B24; cursor: pointer; opacity: 0.8; flex-shrink: 0; padding: 0;">
        <img src="../../style-guide/assets/alembic/alembic_hero_commercial_hub.webp?v=20260830_v1" style="width: 100%; height: 100%; object-fit: cover;">
      </button>
    </div>

    <div class="ak-editorial-gallery-trigger" style="display: flex; align-items: center; pointer-events: auto; flex-shrink: 0;">
      <div class="ak-editorial-divider" style="width: 1px; height: 28px; background: rgba(255, 255, 255, 0.45); margin-left: 8px; margin-right: 20px;"></div>
      <button type="button" class="ak-editorial-view-btn" onclick="event.stopPropagation(); openAkLightbox(window.akGalleryIndex || 0);" style="display: flex; align-items: center; gap: 10px; background: none; border: none; padding: 0; cursor: pointer; color: #FFFFFF; font-family: 'Manrope', sans-serif; font-size: 14px; font-weight: 500;">
        <span>View gallery</span>
      </button>
    </div>
  </div>
</div>
"""
old_gallery_pattern = r'<div class="ak-gallery-wrapper" id="akHeroGallery".*?<button class="ak-view-all-text-btn".*?</button>\s*</div>\s*</div>\s*</div>'
html = re.sub(old_gallery_pattern, editorial_gallery_html, html, flags=re.DOTALL)

with open('property/alembic-cloud-forest-alembic-city/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
