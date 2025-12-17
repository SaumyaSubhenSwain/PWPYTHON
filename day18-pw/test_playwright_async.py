# Pre-requisite for Asynchrouns execution
# install  pytest-asyncio
# command:   pip install pytest-asyncio

import pytest
#from playwright.sync_api import Page, expect
from playwright.async_api import Page, expect, async_playwright


@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        myPage = await browser.new_page()
        await myPage.goto("http://www.automationpractice.pl/index.php")

        myUrl = myPage.url
        print("URL of the application:", myUrl)

        await expect(myPage).to_have_url("http://www.automationpractice.pl/index.php")  # expected url
