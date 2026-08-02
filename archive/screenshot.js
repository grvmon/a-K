const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  // iPhone X viewport
  await page.setViewport({
    width: 375,
    height: 812,
    isMobile: true,
    hasTouch: true
  });
  
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'mobile_qa_screenshot.png', fullPage: true });
  
  await browser.close();
  console.log("Screenshot saved to mobile_qa_screenshot.png");
})();
