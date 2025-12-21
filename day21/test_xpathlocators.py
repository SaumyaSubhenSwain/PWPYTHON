from playwright.sync_api import Page, expect


def test_xpath_locators(page:Page):
    #Launch the browser
    page.goto("https://demowebshop.tricentis.com/")

    # 1. Absolute xpath(full xpath)  - Not recomended
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    # 2. Relative xpath :    //tagname[@attribute='value']
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)