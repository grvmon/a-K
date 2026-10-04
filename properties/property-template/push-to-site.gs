/**
 * ╔══════════════════════════════════════════════════════════════════╗
 * ║  acre&key — "Push to Site" Google Apps Script                   ║
 * ║  Reads this Google Sheet → pushes property-data.js to GitHub    ║
 * ╠══════════════════════════════════════════════════════════════════╣
 * ║  SETUP (one-time, 5 minutes):                                   ║
 * ║  1. In your Google Sheet → Extensions → Apps Script             ║
 * ║  2. Paste this entire file                                       ║
 * ║  3. Fill in GITHUB_TOKEN, GITHUB_REPO, and PROPERTY_SLUG below  ║
 * ║  4. Save → Run → Authorize                                      ║
 * ║  5. Extensions → Apps Script → Add a button to your sheet:      ║
 * ║     Insert → Drawing → draw a button shape → assign pushToSite  ║
 * ╚══════════════════════════════════════════════════════════════════╝
 */

// ─── CONFIG — FILL THESE IN ───────────────────────────────────────────────────

var GITHUB_TOKEN  = 'ghp_YOUR_PERSONAL_ACCESS_TOKEN_HERE';
// GitHub → Settings → Developer settings → Personal access tokens → Fine-grained
// Permissions needed: Contents (read + write) on your repo

var GITHUB_OWNER  = 'grvmon';          // Your GitHub username
var GITHUB_REPO   = 'a-K';            // Your repo name
var GITHUB_BRANCH = 'main';

// The path inside the repo where property-data.js lives for this property
// e.g. for /property/prestige-evergreen/ → 'property/prestige-evergreen/property-data.js'
var FILE_PATH     = 'properties/property-template/property-data.js';

// The sheet tab name that holds your key-value data
var SHEET_NAME    = 'Sheet1';

// ─────────────────────────────────────────────────────────────────────────────

/**
 * Reads Column A (keys) and Column B (values) from the sheet,
 * builds a JS file, and pushes it to GitHub via the REST API.
 *
 * Assign this function to your "Push to Site" button.
 */
function pushToSite() {
  var ss    = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  var rows  = sheet.getDataRange().getValues();

  // Build a plain object from the key-value rows
  var data = {};
  rows.forEach(function (row) {
    var key = String(row[0]).trim();
    var val = String(row[1]).trim();
    if (key && key !== 'KEY') data[key] = val;
  });

  // Stamp the current date
  data['LAST_PUSHED'] = new Date().toISOString();

  // Generate the property-data.js file content
  var jsContent = buildJsFile(data);

  // Push to GitHub
  var result = pushToGitHub(jsContent);

  if (result.success) {
    SpreadsheetApp.getUi().alert(
      '✅ Pushed successfully!\n\nThe property page will reflect your changes within seconds.\n\nCommit: ' + result.sha
    );
  } else {
    SpreadsheetApp.getUi().alert('❌ Push failed:\n\n' + result.error);
  }
}

/**
 * Build the property-data.js file content from a data object.
 */
function buildJsFile(data) {
  var lines = [
    '/**',
    ' * acre&key Property Data',
    ' * Last pushed: ' + new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST',
    ' * DO NOT EDIT MANUALLY — edit the Google Sheet, then click "Push to Site".',
    ' * NOTE: SEO-critical fields must be hardcoded in the HTML.',
    ' */',
    'window.AK_PROPERTY = {'
  ];

  var keys = Object.keys(data);
  keys.forEach(function (key, i) {
    var val = data[key].replace(/\/g, '\\').replace(/"/g, '\"');
    var comma = i < keys.length - 1 ? ',' : '';
    lines.push('  ' + JSON.stringify(key) + ': "' + val + '"' + comma);
  });

  lines.push('};');
  lines.push('');
  lines.push('// Auto-inject into DOM');
  lines.push('(function () {');
  lines.push('  var d = window.AK_PROPERTY;');
  lines.push('  document.querySelectorAll(\'[data-ak-field]\').forEach(function (el) {');
  lines.push('    var key = el.getAttribute(\'data-ak-field\');');
  lines.push('    if (d[key] !== undefined && d[key] !== \'\') el.textContent = d[key];');
  lines.push('  });');
  lines.push('  window.dispatchEvent(new CustomEvent(\'ak:data:ready\', { detail: d }));');
  lines.push('})();');

  return lines.join('
');
}

/**
 * Push content to GitHub via the Contents API.
 * Automatically handles the SHA (create vs. update).
 */
function pushToGitHub(content) {
  var apiUrl = 'https://api.github.com/repos/' + GITHUB_OWNER + '/' + GITHUB_REPO +
               '/contents/' + FILE_PATH;

  var headers = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
    'User-Agent': 'AcreKey-Sheets-Script'
  };

  // Step 1: Get the current file SHA (needed for updates)
  var sha = null;
  try {
    var getResp = UrlFetchApp.fetch(apiUrl + '?ref=' + GITHUB_BRANCH, {
      method: 'get',
      headers: headers,
      muteHttpExceptions: true
    });
    if (getResp.getResponseCode() === 200) {
      sha = JSON.parse(getResp.getContentText()).sha;
    }
  } catch (e) { /* file doesn't exist yet — will create */ }

  // Step 2: Push the new content
  var encodedContent = Utilities.base64Encode(
    Utilities.newBlob(content).getBytes()
  );

  var payload = {
    message: 'Push from Google Sheets: ' + new Date().toISOString(),
    content: encodedContent,
    branch: GITHUB_BRANCH
  };
  if (sha) payload.sha = sha;

  try {
    var putResp = UrlFetchApp.fetch(apiUrl, {
      method: 'put',
      headers: headers,
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    });

    var code = putResp.getResponseCode();
    if (code === 200 || code === 201) {
      var respData = JSON.parse(putResp.getContentText());
      return { success: true, sha: respData.commit.sha.substring(0, 7) };
    } else {
      return { success: false, error: 'HTTP ' + code + ': ' + putResp.getContentText() };
    }
  } catch (e) {
    return { success: false, error: e.message };
  }
}

/**
 * Adds a custom "acre&key" menu to the Google Sheet toolbar.
 * Runs automatically when the sheet is opened.
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('acre&key')
    .addItem('🚀 Push to Site', 'pushToSite')
    .addToUi();
}
