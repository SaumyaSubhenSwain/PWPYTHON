import pytest
from playwright.sync_api import Page, expect

def select_date(page, target_year, target_month, target_date):
    # Keep clicking next until desired month & year are found
    while True:
        current_month = page.locator('span.ui-datepicker-month').inner_text()
        current_year = page.locator('span.ui-datepicker-year').inner_text()

        if current_month == target_month and current_year == target_year:
            break
        else:
            page.click('a.ui-datepicker-next')  # Click next button

    # Select the date
    all_dates = page.locator('table.ui-datepicker-calendar tbody td a').all()
    for date in all_dates:
        if date.inner_text() == target_date:
            date.click()
            break


def test_irctc_date_picker(page: Page):
    # 1. Navigate to IRCTC website
    page.goto("https://www.irctc.co.in/nget/train-search")

    # th will handle alert window opens on page( some times)
    if page.locator("button[class='btn btn-primary']").is_visible():
        page.locator("button[class='btn btn-primary']").click()

    # 2. Open the date picker
    date_input = page.locator("#jDate span input")
    date_input.click()

    # 3. Define target date values
    target_year = "2025"
    target_month = "October"
    target_date = "20"

    # 4. Select date
    select_date(page, target_year, target_month, target_date)

    # 5. Assert selected date is reflected in input field (contains day)
    selected_date = date_input.input_value()
    print("Selected date=====>:",selected_date)
    expect(date_input).to_have_value("20/10/2025")
