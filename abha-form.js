/**
 * ── Talk to Abha Lead Modal Widget ──
 * Standalone lead capture widget for the floating Abha advisor.
 * Fully decoupled from lead-form.js.
 */
(function() {
  'use strict';

  var REDIRECT_URL = (typeof window.abhaRedirectUrl !== 'undefined') ? window.abhaRedirectUrl : '/thankyou';
  var HUBSPOT_PORTAL_ID = '23862215';
  var HUBSPOT_FORM_GUID = '9b14b80b-ee22-446a-86c3-1d00c3b03f0b';

  var modalOverlay, modalWrap, form, nameInput, phoneInput, emailInput, submitBtn, globalErr;
  var nameField, phoneField, emailField, nameErr, phoneErr, emailErr;
  var isSubmitting = false;

  function getQueryParam(param) {
    if (!window.location.search) return '';
    var params = new URLSearchParams(window.location.search);
    return params.get(param) || '';
  }

  function getTrackingPayload() {
    return {
      gclid: getQueryParam('gclid') || sessionStorage.getItem('lf_gclid') || '',
      fclid: getQueryParam('fclid') || sessionStorage.getItem('lf_fclid') || '',
      utm_source: getQueryParam('utm_source') || sessionStorage.getItem('lf_utm_source') || '',
      utm_medium: getQueryParam('utm_medium') || sessionStorage.getItem('lf_utm_medium') || '',
      utm_campaign: getQueryParam('utm_campaign') || sessionStorage.getItem('lf_utm_campaign') || '',
      utm_term: getQueryParam('utm_term') || sessionStorage.getItem('lf_utm_term') || '',
      utm_content: getQueryParam('utm_content') || sessionStorage.getItem('lf_utm_content') || '',
      source_url: window.location.href,
      submitted_at: new Date().toISOString()
    };
  }

  function injectModalMarkup() {
    if (document.getElementById('abhaModalOverlay')) return;

    var avatarUrl = (window.location.origin && window.location.origin.indexOf('http') === 0)
      ? '/style-guide/assets/advisor-abha.webp'
      : 'https://acrenkey.com/style-guide/assets/advisor-abha.webp';

    var html = '' +
      '<div class="abha-modal-overlay" id="abhaModalOverlay" aria-hidden="true">' +
        '<div class="abha-modal-backdrop" id="abhaModalBackdrop"></div>' +
        '<div class="abha-modal-wrap" id="abhaModalWrap" role="dialog" aria-modal="true" aria-labelledby="abhaHeading" aria-describedby="abhaSubheading">' +
          '<div class="abha-drag-handle"></div>' +
          '<button type="button" class="abha-close-btn" id="abhaCloseBtn" aria-label="Close Talk to Abha modal">' +
            '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">' +
              '<path d="M1 1l12 12M13 1L1 13"/>' +
            '</svg>' +
          '</button>' +
          '<div class="abha-modal-header">' +
            '<div class="abha-header-avatar-wrap">' +
              '<svg class="abha-header-rays" width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">' +
                '<path d="M13 20L8 16" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
                '<path d="M16 14L11 8" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
                '<path d="M23 9L20 3" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
              '</svg>' +
              '<img src="' + avatarUrl + '" alt="Abha - Home Buying Advisor" class="abha-header-avatar-img" width="82" height="82">' +
              '<span class="abha-header-status-dot" aria-label="Abha is online"></span>' +
            '</div>' +
            '<div class="abha-header-text">' +
              '<h2 class="abha-modal-title" id="abhaHeading">Talk to Abha</h2>' +
              '<p class="abha-modal-subtitle" id="abhaSubheading">We need some details to get started.</p>' +
            '</div>' +
          '</div>' +
          '<form class="abha-form" id="abhaForm" novalidate>' +
            '<div class="abha-field" id="abhaNameField">' +
              '<div class="abha-input-box">' +
                '<span class="abha-field-icon" aria-hidden="true">' +
                  '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
                    '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>' +
                    '<circle cx="12" cy="7" r="4"></circle>' +
                  '</svg>' +
                '</span>' +
                '<input type="text" class="abha-input" id="abhaName" name="name" placeholder="Full Name*" autocomplete="name" enterkeyhint="next" required maxlength="60">' +
              '</div>' +
              '<div class="abha-field-err" id="abhaNameErr" role="alert"></div>' +
            '</div>' +
            '<div class="abha-field" id="abhaPhoneField">' +
              '<div class="abha-input-box">' +
                '<span class="abha-field-icon" aria-hidden="true">' +
                  '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
                    '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>' +
                  '</svg>' +
                '</span>' +
                '<input type="tel" class="abha-input" id="abhaPhone" name="phone" placeholder="+91 Mobile Number*" autocomplete="tel" enterkeyhint="next" inputmode="numeric" required maxlength="16">' +
              '</div>' +
              '<div class="abha-field-err" id="abhaPhoneErr" role="alert"></div>' +
            '</div>' +
            '<div class="abha-field" id="abhaEmailField">' +
              '<div class="abha-input-box">' +
                '<span class="abha-field-icon" aria-hidden="true">' +
                  '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
                    '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>' +
                    '<polyline points="22,6 12,13 2,6"></polyline>' +
                  '</svg>' +
                '</span>' +
                '<input type="email" class="abha-input" id="abhaEmail" name="email" placeholder="Email (Optional)" autocomplete="email" enterkeyhint="done" maxlength="120">' +
              '</div>' +
              '<div class="abha-field-err" id="abhaEmailErr" role="alert"></div>' +
            '</div>' +
            '<button type="submit" class="abha-submit-btn" id="abhaSubmitBtn">' +
              '<span class="abha-btn-spinner" aria-hidden="true"></span>' +
              '<span class="abha-btn-text">Talk to Abha</span>' +
              '<svg class="abha-btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
                '<line x1="5" y1="12" x2="19" y2="12"></line>' +
                '<polyline points="12 5 19 12 12 19"></polyline>' +
              '</svg>' +
            '</button>' +
            '<p class="abha-consent-text">' +
              'By submitting your details, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.' +
            '</p>' +
            '<p class="abha-global-err" id="abhaGlobalErr" role="alert" aria-live="assertive"></p>' +
          '</form>' +
        '</div>' +
      '</div>';

    var container = document.createElement('div');
    container.innerHTML = html;
    document.body.appendChild(container.firstElementChild);
  }

  function initElements() {
    injectModalMarkup();

    modalOverlay = document.getElementById('abhaModalOverlay');
    modalWrap    = document.getElementById('abhaModalWrap');
    form         = document.getElementById('abhaForm');
    nameInput    = document.getElementById('abhaName');
    phoneInput   = document.getElementById('abhaPhone');
    emailInput   = document.getElementById('abhaEmail');
    submitBtn    = document.getElementById('abhaSubmitBtn');
    globalErr    = document.getElementById('abhaGlobalErr');

    nameField    = document.getElementById('abhaNameField');
    phoneField   = document.getElementById('abhaPhoneField');
    emailField   = document.getElementById('abhaEmailField');

    nameErr      = document.getElementById('abhaNameErr');
    phoneErr     = document.getElementById('abhaPhoneErr');
    emailErr     = document.getElementById('abhaEmailErr');

    var backdrop = document.getElementById('abhaModalBackdrop');
    if (backdrop) backdrop.addEventListener('click', closeModal);

    var closeBtn = document.getElementById('abhaCloseBtn');
    if (closeBtn) closeBtn.addEventListener('click', closeModal);

    if (form) form.addEventListener('submit', handleSubmit);

    // Live validation on blur/input
    if (nameInput) {
      nameInput.addEventListener('input', function() { if (nameField.classList.contains('abha-has-error')) validateName(); });
      nameInput.addEventListener('blur', validateName);
    }
    if (phoneInput) {
      phoneInput.addEventListener('input', function() {
        // Auto-sanitize digits
        var val = phoneInput.value;
        if (val.indexOf('+') === 0) {
          phoneInput.value = '+' + val.substring(1).replace(/\D/g, '');
        } else {
          phoneInput.value = val.replace(/[^\d+]/g, '');
        }
        if (phoneField.classList.contains('abha-has-error')) validatePhone();
      });
      phoneInput.addEventListener('blur', validatePhone);
    }
    if (emailInput) {
      emailInput.addEventListener('input', function() { if (emailField.classList.contains('abha-has-error')) validateEmail(); });
      emailInput.addEventListener('blur', validateEmail);
    }

    // Keyboard support: ESC to close
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('abha-modal-open')) {
        closeModal();
      }
    });
  }

  function setFieldError(field, errEl, message) {
    if (!field) return;
    if (message) {
      field.classList.add('abha-has-error');
      if (errEl) {
        errEl.textContent = message;
        errEl.style.display = 'block';
      }
    } else {
      field.classList.remove('abha-has-error');
      if (errEl) {
        errEl.textContent = '';
        errEl.style.display = 'none';
      }
    }
  }

  function validateName() {
    if (!nameInput) return true;
    var val = nameInput.value.trim();
    if (!val) {
      setFieldError(nameField, nameErr, 'Please enter your full name');
      return false;
    }
    if (val.length < 2) {
      setFieldError(nameField, nameErr, 'Name must be at least 2 characters');
      return false;
    }
    setFieldError(nameField, nameErr, '');
    return true;
  }

  function validatePhone() {
    if (!phoneInput) return true;
    var val = phoneInput.value.trim().replace(/[\s\-()]/g, '');
    if (!val) {
      setFieldError(phoneField, phoneErr, 'Please enter your mobile number');
      return false;
    }
    // Check Indian 10-digit number or international with +
    var digitsOnly = val.replace(/\D/g, '');
    if (val.indexOf('+91') === 0) {
      digitsOnly = val.substring(3).replace(/\D/g, '');
    } else if (val.indexOf('91') === 0 && digitsOnly.length === 12) {
      digitsOnly = digitsOnly.substring(2);
    }

    if (digitsOnly.length === 10) {
      if (!/^[6-9]\d{9}$/.test(digitsOnly)) {
        setFieldError(phoneField, phoneErr, 'Please enter a valid 10-digit mobile number');
        return false;
      }
    } else if (digitsOnly.length < 7 || digitsOnly.length > 15) {
      setFieldError(phoneField, phoneErr, 'Please enter a valid mobile number');
      return false;
    }
    setFieldError(phoneField, phoneErr, '');
    return true;
  }

  function validateEmail() {
    if (!emailInput) return true;
    var val = emailInput.value.trim();
    if (!val) {
      // Email is optional in Talk to Abha widget
      setFieldError(emailField, emailErr, '');
      return true;
    }
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    if (!emailRegex.test(val)) {
      setFieldError(emailField, emailErr, 'Please enter a valid email address');
      return false;
    }
    setFieldError(emailField, emailErr, '');
    return true;
  }

  async function sendToApi(payload) {
    // 1. Custom function hook: window.sendAbhaData(payload)
    if (typeof window.sendAbhaData === 'function') {
      return await window.sendAbhaData(payload);
    }

    // 2. Custom API URL hook: window.abhaApiUrl
    if (window.abhaApiUrl) {
      var res = await fetch(window.abhaApiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error('API submission failed with status ' + res.status);
      return await res.json().catch(function() { return { success: true }; });
    }

    // 3. Default API: HubSpot Forms API
    var portalId = window.abhaHubspotPortalId || window.lfHubspotPortalId || HUBSPOT_PORTAL_ID;
    var formGuid = window.abhaHubspotFormGuid || window.lfHubspotFormGuid || HUBSPOT_FORM_GUID;
    var hsUrl = 'https://api.hsforms.com/submissions/v3/integration/submit/' + portalId + '/' + formGuid;

    var fields = [
      { name: 'firstname', value: payload.name },
      { name: 'phone', value: payload.phone },
      { name: 'mobilephone', value: payload.phone }
    ];
    if (payload.email) {
      fields.push({ name: 'email', value: payload.email });
    }

    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fclid'].forEach(function(k) {
      if (payload[k]) fields.push({ name: k, value: payload[k] });
    });

    var hsBody = {
      fields: fields,
      context: {
        pageUri: payload.source_url || window.location.href,
        pageName: document.title || 'acre&key - Talk to Abha'
      }
    };

    var hsRes = await fetch(hsUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(hsBody)
    });

    if (!hsRes.ok) {
      var errData = await hsRes.json().catch(function() { return {}; });
      throw new Error(errData.message || ('HubSpot API error ' + hsRes.status));
    }

    return await hsRes.json().catch(function() { return { inlineMessage: 'Success' }; });
  }

  async function handleSubmit(e) {
    if (e) e.preventDefault();
    if (isSubmitting) return;

    var isNameValid = validateName();
    var isPhoneValid = validatePhone();
    var isEmailValid = validateEmail();

    if (!isNameValid || !isPhoneValid || !isEmailValid) {
      if (!isNameValid && nameInput) nameInput.focus();
      else if (!isPhoneValid && phoneInput) phoneInput.focus();
      else if (!isEmailValid && emailInput) emailInput.focus();
      return;
    }

    isSubmitting = true;
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.classList.add('abha-loading');
    }
    if (globalErr) {
      globalErr.classList.remove('abha-show');
      globalErr.textContent = '';
    }

    var tracking = getTrackingPayload();
    var rawPhone = phoneInput.value.trim().replace(/[\s\-()]/g, '');
    var formattedPhone = rawPhone.indexOf('+') === 0 ? rawPhone : ('+91' + rawPhone);

    var payload = {
      name: nameInput.value.trim(),
      phone: formattedPhone,
      email: emailInput.value.trim().toLowerCase(),
      source_widget: 'talk_to_abha',
      source_url: tracking.source_url,
      submitted_at: tracking.submitted_at,
      gclid: tracking.gclid,
      fclid: tracking.fclid,
      utm_source: tracking.utm_source,
      utm_medium: tracking.utm_medium,
      utm_campaign: tracking.utm_campaign,
      utm_term: tracking.utm_term,
      utm_content: tracking.utm_content
    };

    try {
      await sendToApi(payload);

      // Direct redirection matching user request
      var targetUrl = REDIRECT_URL;
      if (window.location.search && targetUrl.indexOf('?') === -1) {
        targetUrl += window.location.search;
      }
      window.location.href = targetUrl;
    } catch (err) {
      isSubmitting = false;
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.classList.remove('abha-loading');
      }
      if (globalErr) {
        globalErr.classList.add('abha-show');
        globalErr.textContent = 'Connection issue. Please check your details and try again.';
      }
      console.error('[Abha Form API Submission Failed]', err);
    }
  }

  function openModal() {
    if (!modalOverlay) initElements();
    if (!modalOverlay) return;

    modalOverlay.classList.add('abha-modal-open');
    modalOverlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Reset errors
    [nameField, phoneField, emailField].forEach(function(f) { if (f) f.classList.remove('abha-has-error'); });
    [nameErr, phoneErr, emailErr].forEach(function(el) { if (el) { el.textContent = ''; el.style.display = 'none'; } });
    if (globalErr) { globalErr.classList.remove('abha-show'); globalErr.textContent = ''; }

    // Auto-focus first input
    setTimeout(function() {
      if (nameInput) nameInput.focus();
    }, 200);
  }

  function closeModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('abha-modal-open');
    modalOverlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Public API
  window.openAbhaModal = openModal;
  window.closeAbhaModal = closeModal;

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initElements);
  } else {
    initElements();
  }
})();
