from playwright.sync_api import Page

def test_verifyPageUrl(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
