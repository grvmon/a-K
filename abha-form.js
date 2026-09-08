/**
 * ── Talk to Abha Lead Modal Widget ──
 * Standalone, decoupled lead capture widget for the floating Abha advisor.
 * Features identical field styling, floating labels, country code picker,
 * validation, and Refined Brass CTA button as the primary advisory form.
 */
(function() {
  'use strict';

  var REDIRECT_URL = (typeof window.abhaRedirectUrl !== 'undefined') ? window.abhaRedirectUrl : '/thankyou';
  var HUBSPOT_PORTAL_ID = '23862215';
  var HUBSPOT_FORM_GUID = '9b14b80b-ee22-446a-86c3-1d00c3b03f0b';

  var COUNTRIES = [
    {name:"Afghanistan",code:"AF",dial:"+93",len:9},{name:"Albania",code:"AL",dial:"+355",len:9},
    {name:"Algeria",code:"DZ",dial:"+213",len:9},{name:"Andorra",code:"AD",dial:"+376",len:6},
    {name:"Angola",code:"AO",dial:"+244",len:9},{name:"Antigua & Barbuda",code:"AG",dial:"+1",len:10},
    {name:"Argentina",code:"AR",dial:"+54",len:10},{name:"Armenia",code:"AM",dial:"+374",len:8},
    {name:"Australia",code:"AU",dial:"+61",len:9},{name:"Austria",code:"AT",dial:"+43",len:10},
    {name:"Azerbaijan",code:"AZ",dial:"+994",len:9},{name:"Bahamas",code:"BS",dial:"+1",len:10},
    {name:"Bahrain",code:"BH",dial:"+973",len:8},{name:"Bangladesh",code:"BD",dial:"+880",len:10},
    {name:"Barbados",code:"BB",dial:"+1",len:10},{name:"Belarus",code:"BY",dial:"+375",len:9},
    {name:"Belgium",code:"BE",dial:"+32",len:9},{name:"Belize",code:"BZ",dial:"+501",len:7},
    {name:"Benin",code:"BJ",dial:"+229",len:8},{name:"Bhutan",code:"BT",dial:"+975",len:8},
    {name:"Bolivia",code:"BO",dial:"+591",len:8},{name:"Bosnia & Herzegovina",code:"BA",dial:"+387",len:8},
    {name:"Botswana",code:"BW",dial:"+267",len:8},{name:"Brazil",code:"BR",dial:"+55",len:11},
    {name:"Brunei",code:"BN",dial:"+673",len:7},{name:"Bulgaria",code:"BG",dial:"+359",len:9},
    {name:"Burkina Faso",code:"BF",dial:"+226",len:8},{name:"Burundi",code:"BI",dial:"+257",len:8},
    {name:"Cambodia",code:"KH",dial:"+855",len:9},{name:"Cameroon",code:"CM",dial:"+237",len:9},
    {name:"Canada",code:"CA",dial:"+1",len:10},{name:"Cape Verde",code:"CV",dial:"+238",len:7},
    {name:"Central African Republic",code:"CF",dial:"+236",len:8},{name:"Chad",code:"TD",dial:"+235",len:8},
    {name:"Chile",code:"CL",dial:"+56",len:9},{name:"China",code:"CN",dial:"+86",len:11},
    {name:"Colombia",code:"CO",dial:"+57",len:10},{name:"Comoros",code:"KM",dial:"+269",len:7},
    {name:"Congo (DRC)",code:"CD",dial:"+243",len:9},{name:"Congo (Republic)",code:"CG",dial:"+242",len:9},
    {name:"Costa Rica",code:"CR",dial:"+506",len:8},{name:"Croatia",code:"HR",dial:"+385",len:9},
    {name:"Cuba",code:"CU",dial:"+53",len:8},{name:"Cyprus",code:"CY",dial:"+357",len:8},
    {name:"Czech Republic",code:"CZ",dial:"+420",len:9},{name:"Denmark",code:"DK",dial:"+45",len:8},
    {name:"Djibouti",code:"DJ",dial:"+253",len:8},{name:"Dominica",code:"DM",dial:"+1",len:10},
    {name:"Dominican Republic",code:"DO",dial:"+1",len:10},{name:"Ecuador",code:"EC",dial:"+593",len:9},
    {name:"Egypt",code:"EG",dial:"+20",len:10},{name:"El Salvador",code:"SV",dial:"+503",len:8},
    {name:"Equatorial Guinea",code:"GQ",dial:"+240",len:9},{name:"Eritrea",code:"ER",dial:"+291",len:7},
    {name:"Estonia",code:"EE",dial:"+372",len:8},{name:"Eswatini",code:"SZ",dial:"+268",len:8},
    {name:"Ethiopia",code:"ET",dial:"+251",len:9},{name:"Fiji",code:"FJ",dial:"+679",len:7},
    {name:"Finland",code:"FI",dial:"+358",len:9},{name:"France",code:"FR",dial:"+33",len:9},
    {name:"Gabon",code:"GA",dial:"+241",len:8},{name:"Gambia",code:"GM",dial:"+220",len:7},
    {name:"Georgia",code:"GE",dial:"+995",len:9},{name:"Germany",code:"DE",dial:"+49",len:10},
    {name:"Ghana",code:"GH",dial:"+233",len:9},{name:"Greece",code:"GR",dial:"+30",len:10},
    {name:"Grenada",code:"GD",dial:"+1",len:10},{name:"Guatemala",code:"GT",dial:"+502",len:8},
    {name:"Guinea",code:"GN",dial:"+224",len:9},{name:"Guinea-Bissau",code:"GW",dial:"+245",len:7},
    {name:"Guyana",code:"GY",dial:"+592",len:7},{name:"Haiti",code:"HT",dial:"+509",len:8},
    {name:"Honduras",code:"HN",dial:"+504",len:8},{name:"Hungary",code:"HU",dial:"+36",len:9},
    {name:"Iceland",code:"IS",dial:"+354",len:7},{name:"India",code:"IN",dial:"+91",len:10},
    {name:"Indonesia",code:"ID",dial:"+62",len:12},{name:"Iran",code:"IR",dial:"+98",len:10},
    {name:"Iraq",code:"IQ",dial:"+964",len:10},{name:"Ireland",code:"IE",dial:"+353",len:9},
    {name:"Israel",code:"IL",dial:"+972",len:9},{name:"Italy",code:"IT",dial:"+39",len:10},
    {name:"Ivory Coast",code:"CI",dial:"+225",len:10},{name:"Jamaica",code:"JM",dial:"+1",len:10},
    {name:"Japan",code:"JP",dial:"+81",len:10},{name:"Jordan",code:"JO",dial:"+962",len:9},
    {name:"Kazakhstan",code:"KZ",dial:"+7",len:10},{name:"Kenya",code:"KE",dial:"+254",len:9},
    {name:"Kiribati",code:"KI",dial:"+686",len:8},{name:"Kuwait",code:"KW",dial:"+965",len:8},
    {name:"Kyrgyzstan",code:"KG",dial:"+996",len:9},{name:"Laos",code:"LA",dial:"+856",len:9},
    {name:"Latvia",code:"LV",dial:"+371",len:8},{name:"Lebanon",code:"LB",dial:"+961",len:8},
    {name:"Lesotho",code:"LS",dial:"+266",len:8},{name:"Liberia",code:"LR",dial:"+231",len:8},
    {name:"Libya",code:"LY",dial:"+218",len:9},{name:"Liechtenstein",code:"LI",dial:"+423",len:7},
    {name:"Lithuania",code:"LT",dial:"+370",len:8},{name:"Luxembourg",code:"LU",dial:"+352",len:9},
    {name:"Madagascar",code:"MG",dial:"+261",len:9},{name:"Malawi",code:"MW",dial:"+265",len:9},
    {name:"Malaysia",code:"MY",dial:"+60",len:9},{name:"Maldives",code:"MV",dial:"+960",len:7},
    {name:"Mali",code:"ML",dial:"+223",len:8},{name:"Malta",code:"MT",dial:"+356",len:8},
    {name:"Marshall Islands",code:"MH",dial:"+692",len:7},{name:"Mauritania",code:"MR",dial:"+222",len:8},
    {name:"Mauritius",code:"MU",dial:"+230",len:8},{name:"Mexico",code:"MX",dial:"+52",len:10},
    {name:"Micronesia",code:"FM",dial:"+691",len:7},{name:"Moldova",code:"MD",dial:"+373",len:8},
    {name:"Monaco",code:"MC",dial:"+377",len:8},{name:"Mongolia",code:"MN",dial:"+976",len:8},
    {name:"Montenegro",code:"ME",dial:"+382",len:8},{name:"Morocco",code:"MA",dial:"+212",len:9},
    {name:"Mozambique",code:"MZ",dial:"+258",len:9},{name:"Myanmar",code:"MM",dial:"+95",len:9},
    {name:"Namibia",code:"NA",dial:"+264",len:9},{name:"Nauru",code:"NR",dial:"+674",len:7},
    {name:"Nepal",code:"NP",dial:"+977",len:10},{name:"Netherlands",code:"NL",dial:"+31",len:9},
    {name:"New Zealand",code:"NZ",dial:"+64",len:9},{name:"Nicaragua",code:"NI",dial:"+505",len:8},
    {name:"Niger",code:"NE",dial:"+227",len:8},{name:"Nigeria",code:"NG",dial:"+234",len:10},
    {name:"North Korea",code:"KP",dial:"+850",len:9},{name:"North Macedonia",code:"MK",dial:"+389",len:8},
    {name:"Norway",code:"NO",dial:"+47",len:8},{name:"Oman",code:"OM",dial:"+968",len:8},
    {name:"Pakistan",code:"PK",dial:"+92",len:10},{name:"Palau",code:"PW",dial:"+680",len:7},
    {name:"Palestine",code:"PS",dial:"+970",len:9},{name:"Panama",code:"PA",dial:"+507",len:8},
    {name:"Papua New Guinea",code:"PG",dial:"+675",len:8},{name:"Paraguay",code:"PY",dial:"+595",len:9},
    {name:"Peru",code:"PE",dial:"+51",len:9},{name:"Philippines",code:"PH",dial:"+63",len:10},
    {name:"Poland",code:"PL",dial:"+48",len:9},{name:"Portugal",code:"PT",dial:"+351",len:9},
    {name:"Qatar",code:"QA",dial:"+974",len:8},{name:"Romania",code:"RO",dial:"+40",len:9},
    {name:"Russia",code:"RU",dial:"+7",len:10},{name:"Rwanda",code:"RW",dial:"+250",len:9},
    {name:"Saint Kitts & Nevis",code:"KN",dial:"+1",len:10},{name:"Saint Lucia",code:"LC",dial:"+1",len:10},
    {name:"Saint Vincent",code:"VC",dial:"+1",len:10},{name:"Samoa",code:"WS",dial:"+685",len:7},
    {name:"San Marino",code:"SM",dial:"+378",len:9},{name:"Sao Tome & Principe",code:"ST",dial:"+239",len:7},
    {name:"Saudi Arabia",code:"SA",dial:"+966",len:9},{name:"Senegal",code:"SN",dial:"+221",len:9},
    {name:"Serbia",code:"RS",dial:"+381",len:9},{name:"Seychelles",code:"SC",dial:"+248",len:7},
    {name:"Sierra Leone",code:"SL",dial:"+232",len:8},{name:"Singapore",code:"SG",dial:"+65",len:8},
    {name:"Slovakia",code:"SK",dial:"+421",len:9},{name:"Slovenia",code:"SI",dial:"+386",len:8},
    {name:"Solomon Islands",code:"SB",dial:"+677",len:7},{name:"Somalia",code:"SO",dial:"+252",len:8},
    {name:"South Africa",code:"ZA",dial:"+27",len:9},{name:"South Korea",code:"KR",dial:"+82",len:10},
    {name:"South Sudan",code:"SS",dial:"+211",len:9},{name:"Spain",code:"ES",dial:"+34",len:9},
    {name:"Sri Lanka",code:"LK",dial:"+94",len:9},{name:"Sudan",code:"SD",dial:"+249",len:9},
    {name:"Suriname",code:"SR",dial:"+597",len:7},{name:"Sweden",code:"SE",dial:"+46",len:9},
    {name:"Switzerland",code:"CH",dial:"+41",len:9},{name:"Syria",code:"SY",dial:"+963",len:9},
    {name:"Taiwan",code:"TW",dial:"+886",len:9},{name:"Tajikistan",code:"TJ",dial:"+992",len:9},
    {name:"Tanzania",code:"TZ",dial:"+255",len:9},{name:"Thailand",code:"TH",dial:"+66",len:9},
    {name:"Timor-Leste",code:"TL",dial:"+670",len:8},{name:"Togo",code:"TG",dial:"+228",len:8},
    {name:"Tonga",code:"TO",dial:"+676",len:7},{name:"Trinidad & Tobago",code:"TT",dial:"+1",len:10},
    {name:"Tunisia",code:"TN",dial:"+216",len:8},{name:"Turkey",code:"TR",dial:"+90",len:10},
    {name:"Turkmenistan",code:"TM",dial:"+993",len:8},{name:"Tuvalu",code:"TV",dial:"+688",len:6},
    {name:"Uganda",code:"UG",dial:"+256",len:9},{name:"Ukraine",code:"UA",dial:"+380",len:9},
    {name:"United Arab Emirates",code:"AE",dial:"+971",len:9},{name:"United Kingdom",code:"GB",dial:"+44",len:10},
    {name:"United States",code:"US",dial:"+1",len:10},{name:"Uruguay",code:"UY",dial:"+598",len:8},
    {name:"Uzbekistan",code:"UZ",dial:"+998",len:9},{name:"Vanuatu",code:"VU",dial:"+678",len:7},
    {name:"Vatican City",code:"VA",dial:"+379",len:9},{name:"Venezuela",code:"VE",dial:"+58",len:10},
    {name:"Vietnam",code:"VN",dial:"+84",len:9},{name:"Yemen",code:"YE",dial:"+967",len:9},
    {name:"Zambia",code:"ZM",dial:"+260",len:9},{name:"Zimbabwe",code:"ZW",dial:"+263",len:9}
  ];

  var sortedCountries = COUNTRIES.slice().sort(function(a, b) {
    return a.name.localeCompare(b.name);
  });

  var currentCountry = sortedCountries.find(function(c) { return c.code === 'IN'; }) || sortedCountries[0];

  var modalOverlay, modalWrap, form, nameInput, phoneInput, emailInput, submitBtn, btnText, globalErr;
  var nameField, phoneField, emailField, nameErr, phoneErr, emailErr;
  var ccTrigger, ccDisplay, ccPanel, ccSearch, ccList, ccVal;
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
        '<div class="lf-wrap abha-modal-wrap" id="abhaModalWrap" role="dialog" aria-modal="true" aria-labelledby="abhaHeading" aria-describedby="abhaSubheading">' +
          '<div class="lf-drag-handle abha-drag-handle"></div>' +
          '<button type="button" class="lf-modal-close-icon abha-close-btn" id="abhaCloseBtn" aria-label="Close Talk to Abha modal">' +
            '<svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">' +
              '<path d="M1 1l12 12M13 1L1 13"/>' +
            '</svg>' +
          '</button>' +
          '<div class="abha-modal-header">' +
            '<div class="abha-header-avatar-wrap">' +
              '<svg class="abha-header-rays" width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true">' +
                '<path d="M13 20L8 16" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
                '<path d="M16 14L11 8" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
                '<path d="M23 9L20 3" stroke="#be7555" stroke-width="3" stroke-linecap="round"/>' +
              '</svg>' +
              '<img src="' + avatarUrl + '" alt="Abha - Home Buying Advisor" class="abha-header-avatar-img" width="76" height="76">' +
              '<span class="abha-header-status-dot" aria-label="Abha is online"></span>' +
            '</div>' +
            '<div class="abha-header-text">' +
              '<h2 class="abha-modal-title" id="abhaHeading">Talk to Abha</h2>' +
              '<p class="abha-modal-subtitle" id="abhaSubheading">We need some details to get started.</p>' +
            '</div>' +
          '</div>' +
          '<form class="lf-form" id="abhaForm" novalidate>' +
            '<div class="lf-field" id="abhaNameField">' +
              '<div class="lf-input-box">' +
                '<label class="lf-label" for="abhaName">Full name<span class="lf-req" aria-hidden="true">*</span></label>' +
                '<input class="lf-input lf-focusable" type="text" id="abhaName" name="name" autocomplete="name" enterkeyhint="next" aria-required="true" tabindex="0" aria-invalid="false" maxlength="60" aria-describedby="abhaNameErr">' +
                '<span class="lf-valid-icon" aria-hidden="true"><svg viewBox="0 0 14 14" fill="none"><path stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" d="M1 7l4 4 8-8"/></svg></span>' +
                '<button type="button" class="lf-clear-btn lf-focusable" id="abhaNameClearBtn" aria-label="Clear name field" tabindex="-1"><svg viewBox="0 0 10 10" fill="none"><path stroke="currentColor" stroke-width="1.2" stroke-linecap="round" d="M1 1l8 8M9 1L1 9"/></svg></button>' +
              '</div>' +
              '<div class="lf-err" id="abhaNameErr" role="alert"></div>' +
            '</div>' +
            '<div class="lf-field lf-field-phone" id="abhaPhoneField">' +
              '<div class="lf-input-box">' +
                '<label class="lf-label" id="abhaPhoneLbl" for="abhaPhone">Mobile<span class="lf-req" aria-hidden="true">*</span></label>' +
                '<div class="lf-phone-row">' +
                  '<button type="button" class="lf-cc-trigger lf-focusable" id="abhaCcTrigger" aria-haspopup="listbox" aria-expanded="false" aria-controls="abhaCcPanel" aria-label="Select country dial code" tabindex="0">' +
                    '<span id="abhaCcDisplay">+91</span>' +
                    '<svg class="lf-cc-arrow" viewBox="0 0 8 5" fill="none"><path stroke="currentColor" stroke-width="1.2" stroke-linecap="round" d="M1 1l3 3 3-3"/></svg>' +
                  '</button>' +
                  '<div class="lf-cc-panel" id="abhaCcPanel" role="listbox" aria-labelledby="abhaPhoneLbl">' +
                    '<input class="lf-cc-search lf-focusable" type="text" id="abhaCcSearch" role="combobox" aria-expanded="true" aria-autocomplete="list" aria-controls="abhaCcList" placeholder="Search country..." autocomplete="off" aria-label="Search countries by name or code" tabindex="-1">' +
                    '<div class="lf-cc-list" id="abhaCcList"></div>' +
                  '</div>' +
                  '<input type="hidden" id="abhaCcVal" name="country_code" value="+91">' +
                  '<div class="lf-divider"></div>' +
                  '<input class="lf-input lf-focusable" type="tel" id="abhaPhone" name="phone" inputmode="numeric" autocomplete="tel" enterkeyhint="next" aria-required="true" tabindex="0" aria-invalid="false" maxlength="15" aria-describedby="abhaPhoneErr">' +
                  '<span class="lf-valid-icon" aria-hidden="true"><svg viewBox="0 0 14 14" fill="none"><path stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" d="M1 7l4 4 8-8"/></svg></span>' +
                  '<button type="button" class="lf-clear-btn lf-focusable" id="abhaPhoneClearBtn" aria-label="Clear mobile number field" tabindex="-1"><svg viewBox="0 0 10 10" fill="none"><path stroke="currentColor" stroke-width="1.2" stroke-linecap="round" d="M1 1l8 8M9 1L1 9"/></svg></button>' +
                '</div>' +
              '</div>' +
              '<div class="lf-err" id="abhaPhoneErr" role="alert"></div>' +
            '</div>' +
            '<div class="lf-field" id="abhaEmailField">' +
              '<div class="lf-input-box">' +
                '<label class="lf-label" for="abhaEmail">Email<span class="lf-req" aria-hidden="true">*</span></label>' +
                '<input class="lf-input lf-focusable" type="email" id="abhaEmail" name="email" autocomplete="email" enterkeyhint="done" aria-required="true" tabindex="0" aria-invalid="false" maxlength="120" aria-describedby="abhaEmailErr">' +
                '<span class="lf-valid-icon" aria-hidden="true"><svg viewBox="0 0 14 14" fill="none"><path stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" d="M1 7l4 4 8-8"/></svg></span>' +
                '<button type="button" class="lf-clear-btn lf-focusable" id="abhaEmailClearBtn" aria-label="Clear email field" tabindex="-1"><svg viewBox="0 0 10 10" fill="none"><path stroke="currentColor" stroke-width="1.2" stroke-linecap="round" d="M1 1l8 8M9 1L1 9"/></svg></button>' +
              '</div>' +
              '<div class="lf-err" id="abhaEmailErr" role="alert"></div>' +
            '</div>' +
            '<div class="lf-submit-wrap">' +
              '<button type="submit" class="lf-btn lf-focusable advisor-talk-btn" id="abhaSubmitBtn" tabindex="0" aria-label="Start chat with Abha">' +
                '<div class="lf-spinner"></div>' +
                '<span id="abhaBtnText">Start Chat</span>' +
                '<svg class="advisor-talk-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
                  '<line x1="5" y1="12" x2="19" y2="12"></line>' +
                  '<polyline points="12 5 19 12 12 19"></polyline>' +
                '</svg>' +
              '</button>' +
              '<p class="lf-privacy-consent">' +
                'By submitting your details, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.' +
              '</p>' +
              '<p class="lf-global-err" id="abhaGlobalErr" role="alert" aria-live="assertive" aria-atomic="true">' +
                'Connection issue. Your details are safely held. Please click Submit once more to retry or reach out to support.' +
              '</p>' +
            '</div>' +
          '</form>' +
        '</div>' +
      '</div>';

    var container = document.createElement('div');
    container.innerHTML = html;
    document.body.appendChild(container.firstElementChild);
  }

  function checkValueState(inputEl) {
    if (!inputEl) return;
    var field = inputEl.closest('.lf-field');
    if (!field) return;
    if (inputEl.value && inputEl.value.trim() !== '') {
      field.classList.add('lf-has-value');
      field.classList.add('lf-has-input-text');
    } else {
      field.classList.remove('lf-has-value');
      field.classList.remove('lf-has-input-text');
    }
  }

  function setFieldError(fieldEl, errEl, msg) {
    if (!fieldEl) return;
    if (msg) {
      fieldEl.classList.add('lf-has-error');
      fieldEl.classList.remove('lf-is-valid');
      if (errEl) {
        errEl.textContent = msg;
      }
      var inp = fieldEl.querySelector('.lf-input');
      if (inp) inp.setAttribute('aria-invalid', 'true');
    } else {
      fieldEl.classList.remove('lf-has-error');
      fieldEl.classList.add('lf-is-valid');
      if (errEl) {
        errEl.textContent = '';
      }
      var inp2 = fieldEl.querySelector('.lf-input');
      if (inp2) inp2.setAttribute('aria-invalid', 'false');
    }
  }

  function clearFieldValidation(fieldEl, errEl) {
    if (!fieldEl) return;
    fieldEl.classList.remove('lf-has-error', 'lf-is-valid');
    if (errEl) errEl.textContent = '';
  }

  function validateName() {
    if (!nameInput) return true;
    var val = nameInput.value.trim();
    if (!val) {
      setFieldError(nameField, nameErr, 'Name is required');
      return false;
    }
    if (val.length < 2) {
      setFieldError(nameField, nameErr, 'Enter a valid name (at least 2 characters)');
      return false;
    }
    setFieldError(nameField, nameErr, '');
    return true;
  }

  function validatePhone() {
    if (!phoneInput) return true;
    var val = phoneInput.value.trim().replace(/[\s\-()]/g, '');
    if (!val) {
      setFieldError(phoneField, phoneErr, 'Mobile number is required');
      return false;
    }
    var digitsOnly = val.replace(/\D/g, '');
    var expLen = (currentCountry && currentCountry.len) ? currentCountry.len : 10;
    
    if (digitsOnly.length < (expLen - 1) || digitsOnly.length > (expLen + 2)) {
      setFieldError(phoneField, phoneErr, 'Enter a valid ' + expLen + '-digit mobile number');
      return false;
    }
    setFieldError(phoneField, phoneErr, '');
    return true;
  }

  function validateEmail() {
    if (!emailInput) return true;
    var val = emailInput.value.trim();
    if (!val) {
      setFieldError(emailField, emailErr, 'Email is required');
      return false;
    }
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    if (!emailRegex.test(val)) {
      setFieldError(emailField, emailErr, 'Enter a valid email address');
      return false;
    }
    setFieldError(emailField, emailErr, '');
    return true;
  }

  function renderCountryList(filterText) {
    if (!ccList) return;
    var query = (filterText || '').toLowerCase().trim();
    var matches = sortedCountries.filter(function(c) {
      return c.name.toLowerCase().indexOf(query) !== -1 ||
             c.dial.indexOf(query) !== -1 ||
             c.code.toLowerCase().indexOf(query) !== -1;
    });

    ccList.innerHTML = '';
    matches.forEach(function(c) {
      var item = document.createElement('div');
      item.className = 'lf-cc-opt';
      item.setAttribute('role', 'option');
      item.setAttribute('data-dial', c.dial);
      item.setAttribute('data-code', c.code);
      item.innerHTML = '<span class="lf-cc-opt-dial">' + c.dial + '</span><span class="lf-cc-opt-name">' + c.name + '</span>';
      item.addEventListener('click', function() {
        selectCountry(c);
      });
      ccList.appendChild(item);
    });
  }

  function selectCountry(country) {
    currentCountry = country;
    if (ccDisplay) ccDisplay.textContent = country.dial;
    if (ccVal) ccVal.value = country.dial;
    closeCcPanel();
    if (phoneInput) {
      phoneInput.focus();
      validatePhone();
    }
  }

  function openCcPanel() {
    if (!ccPanel) return;
    ccPanel.classList.add('lf-cc-open');
    if (ccTrigger) ccTrigger.setAttribute('aria-expanded', 'true');
    renderCountryList('');
    if (ccSearch) {
      ccSearch.value = '';
      setTimeout(function() { ccSearch.focus(); }, 100);
    }
  }

  function closeCcPanel() {
    if (!ccPanel) return;
    ccPanel.classList.remove('lf-cc-open');
    if (ccTrigger) ccTrigger.setAttribute('aria-expanded', 'false');
  }

  async function sendToApi(payload) {
    // 1. Custom function hook
    if (typeof window.sendAbhaData === 'function') {
      return await window.sendAbhaData(payload);
    }

    // 2. Custom API URL hook
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
      { name: 'mobilephone', value: payload.phone },
      { name: 'email', value: payload.email }
    ];

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
      submitBtn.classList.add('lf-loading');
    }
    if (btnText) btnText.textContent = 'Connecting...';
    if (globalErr) {
      globalErr.classList.remove('lf-show');
      globalErr.textContent = '';
    }

    var tracking = getTrackingPayload();
    var dial = (ccVal ? ccVal.value : '+91') || '+91';
    var rawDigits = phoneInput.value.trim().replace(/\D/g, '');
    var formattedPhone = dial + rawDigits;

    var payload = {
      name: nameInput.value.trim(),
      phone: formattedPhone,
      email: emailInput.value.trim().toLowerCase(),
      country_code: dial,
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
        submitBtn.classList.remove('lf-loading');
      }
      if (btnText) btnText.textContent = 'Start Chat';
      if (globalErr) {
        globalErr.classList.add('lf-show');
        globalErr.textContent = 'Connection issue. Your details are safely held. Please click Submit once more to retry.';
      }
      console.error('[Abha Form API Submission Failed]', err);
    }
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
    btnText      = document.getElementById('abhaBtnText');
    globalErr    = document.getElementById('abhaGlobalErr');

    nameField    = document.getElementById('abhaNameField');
    phoneField   = document.getElementById('abhaPhoneField');
    emailField   = document.getElementById('abhaEmailField');

    nameErr      = document.getElementById('abhaNameErr');
    phoneErr     = document.getElementById('abhaPhoneErr');
    emailErr     = document.getElementById('abhaEmailErr');

    ccTrigger    = document.getElementById('abhaCcTrigger');
    ccDisplay    = document.getElementById('abhaCcDisplay');
    ccPanel      = document.getElementById('abhaCcPanel');
    ccSearch     = document.getElementById('abhaCcSearch');
    ccList       = document.getElementById('abhaCcList');
    ccVal        = document.getElementById('abhaCcVal');

    var backdrop = document.getElementById('abhaModalBackdrop');
    if (backdrop) backdrop.addEventListener('click', closeModal);

    var closeBtn = document.getElementById('abhaCloseBtn');
    if (closeBtn) closeBtn.addEventListener('click', closeModal);

    if (form) form.addEventListener('submit', handleSubmit);

    // Country Code dropdown events
    if (ccTrigger) {
      ccTrigger.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        if (ccPanel && ccPanel.classList.contains('lf-cc-open')) {
          closeCcPanel();
        } else {
          openCcPanel();
        }
      });
    }

    if (ccSearch) {
      ccSearch.addEventListener('input', function() {
        renderCountryList(ccSearch.value);
      });
      ccSearch.addEventListener('click', function(e) {
        e.stopPropagation();
      });
    }

    document.addEventListener('click', function(e) {
      if (ccPanel && ccPanel.classList.contains('lf-cc-open')) {
        if (!ccPanel.contains(e.target) && (!ccTrigger || !ccTrigger.contains(e.target))) {
          closeCcPanel();
        }
      }
    });

    // Floating labels & clear buttons
    [
      { input: nameInput, field: nameField, clearId: 'abhaNameClearBtn', validator: validateName },
      { input: phoneInput, field: phoneField, clearId: 'abhaPhoneClearBtn', validator: validatePhone },
      { input: emailInput, field: emailField, clearId: 'abhaEmailClearBtn', validator: validateEmail }
    ].forEach(function(item) {
      if (!item.input || !item.field) return;

      item.input.addEventListener('focus', function() {
        item.field.classList.add('lf-focused');
      });

      item.input.addEventListener('blur', function() {
        item.field.classList.remove('lf-focused');
        checkValueState(item.input);
        if (item.input.value.trim() !== '') {
          item.validator();
        }
      });

      item.input.addEventListener('input', function() {
        checkValueState(item.input);
        if (item.field.classList.contains('lf-has-error')) {
          item.validator();
        }
      });

      var clearBtn = document.getElementById(item.clearId);
      if (clearBtn) {
        clearBtn.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          item.input.value = '';
          checkValueState(item.input);
          clearFieldValidation(item.field, (item.field === nameField ? nameErr : (item.field === phoneField ? phoneErr : emailErr)));
          item.input.focus();
        });
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('abha-modal-open')) {
        if (ccPanel && ccPanel.classList.contains('lf-cc-open')) {
          closeCcPanel();
        } else {
          closeModal();
        }
      }
    });
  }

  function openModal() {
    if (!modalOverlay) initElements();
    if (!modalOverlay) return;

    modalOverlay.classList.add('abha-modal-open');
    modalOverlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Reset error & valid state
    [nameField, phoneField, emailField].forEach(function(f) {
      if (f) f.classList.remove('lf-has-error', 'lf-is-valid');
    });
    [nameErr, phoneErr, emailErr].forEach(function(el) {
      if (el) el.textContent = '';
    });
    if (globalErr) {
      globalErr.classList.remove('lf-show');
      globalErr.textContent = '';
    }

    // Check prefilled values
    [nameInput, phoneInput, emailInput].forEach(function(el) {
      if (el) checkValueState(el);
    });

    setTimeout(function() {
      if (nameInput) nameInput.focus();
    }, 200);
  }

  function closeModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('abha-modal-open');
    modalOverlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    closeCcPanel();
  }

  // Public API
  window.openAbhaModal = openModal;
  window.closeAbhaModal = closeModal;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initElements);
  } else {
    initElements();
  }
})();
