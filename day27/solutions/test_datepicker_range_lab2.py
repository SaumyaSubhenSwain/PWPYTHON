from playwright.sync_api import Page, expect


def test_date_range_picker(page:Page):
    # Navigate to the site
    page.goto("https://testautomationpractice.blogspot.com/")

    # Fill in the start and end date using YYYY-MM-DD format (required for <input type="date">)
    page.locator("#start-date").fill("2026-01-16")
    page.locator("#end-date").fill("2026-09-05")

    # Assertion: Verify the values are correctly filled
    expect(page.locator("#start-date")).to_have_value("2026-01-16")
    expect(page.locator("#end-date")).to_have_value("2026-09-05")

    # Click on Submit button
    page.locator(".submit-btn").click()

    # Assertion: Check if submission resulted in any visible success message or confirmation
    success_message = page.locator("#result")
    expect(success_message).to_be_visible()

    # Print values for debug (optional)
    print("Start Date===>:", page.locator("#start-date").input_value())
    print("End Date===>:", page.locator("#end-date").input_value())

    page.wait_for_timeout(5000)