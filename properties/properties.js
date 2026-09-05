document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('prop-search-input');
  const locationSelect = document.getElementById('filter-location');
  const budgetSelect = document.getElementById('filter-budget');
  const configSelect = document.getElementById('filter-config');
  const possessionSelect = document.getElementById('filter-possession');
  const developerSelect = document.getElementById('filter-developer');
  const sortSelect = document.getElementById('sort-select');
  const gridContainer = document.getElementById('properties-grid');
  const resultsCounter = document.getElementById('results-counter');
  const clearFiltersBtn = document.getElementById('clear-filters-btn');
  
  // Mobile drawer controls
  const mobileFilterToggleBtn = document.getElementById('mobile-filter-toggle-btn');
  const filterDrawer = document.getElementById('filter-drawer');
  const filterDrawerOverlay = document.getElementById('filter-drawer-overlay');
  const filterDrawerCloseBtn = document.getElementById('filter-drawer-close');

  if (!gridContainer || typeof PROPERTIES_DATA === 'undefined') return;

  // Populate Developer Filter dynamically from properties data
  if (developerSelect && developerSelect.options.length <= 1) {
    const developers = Array.from(new Set(PROPERTIES_DATA.map(p => p.developer))).sort();
    developers.forEach(dev => {
      const opt = document.createElement('option');
      opt.value = dev;
      opt.textContent = dev;
      developerSelect.appendChild(opt);
    });
  }

  // Populate Location Filter dynamically from properties data
  if (locationSelect && locationSelect.options.length <= 1) {
    const locations = Array.from(new Set(PROPERTIES_DATA.map(p => p.location))).sort();
    locations.forEach(loc => {
      const opt = document.createElement('option');
      opt.value = loc;
      opt.textContent = loc;
      locationSelect.appendChild(opt);
    });
  }

  function renderProperties(list) {
    gridContainer.innerHTML = '';

    if (resultsCounter) {
      resultsCounter.textContent = `Showing ${list.length} of ${PROPERTIES_DATA.length} verified projects`;
    }

    if (list.length === 0) {
      gridContainer.innerHTML = `
        <div class="ak-no-results">
          <div class="ak-no-results-icon"><i data-feather="search"></i></div>
          <h3>No properties match your search</h3>
          <p>Try adjusting your search keywords, budget, or location filters to see more results.</p>
          <button type="button" class="sd-btn-gold" id="no-results-clear-btn" style="margin-top:1rem;">
            <span>Reset All Filters</span>
          </button>
        </div>
      `;
      if (typeof feather !== 'undefined') feather.replace();
      const resetBtn = document.getElementById('no-results-clear-btn');
      if (resetBtn) resetBtn.addEventListener('click', resetFilters);
      return;
    }

    list.forEach(prop => {
      const cardAnchor = document.createElement('a');
      cardAnchor.href = prop.url;
      cardAnchor.className = 'ak-card-anchor';
      cardAnchor.setAttribute('aria-label', `View ${prop.name} property details`);

      const minPriceStr = prop.minPrice ? `₹${prop.minPrice.toFixed(2).replace(/\.00$/, '')} Cr` : prop.priceRange;
      const hasMaxPrice = prop.maxPrice && prop.maxPrice !== prop.minPrice;
      const maxPriceStr = hasMaxPrice ? `Up to ₹${prop.maxPrice.toFixed(2).replace(/\.00$/, '')} Cr` : '';

      cardAnchor.innerHTML = `
        <article class="ak-property-card">
          <div class="ak-card-img-box">
            <img src="${prop.heroImg}" alt="${prop.name} ${prop.location}" loading="lazy" decoding="async" />
            <div class="ak-card-img-overlay"></div>
            <span class="ak-card-dev-badge">${prop.developer}</span>
          </div>
          <div class="ak-card-body">
            <div class="ak-card-header">
              <h3 class="ak-card-title">${prop.name}</h3>
              <div class="ak-card-loc">
                <i data-feather="map-pin"></i>
                <span>${prop.sublocation || prop.location}</span>
              </div>
            </div>
            
            <div class="ak-card-price-container">
              <div class="ak-price-main-wrap">
                <span class="ak-price-kicker">STARTING FROM</span>
                <span class="ak-price-val">${minPriceStr}</span>
              </div>
              ${hasMaxPrice ? `
                <div class="ak-price-upto-wrap">
                  <span class="ak-price-upto-val">${maxPriceStr}</span>
                </div>
              ` : ''}
            </div>

            <div class="ak-card-specs-grid">
              <div class="ak-spec-row">
                <i data-feather="home" class="ak-spec-icon"></i>
                <span class="ak-spec-text">${prop.config}</span>
              </div>
              <div class="ak-spec-row">
                <i data-feather="maximize-2" class="ak-spec-icon"></i>
                <span class="ak-spec-text">${prop.sizeRange}</span>
              </div>
              <div class="ak-spec-row">
                <i data-feather="calendar" class="ak-spec-icon"></i>
                <span class="ak-spec-text">${prop.possession}</span>
              </div>
            </div>

            <!-- Acre&Key Research Assessment Box -->
            <div class="ak-card-verdict-box">
              <div class="ak-verdict-score-sq">
                <span class="ak-verdict-score-num">${prop.score}</span>
                <span class="ak-verdict-score-sub">/ 5</span>
              </div>
              <div class="ak-verdict-info">
                <div class="ak-verdict-top-row">
                  <span class="ak-verdict-kicker">ACRE&KEY VERDICT</span>
                  <span class="ak-verdict-why">Why this verdict? <span class="ak-why-arrow">→</span></span>
                </div>
                <div class="ak-verdict-statement">${prop.verdict}</div>
              </div>
            </div>

            <div class="ak-card-footer">
              <button type="button" class="ak-card-compare-btn" aria-label="Compare ${prop.name}">
                <i data-feather="plus" class="ak-compare-icon"></i>
                <span>+ Compare</span>
              </button>
              <span class="ak-card-primary-cta">
                <span>Explore Property</span>
                <span class="ak-cta-arrow">→</span>
              </span>
            </div>
          </div>
        </article>
      `;

      gridContainer.appendChild(cardAnchor);

      const compareBtn = cardAnchor.querySelector('.ak-card-compare-btn');
      if (compareBtn) {
        compareBtn.addEventListener('click', function (e) {
          e.preventDefault();
          e.stopPropagation();
          this.classList.toggle('active');
          const span = this.querySelector('span');
          if (this.classList.contains('active')) {
            if (span) span.textContent = '✓ Added';
            this.style.borderColor = '#8C6734';
            this.style.background = 'rgba(140, 103, 52, 0.12)';
            this.style.color = '#5E4119';
          } else {
            if (span) span.textContent = '+ Compare';
            this.style.borderColor = '';
            this.style.background = '';
            this.style.color = '';
          }
        });
      }
    });

    if (typeof feather !== 'undefined') {
      feather.replace();
    }
  }

  function filterAndSort() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedLoc = locationSelect ? locationSelect.value : '';
    const selectedBudget = budgetSelect ? budgetSelect.value : '';
    const selectedConfig = configSelect ? configSelect.value : '';
    const selectedPoss = possessionSelect ? possessionSelect.value : '';
    const selectedDev = developerSelect ? developerSelect.value : '';
    const selectedSort = sortSelect ? sortSelect.value : 'recommended';

    let filtered = PROPERTIES_DATA.filter(prop => {
      // Search query
      if (query) {
        const matchesName = prop.name.toLowerCase().includes(query);
        const matchesDev = prop.developer.toLowerCase().includes(query);
        const matchesLoc = prop.location.toLowerCase().includes(query);
        const matchesSubLoc = prop.sublocation.toLowerCase().includes(query);
        if (!matchesName && !matchesDev && !matchesLoc && !matchesSubLoc) {
          return false;
        }
      }

      // Location filter
      if (selectedLoc && prop.location !== selectedLoc && !prop.sublocation.includes(selectedLoc)) {
        return false;
      }

      // Developer filter
      if (selectedDev && prop.developer !== selectedDev) {
        return false;
      }

      // Configuration filter
      if (selectedConfig) {
        if (selectedConfig === 'Villas') {
          if (!prop.configTypes.includes('Villas') && !prop.config.toLowerCase().includes('villa')) return false;
        } else {
          if (!prop.configTypes.includes(selectedConfig) && !prop.config.includes(selectedConfig)) return false;
        }
      }

      // Budget filter
      if (selectedBudget) {
        if (selectedBudget === 'under_1.5' && prop.minPrice > 1.5) return false;
        if (selectedBudget === '1.5_2' && (prop.minPrice > 2.0 || prop.maxPrice < 1.5)) return false;
        if (selectedBudget === '2_3' && (prop.minPrice > 3.0 || prop.maxPrice < 2.0)) return false;
        if (selectedBudget === '3_5' && (prop.minPrice > 5.0 || prop.maxPrice < 3.0)) return false;
        if (selectedBudget === 'above_5' && prop.maxPrice < 5.0) return false;
      }

      // Possession filter
      if (selectedPoss) {
        if (selectedPoss === 'ready' && prop.possessionCategory !== 'Ready to Move') return false;
        if (selectedPoss === 'under_1' && prop.possessionCategory !== '< 1 Year' && prop.possessionCategory !== 'Ready to Move') return false;
        if (selectedPoss === '1_2' && prop.possessionCategory !== '1–2 Years') return false;
        if (selectedPoss === '2_4' && prop.possessionCategory !== '2–4 Years') return false;
        if (selectedPoss === 'above_4' && prop.possessionCategory !== '4+ Years') return false;
      }

      return true;
    });

    // Sorting
    if (selectedSort === 'score_desc') {
      filtered.sort((a, b) => b.score - a.score);
    } else if (selectedSort === 'price_asc') {
      filtered.sort((a, b) => a.minPrice - b.minPrice);
    } else if (selectedSort === 'price_desc') {
      filtered.sort((a, b) => b.maxPrice - a.maxPrice);
    } else if (selectedSort === 'possession_asc') {
      filtered.sort((a, b) => a.possessionYear - b.possessionYear);
    }

    renderProperties(filtered);
  }

  function resetFilters() {
    if (searchInput) searchInput.value = '';
    if (locationSelect) locationSelect.value = '';
    if (budgetSelect) budgetSelect.value = '';
    if (configSelect) configSelect.value = '';
    if (possessionSelect) possessionSelect.value = '';
    if (developerSelect) developerSelect.value = '';
    if (sortSelect) sortSelect.value = 'recommended';
    filterAndSort();
  }

  // Event Listeners
  if (searchInput) searchInput.addEventListener('input', filterAndSort);
  if (locationSelect) locationSelect.addEventListener('change', filterAndSort);
  if (budgetSelect) budgetSelect.addEventListener('change', filterAndSort);
  if (configSelect) configSelect.addEventListener('change', filterAndSort);
  if (possessionSelect) possessionSelect.addEventListener('change', filterAndSort);
  if (developerSelect) developerSelect.addEventListener('change', filterAndSort);
  if (sortSelect) sortSelect.addEventListener('change', filterAndSort);
  if (clearFiltersBtn) clearFiltersBtn.addEventListener('click', resetFilters);

  // Mobile drawer handlers
  function openFilterDrawer() {
    if (filterDrawer) filterDrawer.classList.add('is-active');
    if (filterDrawerOverlay) filterDrawerOverlay.classList.add('is-active');
  }

  function closeFilterDrawer() {
    if (filterDrawer) filterDrawer.classList.remove('is-active');
    if (filterDrawerOverlay) filterDrawerOverlay.classList.remove('is-active');
  }

  if (mobileFilterToggleBtn) mobileFilterToggleBtn.addEventListener('click', openFilterDrawer);
  if (filterDrawerCloseBtn) filterDrawerCloseBtn.addEventListener('click', closeFilterDrawer);
  if (filterDrawerOverlay) filterDrawerOverlay.addEventListener('click', closeFilterDrawer);

  // Initial render
  filterAndSort();
});
