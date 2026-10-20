document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('prop-search-input');
  const budgetSelect = document.getElementById('filter-budget');
  const configSelect = document.getElementById('filter-config');
  const sortSelect = document.getElementById('sort-select');
  const gridContainer = document.getElementById('properties-grid');
  const resultsCounter = document.getElementById('results-counter');

  if (!gridContainer || typeof PROPERTIES_DATA === 'undefined') return;

  const isSubpath = window.location.pathname.startsWith('/a-K/');
  const basePath = isSubpath ? '/a-K' : '';

  function updateQueryParams() {
    const params = new URLSearchParams();
    if (searchInput && searchInput.value.trim()) params.set('search', searchInput.value.trim());
    if (budgetSelect && budgetSelect.value) params.set('budget', budgetSelect.value);
    if (configSelect && configSelect.value) params.set('config', configSelect.value);
    if (sortSelect && sortSelect.value && sortSelect.value !== 'recommended') params.set('sort', sortSelect.value);

    const queryString = params.toString();
    const newUrl = queryString ? `${window.location.pathname}?${queryString}` : window.location.pathname;
    window.history.replaceState(null, '', newUrl);
  }

  function loadQueryParams() {
    const params = new URLSearchParams(window.location.search);
    const searchVal = params.get('search') || params.get('q');
    if (searchVal && searchInput) searchInput.value = searchVal;

    const budgetVal = params.get('budget');
    if (budgetVal && budgetSelect) budgetSelect.value = budgetVal;

    const configVal = params.get('config');
    if (configVal && configSelect) configSelect.value = configVal;

    const sortVal = params.get('sort');
    if (sortVal && sortSelect) sortSelect.value = sortVal;
  }

  function renderProperties(list) {
    gridContainer.innerHTML = '';

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
            <button type="button" class="primary-cta-btn" onclick="window.openModal && window.openModal();" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.25rem; font-family: 'Manrope', sans-serif; font-size: 0.88rem; font-weight: 700; border-radius: 4px; cursor: pointer; border: none; background: linear-gradient(135deg, #E88D67 0%, #9E3F23 100%); color: #FFFFFF; text-shadow: 0 1px 2px rgba(43,45,49,0.35);">
              <span>Request Off-Market Dossier</span>
              <span class="cta-arrow-badge" aria-hidden="true" style="display: inline-flex;"><svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="4.5" y1="11.5" x2="11.5" y2="4.5"></line><polyline points="6.5 4.5 11.5 4.5 11.5 9.5"></polyline></svg></span>
            </button>
            <button type="button" id="no-results-clear-btn" style="display: inline-flex; align-items: center; padding: 0.65rem 1.15rem; font-family: 'Manrope', sans-serif; font-size: 0.88rem; font-weight: 600; border-radius: 4px; cursor: pointer; border: 0.5px solid rgba(85, 85, 90, 0.3); background: #FAFAFA; color: #2B2D31; transition: all 0.25s ease;">
              <span>Reset All Filters</span>
            </button>
          </div>
        </div>
      `;
      updateCounter();
      if (typeof feather !== 'undefined') feather.replace();
      const resetBtn = document.getElementById('no-results-clear-btn');
      if (resetBtn) resetBtn.addEventListener('click', resetFilters);
      return;
    }

    const methodologyHref = (basePath || '') + '/#core';
    list.forEach((prop, idx) => {
      if (idx === 6) gridContainer.appendChild(buildCtaCard());
      const isReady = prop.possessionCategory === 'Ready to Move';
      const statusLabel = isReady ? 'Ready to move' : 'Under construction';
      const cardWrap = document.createElement('div');
      cardWrap.className = 'ak-card-anchor';

      cardWrap.innerHTML = `
        <article class="ak-property-card">
          <div class="ak-card-img-box">
            <img src="${prop.heroImg}" alt="${prop.name} ${prop.location}" width="${prop.heroW || 640}" height="${prop.heroH || 320}" ${idx < 3 ? 'loading="eager"' + (idx === 0 ? ' fetchpriority="high"' : '') : 'loading="lazy"'} decoding="async" onload="this.classList.add('is-loaded')" onerror="this.remove()" />
            <span class="ak-card-dev-badge">${prop.developer}</span>
            <span class="ak-status-pill ${isReady ? 'is-ready' : 'is-uc'}">${statusLabel}</span>
          </div>
          <div class="ak-card-body">
            <div class="ak-card-header">
              <div class="ak-card-title-row">
                <h3 class="ak-card-title"><a class="ak-card-stretch" href="${basePath + prop.url}">${prop.name}</a></h3>
                <span class="ak-card-score-pill" title="acre&key Score: ${prop.score} / 5"><span class="ak-score-val">${prop.score}</span><span class="ak-score-denom">/5</span></span>
              </div>
              <span class="ak-card-loc"><i data-feather="map-pin"></i> ${prop.sublocation || prop.location}</span>
            </div>

            <div class="ak-card-specs-ledger">
              <span class="ak-ledger-item ak-ledger-config"><i data-feather="home"></i> ${prop.config}</span>
              <span class="ak-ledger-sep">·</span>
              <span class="ak-ledger-item ak-ledger-size"><i data-feather="maximize-2"></i> ${prop.sizeRange}</span>
            </div>
          </div>
        </article>
      `;

      gridContainer.appendChild(cardWrap);
    });

    updateCounter();

    if (typeof feather !== 'undefined') {
      feather.replace();
    }
  }

  function buildCtaCard() {
    const el = document.createElement('div');
    el.className = 'ak-cta-card';
    el.innerHTML = `
      <span class="ak-cta-card-kicker">Not sure which fits?</span>
      <h3 class="ak-cta-card-title">Get a shortlist built around your brief</h3>
      <p class="ak-cta-card-text">Share your budget, commute and timeline. An acre&amp;key advisor will walk you through RERA records, possession risk and the trade-offs between projects.</p>
      <button type="button" class="primary-cta-btn ak-cta-card-btn" onclick="window.openModal && window.openModal();">Book a consultation</button>
    `;
    return el;
  }

  function updateCounter() {
    if (!resultsCounter) return;
    const shown = gridContainer.querySelectorAll('.ak-property-card').length;
    resultsCounter.textContent = `Showing ${shown} of ${PROPERTIES_DATA.length} verified projects`;
  }

  function filterAndSort(shouldUpdateUrl = true) {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedBudget = budgetSelect ? budgetSelect.value : '';
    const selectedConfig = configSelect ? configSelect.value : '';
    const selectedSort = sortSelect ? sortSelect.value : 'recommended';

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

      // Budget filter
      if (selectedBudget) {
        if (selectedBudget === 'under_1.5') {
          if (prop.minPrice >= 1.5) return false;
        } else if (selectedBudget === '1.5_2.5') {
          if (prop.minPrice > 2.5 || prop.maxPrice < 1.5) return false;
        } else if (selectedBudget === '2.5_4') {
          if (prop.minPrice > 4.0 || prop.maxPrice < 2.5) return false;
        } else if (selectedBudget === 'above_4') {
          if (prop.maxPrice < 4.0) return false;
        }
      }

      // Configuration filter
      if (selectedConfig) {
        if (selectedConfig === 'Villas') {
          if (!prop.configTypes.includes('Villas') && !prop.config.toLowerCase().includes('villa')) return false;
        } else {
          if (!prop.configTypes.includes(selectedConfig) && !prop.config.includes(selectedConfig)) return false;
        }
      }

      return true;
    });

    // Sorting
    if (selectedSort === 'score_desc') {
      filtered.sort((a, b) => b.score - a.score);
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
    if (budgetSelect) budgetSelect.value = '';
    if (configSelect) configSelect.value = '';
    if (sortSelect) sortSelect.value = 'recommended';
    filterAndSort();
  }

  // Event Listeners
  if (searchInput) searchInput.addEventListener('input', () => filterAndSort());
  if (budgetSelect) budgetSelect.addEventListener('change', () => filterAndSort());
  if (configSelect) configSelect.addEventListener('change', () => filterAndSort());
  if (sortSelect) sortSelect.addEventListener('change', () => filterAndSort());

  // Handle browser back/forward buttons
  window.addEventListener('popstate', function () {
    loadQueryParams();
    filterAndSort(false);
  });

  // Initial load from URL params
  loadQueryParams();
  filterAndSort(false);
});
