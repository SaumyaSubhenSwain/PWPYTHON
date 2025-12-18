from playwright.sync_api import Page, expect


def test_verify_playwright_locators(page:Page):
    # Open local test page
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    # 1. get_by_alt_text() - locate image by alt attribute
    logo= page.get_by_alt_text("logo image")
    expect(logo).to_be_visible()

    # 2. get_by_text() - locate by text content (non-interactive element)
    expect(page.get_by_text("List item 1")).to_be_visible()
    expect(page.get_by_text("List item 2 with ")).to_be_visible()      # partial text
    expect(page.get_by_text("Special: Unique text identifier")).to_be_visible()

    # 3. get_by_role() - locate by ARIA role
    expect(page.get_by_role("button", name="Primary Action")).to_be_visible()
    expect(page.get_by_role("button", name="Toggle Button")).to_be_visible()
    expect(page.get_by_role("textbox", name="username")).to_be_visible()
    expect(page.get_by_role("checkbox", name=" Accept terms")).to_be_editable()

    # 4. get_by_label() - form controls
    page.get_by_label("Email Address:").fill("abc@gmail.com")
    page.get_by_label("Password:").fill("testing")
    page.get_by_label("Your Age:").fill("20")
    page.get_by_label(" Standard").check()
    page.get_by_label(" Express").check()

    # 5. get_by_placeholder() - locate by placeholder