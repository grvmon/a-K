import sys
import re

snippet = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400&display=swap" rel="stylesheet">

<style>
/* Scoped styles - will not affect the rest of your WordPress theme */
.lf-modal-overlay,
.lf-modal-overlay * { box-sizing: border-box; margin: 0; padding: 0; }

/* ── MODAL OVERLAY ── */
.lf-modal-overlay {
  position: fixed; inset: 0;
  background: rgba(15,15,15,0.6);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  z-index: 999999 !important;
  display: flex; align-items: center; justify-content: center;
  padding: 20px; opacity: 0; visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}
.lf-modal-overlay.lf-modal-open { opacity: 1; visibility: visible; }

.lf-wrap {
  --lf-font-sans: 'DM Sans', sans-serif;
  --lf-font-mono: 'DM Mono', monospace;
  --lf-ink:   #0f0f0f;
  --lf-muted: #666;
  --lf-line:  #dcdcdc;
  --lf-line-focus: #0f0f0f;
  --lf-err:   #c0392b;
  --lf-ok:    #2e7d52;
  --lf-bg-surface: #ffffff;

  position: relative; z-index: 10; width: 100%; max-width: 440px;
  background: var(--lf-bg-surface); border-radius: 8px;
  padding: 44px 40px 40px 40px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.2);
  max-height: calc(100vh - 40px); max-height: calc(100dvh - 40px); 
  overflow-y: auto;
  overscroll-behavior-y: none; /* Android Fix: Prevents Chrome pull-to-refresh */
  transform: translateY(24px);
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
}
@media (max-width: 480px) {
  .lf-wrap { padding: 32px 20px; }
}
.lf-modal-overlay.lf-modal-open .lf-wrap { transform: translateY(0); }

@media (prefers-reduced-motion: reduce) {
  .lf-modal-overlay, .lf-wrap, .lf-label {
    transition: none !important; transform: none !important; backdrop-filter: none !important;
  }
}

.lf-modal-close-icon {
  position: absolute; top: 18px; right: 18px;
  background: none; border: none; outline: none; cursor: pointer;
  color: var(--lf-muted); padding: 8px;
  display: flex; align-items: center; justify-content: center;
  transition: color 0.15s, transform 0.15s; z-index: 10;
}
.lf-modal-close-icon svg { width: 13px; height: 13px; }
.lf-modal-close-icon:hover { color: var(--lf-ink); transform: scale(1.05); }

.lf-header { margin-bottom: 26px; padding-right: 20px; }
.lf-main-heading { font-size: 24px; font-weight: 500; margin-bottom: 6px; color: var(--lf-ink); }
.lf-sub-heading { font-size: 14px; color: var(--lf-muted); line-height: 1.4; }

.lf-form { display: flex; flex-direction: column; gap: 20px; }
.lf-form .lf-field { position: relative; width: 100%; }

.lf-input-box {
  position: relative; width: 100%; height: 56px; min-height: 56px;
  border: 1px solid var(--lf-line); border-radius: 6px;
  background: var(--lf-bg-surface);
  display: flex; align-items: center; padding: 0 16px;
  transition: border-color .2s, background-color .2s;
}
.lf-field.lf-focused .lf-input-box { border-color: var(--lf-line-focus); }
.lf-field.lf-has-error .lf-input-box { border-color: var(--lf-err); background: #fffcfb; }
.lf-field.lf-has-error.lf-focused .lf-input-box { border-color: var(--lf-line-focus); background: var(--lf-bg-surface); }
.lf-field.lf-is-valid .lf-input-box { border-color: var(--lf-ok); }

.lf-wrap .lf-label {
  position: absolute !important; left: 16px !important; top: 50% !important;
  transform: translateY(-50%) !important; font-size: 14px !important;
  color: var(--lf-muted) !important;
  transition: transform .2s ease, top .2s ease, font-size .2s ease, color .2s ease, background-color .2s ease !important;
  font-family: var(--lf-font-sans) !important; pointer-events: none;
  z-index: 5 !important; background: transparent !important; padding: 0 4px !important;
}
.lf-field.lf-focused .lf-label,
.lf-field.lf-has-value .lf-label,
.lf-field.lf-autofilled .lf-label {
  top: 0 !important; transform: translateY(-50%) !important;
  font-size: 11px !important; font-weight: 500 !important;
  text-transform: uppercase !important;
  background-color: var(--lf-bg-surface) !important; left: 12px !important;
}
.lf-field-phone .lf-label { left: 82px !important; }
.lf-field-phone.lf-focused .lf-label,
.lf-field-phone.lf-has-value .lf-label,
.lf-field-phone.lf-autofilled .lf-label { left: 12px !important; }

.lf-req { color: var(--lf-err); margin-left: 3px; }

.lf-wrap input.lf-input {
  flex: 1 !important; width: 100% !important;
  border: none !important; background: transparent !important; outline: none !important;
  font-family: var(--lf-font-mono) !important; font-size: 16px !important;
  color: var(--lf-ink) !important; padding: 14px 0 0 0 !important; height: 54px !important;
}
.lf-input-phone-stretch { flex: 1 !important; }

.lf-clear-btn {
  display: inline-flex; align-items: center; justify-content: center;
  background: none; border: none; cursor: pointer; color: #bbb;
  padding: 6px; margin-left: 8px; flex-shrink: 0; z-index: 6;
  opacity: 0; visibility: hidden;
  transition: opacity 0.15s, color 0.15s; height: 32px; width: 32px;
}
.lf-clear-btn svg { width: 10px; height: 10px; pointer-events: none; }
.lf-clear-btn:hover { color: var(--lf-ink); }
.lf-field.lf-has-input-text .lf-clear-btn { opacity: 1; visibility: visible; }

.lf-valid-icon {
  display: none; align-items: center; justify-content: center;
  width: 18px; height: 18px; flex-shrink: 0; margin-left: 6px; color: var(--lf-ok);
}
.lf-valid-icon svg { width: 14px; height: 14px; }
.lf-field.lf-is-valid:not(.lf-has-input-text) .lf-valid-icon { display: inline-flex; }

input:-webkit-autofill { animation-name: lfAutofillDetected; animation-duration: 0.01s; }
@keyframes lfAutofillDetected { from {} to {} }

.lf-phone-row { display: flex; align-items: center; width: 100%; position: relative; height: 100%; }

.lf-cc-trigger {
  display: inline-flex !important; align-items: center !important;
  justify-content: space-between !important; gap: 4px !important;
  cursor: pointer !important; padding: 12px 0 0 0 !important;
  background: none !important; border: none !important;
  font-family: var(--lf-font-mono) !important; font-size: 16px !important;
  color: var(--lf-ink) !important; height: 54px !important; width: 54px !important;
  flex-shrink: 0 !important;
}
.lf-cc-arrow { width: 8px; height: 5px; color: var(--lf-muted); flex-shrink: 0; }

/* ── DESKTOP DROPDOWN ── */
.lf-cc-panel {
  display: none;
  position: absolute;
  top: calc(100% + 8px);
  left: -16px;
  z-index: 9999999 !important;
  width: calc(100% + 32px);
  background: #fff;
  border: 1px solid #e2e2e2;
  border-radius: 6px;
  box-shadow: 0 10px 30px rgba(0,0,0,.12);
  max-height: 260px;
  overflow: hidden;
  flex-direction: column;
}
.lf-cc-panel.lf-cc-open { display: flex; }

/* ── WP-SAFE MOBILE BOTTOM SHEET ── */
@media (max-width: 600px) {
  .lf-cc-backdrop {
    display: none;
    position: absolute !important;
    inset: 0 !important;
    background: rgba(0,0,0,0.6) !important;
    z-index: 90 !important;
  }
  .lf-cc-backdrop.lf-cc-open { display: block !important; }

  .lf-cc-panel {
    display: flex !important;
    visibility: hidden;
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    top: auto !important;
    width: 100% !important;
    max-height: 60vh !important;
    border-radius: 16px 16px 0 0 !important;
    border: none !important;
    box-shadow: 0 -10px 32px rgba(0,0,0,0.2) !important;
    z-index: 100 !important;
    transform: translateY(100%);
    transition: transform 0.3s cubic-bezier(0.4,0,0.2,1), visibility 0s linear 0.3s;
    padding-bottom: env(safe-area-inset-bottom);
    margin: 0 !important;
    overscroll-behavior-y: none; /* Android Fix: Prevents Chrome pull-to-refresh */
  }
  
  .lf-cc-panel.lf-cc-open {
    visibility: visible;
    transform: translateY(0) !important;
    transition: transform 0.3s cubic-bezier(0.4,0,0.2,1), visibility 0s linear 0s;
  }
  
  .lf-cc-panel::before {
    content: '';
    display: block;
    width: 36px; height: 4px;
    background: #ccc;
    border-radius: 2px;
    margin: 12px auto 6px;
    flex-shrink: 0;
  }
}

.lf-cc-search {
  padding: 12px 14px;
  border: none !important;
  border-bottom: 1px solid #eee !important;
  width: 100%; outline: none !important;
  font-family: var(--lf-font-sans, 'DM Sans', sans-serif) !important;
  font-size: 16px !important;
  flex-shrink: 0;
}
.lf-cc-list { overflow-y: auto; flex: 1; -webkit-overflow-scrolling: touch; }

.lf-cc-opt {
  padding: 11px 14px;
  font-family: var(--lf-font-sans, 'DM Sans', sans-serif) !important;
  font-size: 13px; cursor: pointer; display: flex; gap: 10px; color: var(--lf-ink);
  user-select: none; -webkit-user-select: none;
}
.lf-cc-opt:hover, .lf-cc-opt.lf-keyboard-active { background: #f7f7f7; outline: none; }
.lf-cc-trigger, .lf-cc-opt, .lf-btn, .lf-modal-close-icon { touch-action: manipulation; }
.lf-cc-opt-dial { font-family: var(--lf-font-mono, 'DM Mono', monospace) !important; color: var(--lf-muted); min-width: 44px; }

@media (max-width: 600px) {
  .lf-cc-opt { padding: 14px 16px; font-size: 15px; }
}

.lf-divider { width: 1px; height: 18px; background: var(--lf-line); margin: 12px 14px 0 8px; flex-shrink: 0; }

.lf-err {
  font-size: 11px; color: var(--lf-err); font-weight: 500;
  visibility: hidden; height: 0; overflow: hidden;
  padding: 0 4px; font-family: var(--lf-font-sans);
}
.lf-has-error .lf-err { visibility: visible; height: auto; padding: 6px 4px 0; }

.lf-submit-wrap { margin-top: 10px; }

.lf-btn {
  width: 100%; height: 54px;
  border: none !important; border-radius: 0px !important;
  background: #cfa847 !important; color: #1a1a1a !important;
  font-family: var(--lf-font-sans) !important; font-size: 13px !important;
  font-weight: 500 !important; letter-spacing: .16em !important;
  text-transform: uppercase !important; cursor: pointer !important;
  position: relative; overflow: hidden; box-shadow: none !important;
  transition: opacity .2s ease !important;
  display: flex; align-items: center; justify-content: center; gap: 10px;
}
.lf-btn:hover { opacity: 0.9 !important; }
.lf-btn:disabled { opacity: 0.6 !important; cursor: not-allowed !important; }
.lf-btn span { position: relative; z-index: 1; }

.lf-spinner {
  display: none; width: 16px; height: 16px;
  border: 2px solid rgba(26,26,26,0.3); border-top-color: #1a1a1a;
  border-radius: 50%; animation: lfSpin 0.7s linear infinite; flex-shrink: 0;
}
.lf-btn.lf-loading .lf-spinner { display: block; }
@keyframes lfSpin { to { transform: rotate(360deg); } }

.lf-global-err {
  font-size: 12px; color: var(--lf-err); margin-top: 14px;
  text-align: center; display: none;
  font-family: var(--lf-font-sans); line-height: 1.4;
}
.lf-global-err.lf-show { display: block; }
.lf-hp { position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }

.lf-success-canvas {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 40px 10px; text-align: center; font-family: 'DM Sans', sans-serif;
}
.lf-success-circle {
  width: 64px; height: 64px; border-radius: 50%; background: #f4ebe1;
  display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #cfa847;
}
.lf-success-circle svg { width: 28px; height: 28px; stroke-dasharray: 40; stroke-dashoffset: 40; animation: lfStrokeCheck 0.4s cubic-bezier(0.4,0,0.2,1) forwards 0.15s; }
@keyframes lfStrokeCheck { to { stroke-dashoffset: 0; } }
</style>

<div class="lf-modal-overlay" id="lfModalOverlay">
  <div class="lf-cc-backdrop" id="lfCcBackdrop"></div>

  <div class="lf-wrap" id="lfWrap" role="dialog" aria-modal="true" aria-labelledby="lfMainHeading" aria-describedby="lfSubHeading">

    <button type="button" class="lf-modal-close-icon lf-focusable" id="lfModalClose" aria-label="Close modal window" tabindex="0">
      <svg viewBox="0 0 14 14" fill="none"><path d="M1 1l12 12M13 1L1 13" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    </button>

    <div id="lfModalFormContent">
      <div class="lf-header">
        <h2 class="lf-main-heading" id="lfMainHeading">Get in touch</h2>
        <p class="lf-sub-heading" id="lfSubHeading">Someone will reach out to you in 24 hours</p>
      </div>

      <form class="lf-form" id="lfForm" novalidate>
        <input class="lf-hp" type="text" name="website" value="" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" id="lfGclid"       name="gclid">
        <input type="hidden" id="lfFclid"       name="fclid">
        <input type="hidden" id="lfUtmSource"   name="utm_source">
        <input type="hidden" id="lfUtmMedium"   name="utm_medium">
        <input type="hidden" id="lfUtmCampaign" name="utm_campaign">
        <input type="hidden" id="lfUtmTerm"     name="utm_term">
        <input type="hidden" id="lfUtmContent"  name="utm_content">
        <input type="hidden" id="lfSourceUrl"   name="source_url">
        <input type="hidden" id="lfSubmittedAt" name="submitted_at">

        <div class="lf-field" id="lfNameField">
          <div class="lf-input-box">
            <label class="lf-label" for="lfName">Full name<span class="lf-req" aria-hidden="true">*</span></label>
            <input class="lf-input lf-focusable" type="text" id="lfName" name="name" autocomplete="name" aria-required="true" tabindex="0" aria-invalid="false" maxlength="60" aria-describedby="lfNameErr">
            <span class="lf-valid-icon" aria-hidden="true">
              <svg viewBox="0 0 14 14" fill="none"><path d="M1 7l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <button type="button" class="lf-clear-btn lf-focusable" aria-label="Clear name field" tabindex="-1">
              <svg viewBox="0 0 10 10" fill="none"><path d="M1 1l8 8M9 1L1 9" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>
            </button>
          </div>
          <div class="lf-err" id="lfNameErr" role="alert"></div>
        </div>

        <div class="lf-field lf-field-phone" id="lfPhoneField">
          <div class="lf-input-box">
            <label class="lf-label" id="lfPhoneLbl" for="lfPhone">Mobile<span class="lf-req" aria-hidden="true">*</span></label>
            <div class="lf-phone-row">
              <button type="button" class="lf-cc-trigger lf-focusable" id="lfCcTrigger" aria-haspopup="listbox" aria-expanded="false" aria-controls="lfCcPanel" aria-label="Select country dial code" tabindex="0">
                <span id="lfCcDisplay">+91</span>
                <svg class="lf-cc-arrow" viewBox="0 0 8 5" fill="none"><path d="M1 1l3 3 3-3" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>
              </button>
              
              <div class="lf-cc-panel" id="lfCcPanel" role="listbox" aria-labelledby="lfPhoneLbl">
                <input class="lf-cc-search lf-focusable" type="text" id="lfCcSearch" role="combobox" aria-expanded="true" aria-autocomplete="list" aria-controls="lfCcList" placeholder="Search country..." autocomplete="off" aria-label="Search countries by name or code" tabindex="-1">
                <div class="lf-cc-list" id="lfCcList"></div>
              </div>

              <input type="hidden" id="lfCcVal" name="country_code" value="+91">
              <div class="lf-divider"></div>
              <input class="lf-input lf-focusable lf-input-phone-stretch" type="tel" id="lfPhone" name="phone" inputmode="numeric" autocomplete="tel" aria-required="true" tabindex="0" aria-invalid="false" maxlength="15" aria-describedby="lfPhoneErr">
              <span class="lf-valid-icon" aria-hidden="true">
                <svg viewBox="0 0 14 14" fill="none"><path d="M1 7l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
              <button type="button" class="lf-clear-btn lf-focusable" id="lfPhoneClearBtn" aria-label="Clear mobile number field" tabindex="-1">
                <svg viewBox="0 0 10 10" fill="none"><path d="M1 1l8 8M9 1L1 9" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>
              </button>
            </div>
          </div>
          <div class="lf-err" id="lfPhoneErr" role="alert"></div>
        </div>

        <div class="lf-field" id="lfEmailField">
          <div class="lf-input-box">
            <label class="lf-label" for="lfEmail">Email<span class="lf-req" aria-hidden="true">*</span></label>
            <input class="lf-input lf-focusable" type="email" id="lfEmail" name="email" autocomplete="email" aria-required="true" tabindex="0" aria-invalid="false" maxlength="120" aria-describedby="lfEmailErr">
            <span class="lf-valid-icon" aria-hidden="true">
              <svg viewBox="0 0 14 14" fill="none"><path d="M1 7l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <button type="button" class="lf-clear-btn lf-focusable" aria-label="Clear email field" tabindex="-1">
              <svg viewBox="0 0 10 10" fill="none"><path d="M1 1l8 8M9 1L1 9" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>
            </button>
          </div>
          <div class="lf-err" id="lfEmailErr" role="alert"></div>
        </div>

        <div class="lf-submit-wrap">
          <button type="submit" class="lf-btn lf-focusable" id="lfSubmitBtn" tabindex="0">
            <div class="lf-spinner"></div>
            <span id="lfBtnText">Submit</span>
          </button>
          <p class="lf-global-err" id="lfGlobalErr" role="alert" aria-live="assertive" aria-atomic="true">Connection issue. Your details are safely held — please click Submit once more to retry or reach out to support.</p>
        </div>
      </form>
    </div>
  </div>
</div>

<script>
(function () {
  var WEBHOOK_URL  = "https://YOUR_WEBHOOK_URL_HERE";
  if (!WEBHOOK_URL || WEBHOOK_URL.indexOf("YOUR_WEBHOOK") !== -1) {
    console.error("[lead form] WEBHOOK_URL is not configured.");
  }
  var REDIRECT_URL = window.lfRedirectUrl || "/thank-you/";

  var STRINGS = {
    btnSubmit:        "Submit",
    btnSending:       "Sending...",
    errNameRequired:  "Name is required",
    errNameInvalid:   "Enter a valid name",
    errPhoneRequired: "Mobile number is required",
    errPhoneInvalid:  "Enter a valid {len}-digit number for {country}",
    errPhoneCode:     "Please select a valid country code",
    errPhoneUnknown:  "Country code not recognised — please select manually",
    errEmailRequired: "Email is required",
    errEmailInvalid:  "Enter a valid email",
    errCooldown:      "You've already submitted recently. Please wait before trying again.",
    slowSubmit:       "Still submitting... Please wait.",
    successHeading:   "Thank You",
    successBody:      "Your request has been received. Redirecting in {n}s...",
  };

  var FORM_SECRET = window.lfFormSecret || "";
  var nameRx  = /^[\p{Letter}\p{Mark}\p{Number}\s.'-]{2,60}$/u;
  var emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  var lfFormOpenTime = null;
  var isSubmitting = false;
  var slowSubmitTimer = null;
  var autofillListeners = [];

  if (window.lfActiveInstanceWipe && typeof window.lfActiveInstanceWipe === "function") {
    window.lfActiveInstanceWipe();
  }

  var Store = (function () {
    var mem = {};
    return {
      set: function (k, v) { mem[k] = v; try { sessionStorage.setItem(k, v); } catch (e) {} },
      get: function (k) {
        try { var v = sessionStorage.getItem(k); if (v !== null) return v; } catch (e) {}
        return mem[k] !== undefined ? String(mem[k]) : null;
      }
    };
  })();

  var VARIABLE_LENGTH_COUNTRIES = ["US","CA","GB","AU","IN","BR","MX","NG","ID","PK"];

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

  var _sorted = null;
  function getSorted() {
    if (!_sorted) _sorted = COUNTRIES.slice().sort(function(a,b){ return a.name.localeCompare(b.name); });
    return _sorted;
  }

  var isMobile = function() { return window.innerWidth <= 600; };

  var modalOverlay       = document.getElementById("lfModalOverlay");
  // DOM Elements
  var modalClose         = document.getElementById("lfModalClose");
  var modalContent       = document.getElementById("lfWrap");
  var mainFormContentBox = document.getElementById("lfModalFormContent");
  var form               = document.getElementById("lfForm");
  var nameInput          = document.getElementById("lfName");
  var phoneInput         = document.getElementById("lfPhone");
  var emailInput         = document.getElementById("lfEmail");
  var nameField          = document.getElementById("lfNameField");
  var phoneField         = document.getElementById("lfPhoneField");
  var emailField         = document.getElementById("lfEmailField");
  var nameErr            = document.getElementById("lfNameErr");
  var phoneErr           = document.getElementById("lfPhoneErr");
  var emailErr           = document.getElementById("lfEmailErr");
  var submitBtn          = document.getElementById("lfSubmitBtn");
  var btnText            = document.getElementById("lfBtnText");
  var honeypot           = form.querySelector('input[name="website"]');
  var ccTrigger          = document.getElementById("lfCcTrigger");
  var ccDisplay          = document.getElementById("lfCcDisplay");
  var ccPanel            = document.getElementById("lfCcPanel");
  var ccSearch           = document.getElementById("lfCcSearch");
  var ccList             = document.getElementById("lfCcList");
  var ccVal              = document.getElementById("lfCcVal");
  var globalErr          = document.getElementById("lfGlobalErr");
  var ccBackdrop         = document.getElementById("lfCcBackdrop");

  var currentCountry = (function() {
    var s = getSorted();
    return s.find(function(c){ return c.code === "IN"; }) || s[0];
  })();

  var submitted = false;
  var kbFocusIdx = -1;
  var filteredCountries = [];
  var searchDebounceTimer = null;
  var lastActiveElement = null;

  function updateClearButtonsA11y(inputEl) {
    var field = inputEl.closest(".lf-field");
    var btn = field.querySelector(".lf-clear-btn");
    if (!btn) return;
    if (inputEl.value.trim() !== "") {
      btn.setAttribute("tabindex", "0");
      field.classList.add("lf-has-input-text");
    } else {
      btn.setAttribute("tabindex", "-1");
      field.classList.remove("lf-has-input-text");
    }
  }

  var ModalController = {
    open: function () {
      // Android QA Fix: Push history state when opening modal
      if (!history.state || !history.state.lfModalOpen) {
        history.pushState({ lfModalOpen: true }, "");
      }

      lfFormOpenTime = Date.now();
      lastActiveElement = document.activeElement;
      var sw = window.innerWidth - document.documentElement.clientWidth;
      if (sw > 0) document.body.style.paddingRight = sw + "px";
      modalOverlay.classList.add("lf-modal-open");
      document.body.style.overflow = "hidden";
      [nameInput, phoneInput, emailInput].forEach(updateClearButtonsA11y);
      setTimeout(function() { nameInput.focus(); }, 250);
    },
    close: function (skipHistory) {
      // Android QA Fix: Revert history if closing manually via UI
      if (!skipHistory && history.state && history.state.lfModalOpen) {
        history.back(); // Triggers popstate, which calls close(true)
        return;
      }

      modalOverlay.classList.remove("lf-modal-open");
      document.body.style.overflow = "";
      document.body.style.paddingRight = "";
      closePanel();
      if (lastActiveElement && typeof lastActiveElement.focus === "function") lastActiveElement.focus();
    }
  };

  // Android QA Fix: Close modal when Android hardware back button is pressed
  var popstateTracker = function(e) {
    if (modalOverlay.classList.contains("lf-modal-open")) {
      ModalController.close(true);
    }
  };
  window.addEventListener("popstate", popstateTracker);

  window.openModal  = function(e) { if (e) e.preventDefault(); ModalController.open(); };
  window.closeModal = function() { ModalController.close(); };

  var ValidationService = {
    setErr: function(fieldEl, errorEl, msg) {
      fieldEl.classList.add("lf-has-error"); fieldEl.classList.remove("lf-is-valid");
      errorEl.textContent = msg;
      var inp = fieldEl.querySelector(".lf-input");
      if (inp) inp.setAttribute("aria-invalid", "true");
    },
    clrErr: function(fieldEl, errorEl) {
      fieldEl.classList.remove("lf-has-error"); errorEl.textContent = "";
      var inp = fieldEl.querySelector(".lf-input");
      if (inp) inp.setAttribute("aria-invalid", "false");
    },
    setValid: function(fieldEl) { fieldEl.classList.add("lf-is-valid"); },
    clrValid: function(fieldEl) { fieldEl.classList.remove("lf-is-valid"); },
    normalizeString: function(str) {
      return str.trim().replace(/\s+/g, " ").replace(/[\u200B-\u200D\uFEFF]/g, "");
    },
    vName: function(live) {
      var v = nameInput.value.trim();
      if (!v) { if (!live || submitted) this.setErr(nameField, nameErr, STRINGS.errNameRequired); return false; }
      if (!nameRx.test(this.normalizeString(v))) { this.setErr(nameField, nameErr, STRINGS.errNameInvalid); return false; }
      this.clrErr(nameField, nameErr);
      if (!live) this.setValid(nameField);
      return true;
    },
    vPhone: function(live) {
      var v = phoneInput.value.trim();
      if (!v) { if (!live || submitted) this.setErr(phoneField, phoneErr, STRINGS.errPhoneRequired); return false; }
      if (!currentCountry || !currentCountry.code) { this.setErr(phoneField, phoneErr, STRINGS.errPhoneCode); return false; }
      var digits = v.replace(/\D/g, "");
      var expLen = currentCountry.len || 10;
      var isVar  = VARIABLE_LENGTH_COUNTRIES.indexOf(currentCountry.code) !== -1;
      var min = isVar ? expLen - 1 : expLen; var max = isVar ? expLen + 1 : expLen;
      if (digits.length < min || digits.length > max) {
        this.setErr(phoneField, phoneErr, STRINGS.errPhoneInvalid.replace("{len}", expLen).replace("{country}", currentCountry.name));
        return false;
      }
      this.clrErr(phoneField, phoneErr);
      if (!live) this.setValid(phoneField);
      return true;
    },
    vEmail: function(live) {
      var v = emailInput.value.trim();
      if (!v) { if (!live || submitted) this.setErr(emailField, emailErr, STRINGS.errEmailRequired); return false; }
      if (!emailRx.test(v) || /\.\./.test(v)) { this.setErr(emailField, emailErr, STRINGS.errEmailInvalid); return false; }
      this.clrErr(emailField, emailErr);
      if (!live) this.setValid(emailField);
      return true;
    }
  };

  var PhoneSyncManager = {
    syncInput: function() {
      var raw = phoneInput.value.trim();
      var s = getSorted();
      var finalStr = "";
      
      if (raw.indexOf('+') === 0 || raw.indexOf('00') === 0) {
        if (raw.indexOf('00') === 0) raw = '+' + raw.substring(2);
        var digits = raw.replace(/\D/g, "");
        var matched = null;
        for (var i = 4; i >= 1; i--) {
          var prefix = "+" + digits.substring(0, i);
          matched = s.find(function(c){ return c.dial === prefix; });
          if (matched) break;
        }
        if (matched) {
          selectCountry(matched);
          finalStr = digits.substring(matched.dial.replace(/\D/g, "").length);
        } else {
          finalStr = raw.replace(/\D/g, "");
          ValidationService.setErr(phoneField, phoneErr, STRINGS.errPhoneUnknown);
        }
      } else {
        var cc = currentCountry ? currentCountry.dial : "";
        var ccDigits = cc.replace(/\D/g, "");
        finalStr = raw;
        
        if (cc) {
          var ccEscaped = cc.replace('+', '\\\\+');
          var rxPlus = new RegExp('^' + ccEscaped); 
          var rxZero = new RegExp('^0' + ccDigits);
          finalStr = finalStr.replace(rxPlus, '').replace(rxZero, '');
        }
        
        finalStr = finalStr.replace(/\D/g, '');
      }

      if (currentCountry && finalStr.indexOf('0') === 0) {
        var expLen = currentCountry.len || 10;
        var isVar = VARIABLE_LENGTH_COUNTRIES.indexOf(currentCountry.code) !== -1;
        var min = isVar ? expLen - 1 : expLen;
        var max = isVar ? expLen + 1 : expLen;
        
        if (finalStr.length - 1 === expLen) {
          finalStr = finalStr.substring(1);
        } else if (finalStr.length > max && (finalStr.length - 1) >= min && (finalStr.length - 1) <= max) {
          finalStr = finalStr.substring(1);
        }
      }

      phoneInput.value = finalStr;
      if (phoneInput.value.length > 15) phoneInput.value = phoneInput.value.substring(0, 15);
      checkValueState(phoneInput);
      if (submitted) ValidationService.vPhone(true);
    }
  };

  var TransportService = {
    pair: function(ms) {
      var c = new AbortController(); var t = setTimeout(function(){ c.abort(); }, ms);
      return { signal: c.signal, timeoutId: t };
    },
    isTransient: function(status) { return [408,425,429,500,502,503,504].indexOf(status) !== -1; },
    post: function(url, data, attempt) {
      var self = this; var max = 3; var backoff = 1000;
      var conn = self.pair(10000);
      var headers = { "Content-Type": "application/json" };
      if (FORM_SECRET) headers["X-Form-Secret"] = FORM_SECRET;
      return fetch(url, { method:"POST", headers: headers, body:JSON.stringify(data), signal:conn.signal })
      .then(function(res) {
        clearTimeout(conn.timeoutId);
        if (!res.ok) {
          if (self.isTransient(res.status) && attempt < max) {
            return new Promise(function(resolve){ setTimeout(function(){ resolve(self.post(url, data, attempt+1)); }, backoff * Math.pow(2, attempt-1)); });
          }
          throw new Error("HTTP " + res.status);
        }
        var ct = res.headers.get("content-type") || "";
        if (res.status === 204 || ct.indexOf("application/json") === -1) return res.text().then(function(){ return {success:true}; });
        return res.json();
      })
      .catch(function(err) {
        clearTimeout(conn.timeoutId);
        if (err.name !== "AbortError" && attempt < max) {
          return new Promise(function(resolve){ setTimeout(function(){ resolve(self.post(url, data, attempt+1)); }, backoff * Math.pow(2, attempt-1)); });
        }
        throw err;
      });
    }
  };

  document.querySelectorAll(".lf-input").forEach(function(inp) {
    var h = function(e) {
      if (e.animationName === "lfAutofillDetected") {
        inp.closest(".lf-field").classList.add("lf-autofilled");
        checkValueState(inp);
      }
    };
    inp.addEventListener("animationstart", h);
    autofillListeners.push({ node: inp, handler: h });
  });

  var footerLinks = document.querySelectorAll('.lf-modal-trigger');
  for (var i = 0; i < footerLinks.length; i++) {
    footerLinks[i].addEventListener("click", window.openModal);
  }
  
  var modalClose = document.getElementById("lfModalCloseBtn");
  if (modalClose) {
    modalClose.addEventListener("click", function() { window.closeModal(); });
  }

  var overlayClickTracker = function(e) {
    if (!modalContent.contains(e.target) && !ccPanel.contains(e.target) && e.target !== ccBackdrop) {
      window.closeModal();
    }
  };
  modalOverlay.addEventListener("click", overlayClickTracker);

  var modalKeyTracker = function(e) {
    if (e.key === "Escape") {
      ccPanel.classList.contains("lf-cc-open") ? (closePanel(), ccTrigger.focus()) : window.closeModal();
      return;
    }
    if (e.key !== "Tab") return;
    var els = Array.prototype.slice.call(modalContent.querySelectorAll(".lf-focusable"));
    var focusables = els.filter(function(el) {
      return (el.offsetWidth > 0 || el.offsetHeight > 0 || el.getClientRects().length > 0)
        && !el.disabled && parseInt(el.getAttribute("tabindex") || "0", 10) >= 0;
    });
    if (!focusables.length) return;
    var first = focusables[0], last = focusables[focusables.length - 1];
    if (e.shiftKey) { if (document.activeElement === first) { last.focus(); e.preventDefault(); } }
    else            { if (document.activeElement === last)  { first.focus(); e.preventDefault(); } }
  };
  modalOverlay.addEventListener("keydown", modalKeyTracker);

  function selectCountry(c) {
    currentCountry = c;
    ccDisplay.textContent = c.dial;
    ccVal.value = c.dial;
  }

  function buildList(filter) {
    ccList.innerHTML = "";
    var q = (filter || "").toLowerCase();
    filteredCountries = getSorted().filter(function(c){
      return !q || c.name.toLowerCase().indexOf(q) !== -1 || c.dial.indexOf(q) !== -1;
    });
    var frag = document.createDocumentFragment();
    filteredCountries.forEach(function(c, idx) {
      var el = document.createElement("div");
      el.className = "lf-cc-opt";
      el.setAttribute("role", "option");
      el.setAttribute("aria-selected", currentCountry && c.code === currentCountry.code ? "true" : "false");
      el.setAttribute("tabindex", "-1");
      el.setAttribute("id", "lf-opt-" + idx);
      el.innerHTML = '<span class="lf-cc-opt-dial">' + c.dial + '</span><span>' + c.name + '</span>';
      el.addEventListener("click", function(e) {
        e.stopPropagation();
        selectCountry(c);
        closePanel();
        phoneInput.focus();
      });
      frag.appendChild(el);
    });
    ccList.appendChild(frag);
    kbFocusIdx = -1;
    ccSearch.removeAttribute("aria-activedescendant");
  }

  function openPanel() {
    if (ccPanel.classList.contains("lf-cc-open")) return;
    buildList("");
    if (isMobile()) {
      modalOverlay.appendChild(ccBackdrop);
      modalOverlay.appendChild(ccPanel);
      void ccPanel.offsetWidth; 
      ccPanel.classList.add("lf-cc-open");
      ccBackdrop.classList.add("lf-cc-open");
      ccTrigger.setAttribute("aria-expanded", "true");
    } else {
      document.querySelector(".lf-phone-row").appendChild(ccPanel);
      ccPanel.classList.add("lf-cc-open");
      ccTrigger.setAttribute("aria-expanded", "true");
      ccSearch.focus();
      setTimeout(function() {
        document.addEventListener("click", outsideClickListener);
      }, 50);
    }
  }

  function closePanel() {
    if (!ccPanel.classList.contains("lf-cc-open")) return;
    ccPanel.classList.remove("lf-cc-open");
    ccTrigger.setAttribute("aria-expanded", "false");
    ccBackdrop.classList.remove("lf-cc-open");
    setTimeout(function() {
      if (!ccPanel.classList.contains("lf-cc-open")) {
        document.querySelector(".lf-phone-row").appendChild(ccPanel);
      }
    }, 300);
    document.removeEventListener("click", outsideClickListener);
    document.removeEventListener("touchstart", outsideClickListener);
  }

  ccBackdrop.addEventListener("click", function(e) { 
    e.stopPropagation();
    closePanel(); 
    ccTrigger.focus(); 
  });

  var outsideClickListener = function(e) {
    var target = e.target;
    if (target && target.nodeType === 3) target = target.parentNode;
    if (!phoneField.contains(target) && target !== ccBackdrop) closePanel();
  };

  var ccTriggerTracker = function(e) {
    e.preventDefault(); e.stopPropagation();
    ccPanel.classList.contains("lf-cc-open") ? closePanel() : openPanel();
  };
  ccTrigger.addEventListener("click", ccTriggerTracker);

  var ccSearchTracker = function() {
    var self = this; clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(function(){ buildList(self.value); }, 150);
  };
  ccSearch.addEventListener("input", ccSearchTracker);

  var ccCcPanelKeyHandler = function(e) {
    if (!ccPanel.classList.contains("lf-cc-open")) return;
    var options = ccList.querySelectorAll(".lf-cc-opt");
    if (!options.length) return;
    function moveTo(newIdx) {
      if (kbFocusIdx >= 0) { options[kbFocusIdx].classList.remove("lf-keyboard-active"); options[kbFocusIdx].setAttribute("aria-selected","false"); }
      kbFocusIdx = newIdx;
      options[kbFocusIdx].classList.add("lf-keyboard-active"); options[kbFocusIdx].setAttribute("aria-selected","true");
      options[kbFocusIdx].scrollIntoView({ block: "nearest" });
      ccSearch.setAttribute("aria-activedescendant", "lf-opt-" + kbFocusIdx);
    }
    if      (e.key === "ArrowDown") { e.preventDefault(); if (kbFocusIdx < options.length - 1) moveTo(kbFocusIdx + 1); }
    else if (e.key === "ArrowUp")   { e.preventDefault(); if (kbFocusIdx > 0) moveTo(kbFocusIdx - 1); }
    else if (e.key === "Home")      { e.preventDefault(); if (options.length) moveTo(0); }
    else if (e.key === "End")       { e.preventDefault(); if (options.length) moveTo(options.length - 1); }
    else if (e.key === "Enter")     { e.preventDefault(); if (kbFocusIdx >= 0 && options[kbFocusIdx]) options[kbFocusIdx].dispatchEvent(new Event("click")); }
    else if (e.key === "Escape")    { e.preventDefault(); closePanel(); ccTrigger.focus(); }
  };
  ccSearch.addEventListener("keydown", ccCcPanelKeyHandler);

  function checkValueState(inputEl) {
    var f = inputEl.closest(".lf-field");
    if (inputEl.value.trim() !== "") f.classList.add("lf-has-value");
    else f.classList.remove("lf-has-value", "lf-autofilled", "lf-is-valid");
    updateClearButtonsA11y(inputEl);
  }

  var phoneClearTracker = function() {
    phoneInput.value = ""; phoneField.classList.remove("lf-is-valid");
    checkValueState(phoneInput); phoneInput.focus();
    if (submitted) ValidationService.vPhone(true);
  };
  document.getElementById("lfPhoneClearBtn").addEventListener("click", phoneClearTracker);

  var activeFieldEraserClosuresArray = [];
  document.querySelectorAll(".lf-field:not(.lf-field-phone)").forEach(function(fieldEl) {
    var inp = fieldEl.querySelector(".lf-input");
    var btn = fieldEl.querySelector(".lf-clear-btn");
    if (btn && inp) {
      var h = function() {
        inp.value = ""; fieldEl.classList.remove("lf-is-valid");
        checkValueState(inp); inp.focus();
        if (submitted) {
          if (inp.id === "lfName")  ValidationService.vName(true);
          if (inp.id === "lfEmail") ValidationService.vEmail(true);
        }
      };
      btn.addEventListener("click", h);
      activeFieldEraserClosuresArray.push({ node: btn, handler: h });
    }
  });

  var inputFocusTracker = function() {
    var f = this.closest(".lf-field");
    f.classList.add("lf-focused", "lf-has-value"); f.classList.remove("lf-is-valid");
  };
  var inputBlurTracker = function() {
    this.closest(".lf-field").classList.remove("lf-focused");
    checkValueState(this);
    if (this === nameInput  && nameInput.value.trim())  ValidationService.vName(false);
    if (this === emailInput && emailInput.value.trim()) ValidationService.vEmail(false);
    if (this === phoneInput && phoneInput.value.trim()) ValidationService.vPhone(false);
  };
  var inputInputTracker = function() { checkValueState(this); };

  [nameInput, emailInput, phoneInput].forEach(function(el) {
    el.addEventListener("focus", inputFocusTracker);
    el.addEventListener("blur",  inputBlurTracker);
    el.addEventListener("input", inputInputTracker);
  });

  var syncPhoneTracker = function() { PhoneSyncManager.syncInput(); };
  phoneInput.addEventListener("input",  syncPhoneTracker);
  phoneInput.addEventListener("change", syncPhoneTracker);

  var phonePasteTracker = function(e) {
    var pasted = null;
    if (e.clipboardData && e.clipboardData.getData) pasted = e.clipboardData.getData("text/plain");
    if (pasted !== null) { e.preventDefault(); phoneInput.value = pasted; PhoneSyncManager.syncInput(); }
    else { setTimeout(function(){ PhoneSyncManager.syncInput(); }, 50); }
  };
  phoneInput.addEventListener("paste", phonePasteTracker);

  var UTM_TTL = 30 * 60 * 1000;
  var urlParams = new URLSearchParams(window.location.search);
  function getParam(key) {
    var val = urlParams.get(key);
    if (val) { Store.set("lf_" + key, val); Store.set("lf_" + key + "_ts", String(Date.now())); return val; }
    var ts = parseInt(Store.get("lf_" + key + "_ts") || "0", 10);
    if (ts && (Date.now() - ts) < UTM_TTL) return Store.get("lf_" + key) || "";
    return "";
  }

  (function prefillHidden() {
    document.getElementById("lfGclid").value       = getParam("gclid");
    document.getElementById("lfFclid").value       = getParam("fclid");
    document.getElementById("lfUtmSource").value   = getParam("utm_source");
    document.getElementById("lfUtmMedium").value   = getParam("utm_medium");
    document.getElementById("lfUtmCampaign").value = getParam("utm_campaign");
    document.getElementById("lfUtmTerm").value     = getParam("utm_term");
    document.getElementById("lfUtmContent").value  = getParam("utm_content");
    document.getElementById("lfSourceUrl").value   = window.location.href;
    setTimeout(function(){ [nameInput, phoneInput, emailInput].forEach(checkValueState); }, 100);
  })();

  var formSubmitTracker = function(e) {
    e.preventDefault();
    if (isSubmitting) return;
    submitted = true;
    globalErr.classList.remove("lf-show");
    if (honeypot.value !== "") return;
    if (!lfFormOpenTime || (Date.now() - lfFormOpenTime) < 1500) return;

    var nameOk  = ValidationService.vName();
    var phoneOk = ValidationService.vPhone();
    var emailOk = ValidationService.vEmail();
    if (!(nameOk && phoneOk && emailOk)) return;

    var lock = Store.get("lf_conversion_timestamp_lock");
    if (lock && (Date.now() - parseInt(lock, 10)) < 10 * 60 * 1000) {
      globalErr.classList.add("lf-show"); globalErr.textContent = STRINGS.errCooldown; return;
    }
    if (!navigator.onLine) { globalErr.classList.add("lf-show"); return; }

    document.getElementById("lfSubmittedAt").value = new Date().toISOString();
    isSubmitting = true; submitBtn.disabled = true;
    submitBtn.classList.add("lf-loading"); btnText.textContent = STRINGS.btnSending;

    slowSubmitTimer = setTimeout(function() {
      if (isSubmitting) btnText.textContent = STRINGS.slowSubmit;
    }, 5000);

    var payload = {
      name: ValidationService.normalizeString(nameInput.value),
      country_code: ccVal.value,
      phone: ccVal.value + phoneInput.value.trim().replace(/\s+/g,""),
      email: emailInput.value.trim().toLowerCase().replace(/[\u200B-\u200D\uFEFF]/g,""),
      source_url:   document.getElementById("lfSourceUrl").value,
      submitted_at: document.getElementById("lfSubmittedAt").value,
      gclid: document.getElementById("lfGclid").value,
      fclid: document.getElementById("lfFclid").value,
      utm_source:   document.getElementById("lfUtmSource").value,
      utm_medium:   document.getElementById("lfUtmMedium").value,
      utm_campaign: document.getElementById("lfUtmCampaign").value,
      utm_term:     document.getElementById("lfUtmTerm").value,
      utm_content:  document.getElementById("lfUtmContent").value
    };

    TransportService.post(WEBHOOK_URL, payload, 1)
    .then(function(data) {
      if (data && data.success === false) throw new Error("API returned success: false");
      clearTimeout(slowSubmitTimer);
      Store.set("lf_conversion_timestamp_lock", String(Date.now()));

      mainFormContentBox.innerHTML = "";
      var canvas = document.createElement("div");
      canvas.className = "lf-success-canvas";
      canvas.setAttribute("role","status"); canvas.setAttribute("aria-live","polite");

      var circle = document.createElement("div");
      circle.className = "lf-success-circle";
      circle.innerHTML = '<svg viewBox="0 0 12 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5l3.5 3.5L11 1"/></svg>';

      var h3 = document.createElement("h3");
      h3.setAttribute("tabindex","-1");
      h3.style.cssText = "font-size:20px;font-weight:500;color:#0f0f0f;margin-bottom:6px;outline:none;";
      h3.textContent = STRINGS.successHeading;

      var delay = 3000; var remaining = 3;
      var p = document.createElement("p");
      p.style.cssText = "font-size:14px;color:#666;";
      p.textContent = STRINGS.successBody.replace("{n}", remaining);

      canvas.appendChild(circle); canvas.appendChild(h3); canvas.appendChild(p);
      mainFormContentBox.appendChild(canvas);
      setTimeout(function() { h3.focus(); }, 50);

      var ticker = setInterval(function() {
        remaining--;
        if (remaining > 0) p.textContent = STRINGS.successBody.replace("{n}", remaining);
        else clearInterval(ticker);
      }, 1000);

      setTimeout(function(){
        clearInterval(ticker);
        isSubmitting = false; submitBtn.disabled = false;
        submitBtn.classList.remove("lf-loading"); btnText.textContent = STRINGS.btnSubmit;
        window.closeModal(); window.location.href = REDIRECT_URL;
      }, delay);
    })
    .catch(function(err) {
      clearTimeout(slowSubmitTimer);
      isSubmitting = false; submitBtn.disabled = false;
      submitBtn.classList.remove("lf-loading"); btnText.textContent = STRINGS.btnSubmit;
      globalErr.classList.add("lf-show");
    });
  };
  form.addEventListener("submit", formSubmitTracker);

  window.lfActiveInstanceWipe = function() {
    clearTimeout(searchDebounceTimer);
    window.removeEventListener("popstate", popstateTracker); // Added cleanup
    for (var i = 0; i < footerLinks.length; i++) {
      footerLinks[i].removeEventListener("click", window.openModal);
    }
    if (modalClose) modalClose.removeEventListener("click", window.closeModal);
    modalOverlay.removeEventListener("click", overlayClickTracker);
    modalOverlay.removeEventListener("keydown", modalKeyTracker);
    ccTrigger.removeEventListener("click", ccTriggerTracker);
    ccSearch.removeEventListener("input", ccSearchTracker);
    ccSearch.removeEventListener("keydown", ccCcPanelKeyHandler);
    document.removeEventListener("click", outsideClickListener);
    document.removeEventListener("touchstart", outsideClickListener);
    document.getElementById("lfPhoneClearBtn").removeEventListener("click", phoneClearTracker);
    phoneInput.removeEventListener("input",  syncPhoneTracker);
    phoneInput.removeEventListener("change", syncPhoneTracker);
    phoneInput.removeEventListener("paste",  phonePasteTracker);
    form.removeEventListener("submit", formSubmitTracker);
    activeFieldEraserClosuresArray.forEach(function(item){ item.node.removeEventListener("click", item.handler); });
    [nameInput, emailInput, phoneInput].forEach(function(el) {
      el.removeEventListener("focus", inputFocusTracker);
      el.removeEventListener("blur",  inputBlurTracker);
      el.removeEventListener("input", inputInputTracker);
    });
    autofillListeners.forEach(function(item){ item.node.removeEventListener("animationstart", item.handler); });
  };
})();
</script>
