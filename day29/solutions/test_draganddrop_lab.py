import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_drag_and_drop_demo_guru99(page:Page):

    # Navigate to the page
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    # Locate source and target elements
    from1 = page.locator("#credit2 a")       # BANK
    to1 = page.locator("#bank li")           # Debit Side

    from2 = page.locator("#credit1 a")       # SALES
    to2 = page.locator("#loan li")           # Credit Side

    from3 = page.locator("#fourth a").first  # 500 (1st)
    to3 = page.locator("#amt7 li")           # Debit Amount

    from4 = page.locator("#fourth a").nth(1) # 500 (2nd)
    to4 = page.locator("#amt8 li")           # Credit Amount

    # Perform drag and drop
    from1.drag_to(to1)
    from2.drag_to(to2)
    from3.drag_to(to3)
    from4.drag_to(to4)

    page.wait_for_timeout(3000)

    # Assert the "Perfect!" message is displayed
    perfect_text = page.locator("a:has-text('Perfect!')")
    expect(perfect_text).to_be_visible()

    page.wait_for_timeout(5000)


