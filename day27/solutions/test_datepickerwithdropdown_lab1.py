from playwright.sync_api import Page, expect

# Reusable function to select a date in the jQuery UI date picker
def select_date(page, target_year, target_month, target_date):
    # Select the year
    year_dropdown = page.locator("select.ui-datepicker-year")
    year_dropdown.select_option(label=target_year)

    # Select the month
    month_dropdown = page.locator("select.ui-datepicker-month")
    month_dropdown.select_option(label=target_month)

    # Click on the desired date
    all_dates = page.locator("table.ui-datepicker-calendar a")
    for i in range(all_dates.count()):
        date_element = all_dates.nth(i)
        if date_element.inner_text() == target_date:
            date_element.click()
            break

def test_date_picker_dropdowns(page: Page):
    # Go to the target page
    page.goto("https://testautomationpractice.blogspot.com/")

    # Click on the input field to open the date picker
    date_input = page.locator("#txtDate")
    date_input.click()

    # Select the date using helper
    select_date(page, '2026', 'May', '15')

    # Assert that the correct date is selected
    expect(date_input).to_have_value('15/05/2026')

    page.wait_for_timeout(5000)