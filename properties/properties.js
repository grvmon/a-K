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
  const chipButtons = document.querySelectorAll('.props-chip');
  
  // Mobile drawer controls
  const mobileFilterToggleBtn = document.getElementById('mobile-filter-toggle-btn');
  const filterDrawer = document.getElementById('filter-drawer');
  const filterDrawerOverlay = document.getElementById('filter-drawer-overlay');
  const filterDrawerCloseBtn = document.getElementById('filter-drawer-close');

  if (!gridContainer || typeof PROPERTIES_DATA === 'undefined') return;

  const isSubpath = window.location.pathname.startsWith('/a-K/');
  const basePath = isSubpath ? '/a-K' : '';

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

  function syncChipsWithLocation(locValue) {
    chipButtons.forEach(chip => {
      const chipLoc = chip.getAttribute('data-location') || '';
      if (chipLoc === locValue) {
        chip.classList.add('is-active');
      } else {
        chip.classList.remove('is-active');
      }
    });
  }

  function updateQueryParams() {
    const params = new URLSearchParams();
    if (searchInput && searchInput.value.trim()) params.set('search', searchInput.value.trim());
    if (locationSelect && locationSelect.value) params.set('location', locationSelect.value);
    if (budgetSelect && budgetSelect.value) params.set('budget', budgetSelect.value);
    if (configSelect && configSelect.value) params.set('config', configSelect.value);
    if (possessionSelect && possessionSelect.value) params.set('possession', possessionSelect.value);
    if (developerSelect && developerSelect.value) params.set('developer', developerSelect.value);
    if (sortSelect && sortSelect.value && sortSelect.value !== 'recommended') params.set('sort', sortSelect.value);

    const queryString = params.toString();
    const newUrl = queryString ? `${window.location.pathname}?${queryString}` : window.location.pathname;
    window.history.replaceState(null, '', newUrl);
  }

  function loadQueryParams() {
    const params = new URLSearchParams(window.location.search);
    const searchVal = params.get('search') || params.get('q');
    if (searchVal && searchInput) searchInput.value = searchVal;

    const locVal = params.get('location') || params.get('loc');
    if (locVal && locationSelect) {
      locationSelect.value = locVal;
      syncChipsWithLocation(locVal);
    }

    const budgetVal = params.get('budget');
    if (budgetVal && budgetSelect) budgetSelect.value = budgetVal;

    const configVal = params.get('config');
    if (configVal && configSelect) configSelect.value = configVal;

    const possVal = params.get('possession');
    if (possVal && possessionSelect) possessionSelect.value = possVal;

    const devVal = params.get('developer');
    if (devVal && developerSelect) developerSelect.value = devVal;

    const sortVal = params.get('sort');
    if (sortVal && sortSelect) sortSelect.value = sortVal;
  }

  function renderProperties(list) {
    gridContainer.innerHTML = '';

    if (resultsCounter) {
      resultsCounter.textContent = `Showing ${list.length} of ${PROPERTIES_DATA.length} verified projects`;
    }

    if (list.length === 0) {
      gridContainer.innerHTML = `
        <div class="ak-no-results" style="grid-column: 1 / -1; max-width: 640px; margin: 2rem auto; text-align: center; background: #FFFFFF; border: 0.5px solid rgba(85, 85, 90, 0.2); border-radius: 4px; padding: 2.5rem 2rem;">
          <div style="width: 48px; height: 48px; margin: 0 auto 1rem auto; display: flex; align-items: center; justify-content: center; background: #FAFAFA; border: 0.5px solid rgba(85, 85, 90, 0.2); border-radius: 4px; color: #804526;">
            <i data-feather="compass"></i>
          </div>
          <span style="font-family: 'Manrope', sans-serif; font-size: 0.8rem; font-weight: 700; color: #804526; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 0.4rem;">Off-Market Due Diligence Concierge</span>
          <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.65rem; color: #2B2D31; font-weight: 400; margin: 0 0 0.6rem 0;">No published projects match these specific criteria</h3>
          <p style="font-family: 'Manrope', sans-serif; font-size: 0.92rem; color: #55555A; line-height: 1.6; margin: 0 0 1.5rem 0;">Our research team continually tracks pre-launch filings, phase expansions, and institutional builder inventory across Bengaluru that are not yet publicly listed.</p>
          <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
            <button type="button" class="primary-cta-btn" onclick="window.openModal &amp;&amp; window.openModal();" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.25rem; font-family: 'Manrope', sans-serif; font-size: 0.88rem; font-weight: 700; border-radius: 4px; cursor: pointer; border: none; background: linear-gradient(135deg, #E88D67 0%, #9E3F23 100%); color: #FFFFFF; text-shadow: 0 1px 2px rgba(43,45,49,0.35);">
              <span>Request Off-Market Dossier</span>
              <span class="cta-arrow-badge" aria-hidden="true" style="display: inline-flex;"><svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="4.5" y1="11.5" x2="11.5" y2="4.5"></line><polyline points="6.5 4.5 11.5 4.5 11.5 9.5"></polyline></svg></span>
            </button>
            <button type="button" id="no-results-clear-btn" style="display: inline-flex; align-items: center; padding: 0.65rem 1.15rem; font-family: 'Manrope', sans-serif; font-size: 0.88rem; font-weight: 600; border-radius: 4px; cursor: pointer; border: 0.5px solid rgba(85, 85, 90, 0.3); background: #FAFAFA; color: #2B2D31; transition: all 0.25s ease;">
              <span>Reset All Filters</span>
            </button>
          </div>
        </div>
      `;
      if (typeof feather !== 'undefined') feather.replace();
      const resetBtn = document.getElementById('no-results-clear-btn');
      if (resetBtn) resetBtn.addEventListener('click', resetFilters);
      return;
    }

    list.forEach(prop => {
      const cardAnchor = document.createElement('a');
      cardAnchor.href = basePath + prop.url;
      cardAnchor.className = 'ak-card-anchor';
      cardAnchor.setAttribute('aria-label', `View ${prop.name} property details`);

      cardAnchor.innerHTML = `
        <article class="ak-property-card">
          <div class="ak-card-img-box">
            <img src="${prop.heroImg}" alt="${prop.name} ${prop.location}" loading="lazy" />
            <span class="ak-card-dev-badge">${prop.developer}</span>
          </div>
          <div class="ak-card-body">
            <div class="ak-card-header">
              <h3 class="ak-card-title">${prop.name}</h3>
              <span class="ak-card-loc"><i data-feather="map-pin"></i> ${prop.sublocation || prop.location}</span>
            </div>
            
            <div class="ak-card-price-row">
              <span class="ak-card-price-label">Price Range</span>
              <span class="ak-card-price-val">${prop.priceRange}</span>
            </div>

            <div class="ak-card-specs">
              <div class="ak-spec-item">
                <i data-feather="home"></i>
                <span>${prop.config}</span>
              </div>
              <div class="ak-spec-item">
                <i data-feather="maximize-2"></i>
                <span>${prop.sizeRange}</span>
              </div>
              <div class="ak-spec-item">
                <i data-feather="calendar"></i>
                <span>${prop.possession.replace('Possession: ', '')}</span>
              </div>
            </div>

            <!-- Acre&Key Research Assessment Box -->
            <div class="ak-card-score-box">
              <div class="ak-score-badge">
                <span class="ak-score-num">${prop.score}</span>
                <span class="ak-score-sub">/ 5</span>
              </div>
              <div class="ak-score-verdict-wrap">
                <span class="ak-verdict-kicker">Acre&Key Verdict</span>
                <span class="ak-verdict-badge">${prop.verdict}</span>
              </div>
            </div>

            <div class="ak-card-footer">
              <span class="ak-card-cta-link">View Property <span class="ak-cta-arrow">→</span></span>
            </div>
          </div>
        </article>
      `;

      gridContainer.appendChild(cardAnchor);
    });

    if (typeof feather !== 'undefined') {
      feather.replace();
    }
  }

  function filterAndSort(shouldUpdateUrl = true) {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedLoc = locationSelect ? locationSelect.value : '';
    const selectedBudget = budgetSelect ? budgetSelect.value : '';
    const selectedConfig = configSelect ? configSelect.value : '';
    const selectedPoss = possessionSelect ? possessionSelect.value : '';
    const selectedDev = developerSelect ? developerSelect.value : '';
    const selectedSort = sortSelect ? sortSelect.value : 'recommended';

    syncChipsWithLocation(selectedLoc);

    let filtered = PROPERTIES_DATA.filter(prop => {
      // Search query
      if (query) {
        const matchesName = prop.name.toLowerCase().includes(query);
        const matchesDev = prop.developer.toLowerCase().includes(query);
        const matchesLoc = prop.location.toLowerCase().includes(query);
        const matchesSubLoc = prop.sublocation ? prop.sublocation.toLowerCase().includes(query) : false;
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

    if (shouldUpdateUrl) {
      updateQueryParams();
    }
  }

  function resetFilters() {
    if (searchInput) searchInput.value = '';
    if (locationSelect) locationSelect.value = '';
    if (budgetSelect) budgetSelect.value = '';
    if (configSelect) configSelect.value = '';
    if (possessionSelect) possessionSelect.value = '';
    if (developerSelect) developerSelect.value = '';
    if (sortSelect) sortSelect.value = 'recommended';
    syncChipsWithLocation('');
    filterAndSort();
  }

  // Chip Buttons Event Listeners
  chipButtons.forEach(chip => {
    chip.addEventListener('click', function () {
      const loc = this.getAttribute('data-location') || '';
      if (locationSelect) {
        locationSelect.value = loc;
      }
      syncChipsWithLocation(loc);
      filterAndSort();
    });
  });

  // Event Listeners
  if (searchInput) searchInput.addEventListener('input', () => filterAndSort());
  if (locationSelect) locationSelect.addEventListener('change', () => filterAndSort());
  if (budgetSelect) budgetSelect.addEventListener('change', () => filterAndSort());
  if (configSelect) configSelect.addEventListener('change', () => filterAndSort());
  if (possessionSelect) possessionSelect.addEventListener('change', () => filterAndSort());
  if (developerSelect) developerSelect.addEventListener('change', () => filterAndSort());
  if (sortSelect) sortSelect.addEventListener('change', () => filterAndSort());
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

  // Handle browser back/forward buttons
  window.addEventListener('popstate', function () {
    loadQueryParams();
    filterAndSort(false);
  });

  // Initial load from URL params
  loadQueryParams();
  filterAndSort(false);
});
