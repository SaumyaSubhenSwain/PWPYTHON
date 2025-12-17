from playwright.sync_api import Page, expect


def test_verifypwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    logo= page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()