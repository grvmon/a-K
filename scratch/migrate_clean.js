const fs = require('fs');
const cheerio = require('cheerio');

const pEvergreen = fs.readFileSync('property/prestige-evergreen-raintree-park/index.html', 'utf8');
const pAlembic = fs.readFileSync('scratch/alembic_v1.html', 'utf8');

const $ = cheerio.load(pEvergreen, { decodeEntities: false });
const $v1 = cheerio.load(pAlembic, { decodeEntities: false });

// 1. Meta / SEO
$('title').text($v1('title').text());
$('meta[name="description"]').attr('content', $v1('meta[name="description"]').attr('content'));
$('link[rel="canonical"]').attr('href', 'https://acrenkey.com/property/alembic-cloud-forest-alembic-city/');

// OG Tags
$('meta[property^="og:"], meta[name^="twitter:"]').remove();
$('head').append($v1('meta[property^="og:"], meta[name^="twitter:"]'));

// Schema
$('script[type="application/ld+json"]').remove();
$('head').append($v1('script[type="application/ld+json"]'));

// 2. Hero Info Header
$('.ak-info-title').text('ALEMBIC CLOUD FOREST');
// The subtitle in Alembic is "At Alembic City · Kadugodi / Hope Farm"
$('.ak-info-meta').html('<span style="white-space:nowrap; display:inline-flex; align-items:center; gap:0.35rem;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#7D442A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg><span>At Alembic City · Kadugodi / Hope Farm</span></span>');

// Score
// Alembic Score: 3.90/5
let scoreHTML = $v1('.prop-glance-item:contains("SCORE")').prev().html(); // V1 actually doesn't have openAkScoreModal in the same way, but it has 3.90
// Let's hardcode Alembic score based on previous knowledge: 3.90
const scoreBox = $('div[onclick*="window.openAkScoreModal"]');
scoreBox.find('span').eq(0).text('3.90');
scoreBox.find('div:last-child div:last-child').text('Integrated City Living. Strong East Bengaluru Location.');

// 3. Glance Grid
const $v1Glance = $v1('.prop-snapshot-strip-v2');
if ($v1Glance.length) {
    // We will extract data from V1's snapshot strip
    let items = $v1Glance.find('.prop-snapshot-item-v2');
    // V2 has 5 items.
    let v2Items = $('.prop-glance-item');
    
    // Map items
    if(items.length >= 4) {
        // Status
        v2Items.eq(0).find('.prop-glance-num').text('Q4 2029');
        v2Items.eq(0).find('div:last-child').text('Possession');
        // Price
        v2Items.eq(1).find('.prop-glance-num').text('₹1.37 Cr');
        v2Items.eq(1).find('div:last-child').text('Starting Price');
        // Acres
        v2Items.eq(2).find('.prop-glance-num').text('~15');
        v2Items.eq(2).find('div:last-child').text('Acres');
        // Units
        v2Items.eq(3).find('.prop-glance-num').text('1,330');
        v2Items.eq(3).find('div:last-child').text('Units');
        // Configs
        v2Items.eq(4).find('.prop-glance-num').text('2–3.5 BHK');
        v2Items.eq(4).find('div:last-child').text('Configurations');
    }
}

// 4. Hero Gallery & JS array
// Remove prestige images from html thumbnail gallery
$('.ak-editorial-thumb').remove(); 
// Alembic images
const alembicImages = [
  { src: '../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1', alt: 'Alembic City Towers Elevation View' },
  { src: '../../style-guide/assets/alembic/alembic_hero_retail_plaza.webp?v=20260830_v1', alt: 'Biophilic Retail & Dining Plaza' },
  { src: '../../style-guide/assets/alembic/alembic_hero_dining_canopy.webp?v=20260830_v1', alt: 'Alfresco Dining Canopy' },
  { src: '../../style-guide/assets/alembic/alembic_hero_commercial_hub.webp?v=20260830_v1', alt: 'Alembic Commercial Hub' }
];

let thumbHtml = '';
alembicImages.forEach((img, i) => {
   thumbHtml += `<button type="button" class="ak-editorial-thumb" onclick="event.stopPropagation(); window.akGallerySelect(${i});" aria-label="View ${img.alt}" title="${img.alt}"><img src="${img.src}" alt="${img.alt}"></button>\n`;
});
// Add video thumb
thumbHtml += `<button type="button" class="ak-editorial-thumb" onclick="event.stopPropagation(); window.akGallerySelect(4);" aria-label="View Video" title="Walkthrough Video">
  <img src="../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1" alt="Walkthrough Video">
  <div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; background:rgba(0,0,0,0.25);">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.5"><circle cx="12" cy="12" r="10" fill="rgba(0,0,0,0.55)"></circle><polygon points="10 8 16 12 10 16 10 8" fill="#7D442A"></polygon></svg>
  </div>
</button>`;

$('.ak-editorial-gallery-trigger').before(thumbHtml);

$('#akMainHeroImage').attr('src', alembicImages[0].src);
$('#akMainHeroImage').attr('alt', alembicImages[0].alt);
$('.ak-editorial-tag').text('ALEMBIC CLOUD FOREST');

// 5. Replace JS array in HTML string later

// 6. Section Content Swaps
// ABOUT
$('#about').html($v1('#overview').html());
// Add padding to match V2 style
$('#about').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// ADVISORY
$('#advisory').html($v1('#assessment').html());
$('#advisory').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// MASTERPLAN
$('#masterplan').html($v1('#amenities').html());
$('#masterplan').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// FLOOR PLANS
$('#floor-plans').html($v1('#floor-plans').html());
$('#floor-plans').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// PRICING
$('#pricing').html($v1('#true-cost').html());
$('#pricing').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// GROWTH
$('#growth').html($v1('#appreciation').html());
$('#growth').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// LOCATION
$('#location').html($v1('#location').html()); // V1 actually has two: location and locality
$('#location').append($v1('#locality').html());
$('#location').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// DILIGENCE
$('#diligence').html($v1('#rera-legal').html());
$('#diligence').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

// COMPARE (Keep Prestige's layout but adjust text)
// Just remove it or keep it? We'll leave it as is, maybe remove the compare block for now.
$('#compare').remove();

// FAQS
$('#faqs').html($v1('#faqs').html());
$('#faqs').css({ 'padding-top': '4.5rem', 'padding-bottom': '1rem' });

let outHTML = $.html();

// Fix JS Gallery Array
outHTML = outHTML.replace(/const akGalleryMedia = \[[\s\S]*?\];/, `const akGalleryMedia = [
  { type: 'image', src: '../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1', alt: 'Alembic City Towers Elevation View', category: 'Exterior' },
  { type: 'image', src: '../../style-guide/assets/alembic/alembic_hero_retail_plaza.webp?v=20260830_v1', alt: 'Biophilic Retail & Dining Plaza', category: 'Lifestyle' },
  { type: 'image', src: '../../style-guide/assets/alembic/alembic_hero_dining_canopy.webp?v=20260830_v1', alt: 'Alfresco Dining Canopy', category: 'Amenities' },
  { type: 'image', src: '../../style-guide/assets/alembic/alembic_hero_commercial_hub.webp?v=20260830_v1', alt: 'Alembic Commercial Hub', category: 'Masterplan' },
  { type: 'video', src: '../../style-guide/assets/alembic_cloud_forest_walkthrough.mp4?v=20260830_v1', poster: '../../style-guide/assets/alembic/alembic_hero_tower_elevation.webp?v=20260830_v1', alt: 'Official Walkthrough Video', category: 'Video Tour' }
];`);

// Fix akLbTotal string
outHTML = outHTML.replace(/<span id="akLbTotal">08<\/span>/g, '<span id="akLbTotal">05</span>');
outHTML = outHTML.replace(/<span id="akHeroSlideTotal">06<\/span>/g, '<span id="akHeroSlideTotal">05</span>');

// Save back
fs.writeFileSync('property/alembic-cloud-forest-alembic-city/index.html', outHTML);

