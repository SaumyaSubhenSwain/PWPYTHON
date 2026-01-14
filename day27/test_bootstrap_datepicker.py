from playwright.sync_api import Page, expect


def select_checkin_date(page: Page, year: str, month: str, day: str):
    while True:
        checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()
        current_month, current_year= checkin_month_year.split()

        if current_month == month and current_year == year:
            break

        page.get_by_label("Next month").click()

    # Select valid dates only
    dates= page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()

    for i in range(dates.count()):
        if dates.nth(i).text_content() == day:
            dates.nth(i).click()
            break

def select_checkout_date(page: Page, year: str, month: str, day: str):
    while True:
        checkout_month_year= page.locator("h3[aria-live='polite']").nth(1).inner_text()
        current_month, current_year= checkout_month_year.split()

        if current_month == month and current_year == year:
            break

        page.get_by_label("Next month").click()

    dates= page.locator("table.b8fcb0c66a tbody").nth(1).locator("td").all()

    for i in range(dates.count()):
        if dates.nth(i).text_content() == day:
            dates.nth(i).click()
            break

def test_bootstrap_datepicker(page:Page):
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click()    # Clicked on the datepicker

    select_checkin_date(page,"2026","January","14")
    select_checkout_date(page,"2026","February","5")

    checkin_text= page.locator("span[data-testid ='date-display-field-start']").inner_text()
    checkout_text= page.locator("span[data-testid ='date-display-field-end']").inner_text()

    print("Check-in date====>", checkin_text)
    print("Check-out date====>",checkout_text)

    expect(page.locator("span[data-testid ='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid ='date-display-field-end']")).to_contain_text(checkout_text)