from playwright.sync_api import Page, expect


def test_css_locators_in_playwright(page:Page):
    # Launch the URL
    page.goto("https://demowebshop.tricentis.com/")

    # logo (CSS locator)
    relative_logo= page.locator("img[alt='Tricentis Demo Web Shop']")
    expect(relative_logo).to_be_visible()

    # Products containing "computer" in href attribute
    products = page.locator("h2>a[href*='computer']")     # [href*="computer"] mimics XPath contains()
    print("Products count:", products.count())
    expect(products).to_have_count(4)

    print("First Computer product:", products.first.text_content())
    print("N-th Computer product:", products.nth(1).text_content())

    # Capture the product titles and print them