const { chromium } = require('C:/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const path = require('path');
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'msedge'});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('file:///'+path.resolve('review/Investment_Review.html').replace(/\\/g,'/'));
 await page.waitForSelector('#tabs button');
 const buttons=await page.locator('#tabs button').evaluateAll(b=>b.map(x=>({key:x.dataset.k,label:x.textContent})));
 const checks=[];
 for(const b of buttons){
  await page.evaluate(k=>go(k),b.key);
  checks.push({key:b.key,characters:await page.locator('#app').innerText().then(s=>s.length)});
 }
 await page.evaluate(()=>go('risklab'));
 const riskRows=await page.locator('#app table').nth(1).locator('tbody tr').count();
 await page.locator('#capital').fill('50000');await page.locator('#capital').dispatchEvent('input');
 const capital=await page.locator('#capitalValue').innerText();
 const stress=await page.locator('#stressTable').innerText();
 await page.screenshot({path:'review/data/risk_dashboard.png',fullPage:false});
 await page.evaluate(()=>go('ledger'));await page.locator('#findStock').fill('NVDA');
 const search=await page.locator('#rowCount').innerText();
 await page.evaluate(()=>go('review'));await page.screenshot({path:'review/data/decision_dashboard.png',fullPage:false});
 await page.setViewportSize({width:390,height:844});await page.screenshot({path:'review/data/decision_mobile.png',fullPage:false});
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
 await page.setViewportSize({width:1440,height:1080});await page.evaluate(()=>go('facts'));
 const dossiers=await page.locator('[id^="co-"]').count();
 const results={tabs:buttons.length,checks,errors,riskRows,capital,stress,search,mobilePageOverflow:overflow,companyDossiers:dossiers};
 fs.writeFileSync('review/data/dashboard_validation.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results));
 await browser.close();if(errors.length||buttons.length!==23||dossiers!==14||search!=='1 companies')process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});

