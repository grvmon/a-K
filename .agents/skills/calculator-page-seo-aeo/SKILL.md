---
name: calculator-page-seo-aeo
description: Build, audit or fix any acre&key calculator page (acrenkey.com/calculators/...) so it ranks in Google and gets cited by AI answer engines (Google AI Overviews, ChatGPT, Perplexity, Gemini). Use it for every one of the 75 calculator pages and the /calculators/ hub, before launch and in monthly re-audits.
---

# Calculator Page SEO + AEO + GEO Skill (acre&key)

Goal: 75 calculator pages plus 1 hub. Each page should be the most useful, trusted and fastest answer for its Bengaluru home-buyer query, readable by Google and quotable by AI.
Run each section in order. Every item is PASS / FIX / N/A. A page ships only when every P0 is PASS.
Priority: P0 = blocks launch, P1 = fix within a week, P2 = improvement.

---

## 0. Brand and compliance rules (P0, check first)
- [ ] The brand is written "acre&key" everywhere (title, meta, OG, schema, body). The legal name is Acrenkey Realty LLP.
- [ ] Never use "independent", "objective", "unbiased" or "100%". "Buyer-first" is allowed.
- [ ] No unbacked claims ("69-point", "saves 3x", "cuts tenure in half", "best", "guaranteed") unless the page shows the maths or a source.
- [ ] Don't compare acre&key with other firms, don't name builders negatively, and don't give project prices.
- [ ] Tax calculators carry "Indicative only. Verify with your CA before acting." Legal or registration ones carry "Verify with your lawyer."
- [ ] Every rate, fee, slab or legal threshold comes from an official source (IGR Karnataka / Kaveri, Karnataka Gazette, RBI, Income Tax Dept / India Code, GST Council / CBIC, BBMP/GBA, K-RERA, bank's official rate page). No figures from aggregator blogs.
- [ ] Results are labelled "indicative", with the assumptions listed.

## 1. Keyword and intent (P0)
- [ ] One primary keyword per page (e.g. "home loan EMI calculator"), plus a Bengaluru/Karnataka modifier where people search it ("stamp duty calculator Karnataka").
- [ ] 5-10 secondary and long-tail queries mapped (e.g. "EMI for 50 lakh home loan", "EMI for 1 crore 20 years").
- [ ] Intent matched: users want to calculate now, so the tool sits above the fold and works with no scroll on mobile.
- [ ] No cannibalisation: no two of the 75 pages target the same primary keyword. Keep a keyword map sheet with columns: slug, primary keyword, secondaries, cluster, hub link.
- [ ] People Also Ask, Google autocomplete and AI-answer questions collected, which become the FAQs and H2s.

## 2. URL, title and meta (P0)
- [ ] URL: /calculators/<primary-keyword-slug>/. Lowercase, hyphens, no dates, no IDs, with a trailing slash consistent sitewide.
- [ ] Title: 50-60 characters, primary keyword first, then the place and brand. Pattern: "<Calculator Name> for Bengaluru | acre&key". Unique across all 75.
- [ ] Meta description: 140-160 characters, states what it calculates plus the benefit, and contains the primary keyword. No banned words. Unique.
- [ ] Canonical is self-referencing, absolute https, and matches the live URL exactly.
- [ ] Robots meta: index, follow, max-snippet:-1, max-image-preview:large.
- [ ] OG and Twitter title, description, image (1200x630, per-calculator if possible) and url all match the page. Test that the apostrophe or ampersand doesn't truncate the text (escape the &).
- [ ] html lang="en-IN", meta charset UTF-8, viewport.

## 3. Page structure and headings (P0)
- [ ] Exactly one H1 with the primary keyword (e.g. "Home Loan EMI Calculator (Bengaluru, 2026)").
- [ ] Under the H1, a direct-answer lead of 40-60 words: what it calculates, the formula in one line, and one worked example. This is the AEO snippet.
- [ ] The tool sits directly below the lead.
- [ ] H2s are written as the questions people actually search (e.g. "How is home loan EMI calculated?"), not jargon ("Prepayment Paradox", "Master Matrix").
- [ ] H3s are used under H2s. No skipped levels, and no headings used for styling.
- [ ] No template placeholders (${...}), "No results found" or empty headings in the raw HTML.
- [ ] A visible breadcrumb: Home > Calculators > <Category> > <Calculator>.
- [ ] A visible "Last updated: DD Mon YYYY", plus "Rates checked: <date>" for any rate tables.

## 4. Content depth and usefulness (helpful content / E-E-A-T)
Required blocks on every page:
1. P0: the direct answer plus the tool.
2. P0: "How to use this calculator", 3-5 steps.
3. P0: "Formula and method", with the formula in text (not an image), each variable explained, and one fully worked Bengaluru example with real-looking round numbers.
4. P0: "What the result means", how to read the output and what decision it supports.
5. P1: "Assumptions and limits", what is and isn't included.
6. P1: a Bengaluru-specific section (local rates, authorities, typical scenarios: Whitefield, Sarjapur, North Bengaluru, and so on), facts only.
7. P1: a scenario table (e.g. EMI for ₹50L/75L/1Cr/1.5Cr/2Cr at 3 tenures), as an HTML table, not an image.
8. P0: FAQs, 5-8 questions from PAA and AI queries, each answered in 40-80 words, self-contained.
9. P1: related calculators, 3-6 links within the same cluster plus the next step in the journey.
10. P1: related guides, 2-4 links to answers.acrenkey.com and the blog.
11. P0: sources, with official links and the date checked.
12. P0: the disclaimer (indicative, plus the CA or lawyer note).
13. P2: a soft CTA ("Talk to an advisor"), not above the tool.

Quality checks:
- [ ] Original value beyond the tool: a worked example, a local angle, a scenario table. Not a copy of competitor text.
- [ ] Word count is typically 800-2,000 of useful text. Never pad. Thin pages (under ~400 words of text) get flagged.
- [ ] Written in plain Indian English, human tone, no AI tells, short paragraphs.
- [ ] Every number in the text matches what the tool outputs for the same inputs (test it).
- [ ] Dates are current. A rate table older than 90 days gets FIXed.

## 5. E-E-A-T and trust signals
- [ ] Byline: "By Gaurav Mongia, acre&key", linked to the author page. A "Reviewed by" line only if a real CA or lawyer reviewed it (never invent one).
- [ ] An author page with bio, LinkedIn and expertise. The Person schema sameAs points to LinkedIn.
- [ ] An About/Contact page linked in the footer, with the real address, RERA registration number and legal name.
- [ ] A methodology note: "How we calculate", with sources.
- [ ] No fake reviews, ratings or user counts. No AggregateRating schema unless the reviews are real and shown on the page.
- [ ] Privacy note if the calculator collects any data. The lead form isn't required to see the results.

## 6. Schema / structured data (P0, JSON-LD in the <head> or body)
Every calculator page uses one @graph containing:
- [ ] WebPage (or a WebPage subtype) with @id, url, name, description, inLanguage en-IN, datePublished, dateModified, isPartOf → WebSite, breadcrumb → BreadcrumbList @id, author/reviewedBy where real.
- [ ] WebApplication (or SoftwareApplication) with name, url, applicationCategory "FinanceApplication", operatingSystem "Any", browserRequirements "Requires JavaScript", offers {price 0, priceCurrency INR}, and publisher → Organization @id.
- [ ] BreadcrumbList that matches the visible breadcrumb.
- [ ] FAQPage whose Q&A text matches the visible FAQs word for word, with no HTML links inside the text. Note that Google shows FAQ rich results only for limited sites, but FAQPage still helps AI engines parse Q&A, so keep it.
- [ ] Organization (or RealEstateAgent) with @id (site-wide, referenced, not duplicated in full on every page), name "acre&key", legalName, url, logo, address, sameAs (LinkedIn and other real profiles).
- [ ] Person (author) with @id, name, jobTitle, sameAs.
- [ ] Optional HowTo for the "how to use" steps (no rich result now, but useful for parsing).
- [ ] Optional Dataset for rate tables, if they're original data.
- [ ] Hub (/calculators/): CollectionPage plus an ItemList of all 75 (position, name, url), plus BreadcrumbList. Not WebApplication.
Validation:
- [ ] Valid JSON, passes the Schema.org validator and Google Rich Results Test, and has no errors.
- [ ] Every value in the schema is visible on the page (no hidden claims).
- [ ] dateModified changes only on real content changes.

## 7. Technical SEO (P0 unless noted)
- [ ] Server-rendered or pre-rendered HTML contains the H1, lead, headings, body text, FAQs, links and schema. Check with curl or "View source", not the browser DOM. JS may run the calculator, but the content must not depend on JS.
- [ ] The calculator has default inputs so the result shows in the HTML on first load (e.g. ₹80L, 8.5%, 20 years).
- [ ] Status 200, no redirect chains, and http → https and non-trailing → trailing-slash redirects are 301.
- [ ] Listed in the XML sitemap with an accurate lastmod. The sitemap is referenced in robots.txt and submitted in Search Console.
- [ ] robots.txt doesn't block the page, its JS or CSS.
- [ ] Indexed: check with URL Inspection in Search Console, and request indexing after launch or major changes.
- [ ] No duplicate URLs (parameters, uppercase, index.html). Use the canonical plus redirects.
- [ ] Core Web Vitals on mobile ("good" at the 75th percentile): LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. Check PageSpeed Insights (field and lab) and the Search Console CWV report.
  - [ ] JS for the calculator is deferred and small. No layout shift when results render (reserve the space).
  - [ ] Fonts preloaded, font-display swap. Images in WebP/AVIF with width and height set, lazy-loaded below the fold.
  - [ ] CSS critical path inlined or small. No unused heavy libraries.
- [ ] Mobile-first: inputs are large and tappable (48px), numeric keyboard on number fields (inputmode="decimal"), and no horizontal scroll.
- [ ] HTTPS with a valid certificate, HSTS, and no mixed content.
- [ ] Clean HTML: no broken links (4xx/5xx), no orphan pages (each page has 3 or more incoming internal links).
- [ ] Cloudflare/CDN cache purged after updates. Check that the live HTML matches the repo.
- [ ] P1: hreflang isn't needed (single language), so don't add it wrongly.
- [ ] P1: a 404 page exists and returns status 404 (not a soft 404).

## 8. Accessibility (helps UX and rankings indirectly) (P1)
- [ ] Every input has a <label>, units are shown, and errors are announced (aria-live on the results).
- [ ] Contrast at least 4.5:1, keyboard-operable, visible focus.
- [ ] Tables have <th> and a caption. Charts have a text summary.
- [ ] Icons aren't used as text (e.g. "expand_more" or "arrow_forward" mustn't appear as visible text when the icon font fails).

## 9. Internal linking and site architecture (P0/P1)
- [ ] Hub-and-spoke: /calculators/ links to all 75 with descriptive anchors. Each calculator links back to the hub and to its category section.
- [ ] Clusters (e.g. Loans & Finance, Costs & Taxes, Investment & Returns, Evaluation, Location, Construction & Interiors, Ownership, Tax, Planning). Each has a category section or page with an intro.
- [ ] Each calculator links to 3-6 siblings plus the next step in the journey (Affordability, then EMI, then Stamp Duty, then Total Cost, then Rent vs Buy).
- [ ] Contextual links from relevant answers.acrenkey.com pages and blog posts into the calculator, and back.
- [ ] Anchor text is descriptive ("stamp duty calculator for Karnataka"), not "click here". Vary it naturally.
- [ ] Each page is within 3 clicks of the homepage. The homepage or nav links to the hub.

## 10. AEO / GEO (AI answer engines)
- [ ] The direct answer is in the first 60 words, self-contained and quotable, with a number in it where relevant.
- [ ] Clear definitions ("EMI is…"), the formula in plain text, and one worked example. AI engines quote these.
- [ ] Question-style H2s and FAQs with short, standalone answers (40-80 words), each answer repeating the subject (not "it").
- [ ] Facts carry an inline source and date ("RBI repo rate 5.50% as of <date>, per RBI"). Stats with sources get cited more.
- [ ] Bengaluru entities named consistently (Bengaluru/Bangalore, BBMP/GBA, BDA, K-RERA, Kaveri 2.0, IGR Karnataka) to build entity relevance.
- [ ] Consistent brand entity: same name, logo, address, sameAs across the site, schema, Google Business Profile, LinkedIn and directories.
- [ ] Tables in HTML with clear headers, since AI and Google extract them.
- [ ] llms.txt (optional, P2) listing the calculators hub and key pages.
- [ ] AI crawler access: robots.txt allows Googlebot and Bingbot, and decides deliberately on GPTBot, PerplexityBot, ClaudeBot and Google-Extended (allow them if AI citations are a goal).
- [ ] Monthly test: ask ChatGPT, Perplexity, Gemini and Google AI Mode the page's top 5 queries, and log whether acre&key is cited and who is cited instead.

## 11. Off-page and authority
- [ ] Google Business Profile: complete, with the same name, address and phone (NAP), category, and website link. Posts link to popular calculators occasionally.
- [ ] Consistent citations (NAP) on Indian directories and real estate listings where acre&key has a genuine presence.
- [ ] Link-earning assets: rate tables updated monthly, an embeddable calculator widget (with an attribution link), original data (e.g. "Bengaluru stamp duty and registration cost index").
- [ ] Digital PR: pitch calculator-based data stories to Bengaluru and real estate media (Deccan Herald, The Hindu Bengaluru, Moneycontrol, ET Realty), with figures from official sources.
- [ ] Community: genuinely helpful Quora/Reddit/LinkedIn answers that link to a calculator only where it directly answers the question (no spam, follow platform rules).
- [ ] Partnerships: CA, lawyer or home-loan DSA blogs referencing the calculators (no paid links, since paid links violate Google's spam policies).
- [ ] Brand mentions (unlinked) are valuable for AI engines too. Track them.
- [ ] Never: PBNs, link exchanges at scale, bought links, or spammy directories.

## 12. Spam-policy guardrails (P0)
- [ ] No scaled near-duplicate pages: each of the 75 must have unique formula, example, FAQs and local angle (not the same template with the keyword swapped).
- [ ] No doorway pages (e.g. "EMI calculator Whitefield", "EMI calculator HSR" with identical content). Only create area variants if the content truly differs (area-specific rates or data).
- [ ] No hidden text, keyword stuffing, or schema content not visible on the page.
- [ ] No auto-generated text without human review.

## 13. Measurement (P1)
- [ ] Search Console: the property is verified, the sitemap is submitted, the page is indexed, and queries, CTR and position are tracked per calculator.
- [ ] GA4 events: calculator_used (on first calculation), inputs_changed, result_shared/printed, cta_clicked, related_calculator_click.
- [ ] Bing Webmaster Tools set up (it also feeds ChatGPT search and Copilot).
- [ ] A monthly report per page: impressions, clicks, CTR, average position, top queries, CWV status, AI-citation check, and last rate-check date.
- [ ] CTR under ~2% at an average position of 1-10: rewrite the title and meta.

## 14. Maintenance cadence
- Monthly: bank rates, the RBI repo rate, and rate-table dates. Run the AI-citation test and check for broken links.
- On every Budget, GST Council or Karnataka stamp-duty change: update the affected calculators within 48 hours, and update dateModified and "Last updated".
- Quarterly: a full re-audit with this skill, a content refresh for pages ranked 5-20, and new FAQs from Search Console queries.

---

## Page template (order of blocks)
1. Breadcrumb
2. H1 + "Last updated" + byline
3. Direct answer (40-60 words, with formula and example)
4. Calculator (default inputs, result visible)
5. How to use (steps)
6. Formula and method (worked Bengaluru example)
7. Scenario table
8. What the result means / next decision
9. Bengaluru-specific notes (sourced)
10. Assumptions and limits
11. FAQs (5-8)
12. Related calculators and guides
13. Sources (official, dated)
14. Disclaimer (indicative + CA/lawyer note)
15. Soft CTA

## Launch gate (all must be YES)
- Brand and compliance rules pass, and every rate is official and dated.
- Title, meta and canonical are unique and correct, with one H1 and a direct answer.
- Content renders in raw HTML (curl test), with no placeholders.
- Schema @graph is valid, matches the page, and FAQ text matches.
- Mobile CWV pass (or lab LCP < 2.5s, CLS < 0.1, with no long tasks on input).
- At least 3 incoming internal links, plus hub, sitemap and Search Console indexing requested.
- The tool's output matches the worked example, tested with 3 input sets, including edge cases (0, max, decimals).

## Audit output format
For each page, give a table with: Section | Item | Status (PASS/FIX/N/A) | Priority | Evidence (URL, snippet, metric) | Fix (exact replacement text or code). End with the top 5 fixes ranked by impact. Never invent metrics; if a tool or figure wasn't checked, write "not checked".
