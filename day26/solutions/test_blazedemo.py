from playwright.sync_api import expect,Page


def test_blazedemo_flight_booking_select_lowest_price(page:Page):
    # 1. Navigate to BlazeDemo homepage
    page.goto("https://blazedemo.com/")

    # 2. Select departure city: Boston
    page.locator('select[name="fromPort"]').select_option("Boston")

    # 3. Select destination city: London
    page.locator('select[name="toPort"]').select_option("London")

    # 4. Click on "Find Flights"
    page.locator('input[type="submit"]').click()

    # 5. Count number of rows (flights) in the table
    rows = page.locator("table.table tbody tr")
    row_count = rows.count()
    print("Number of flight rows:", row_count)

    # 6. Capture all prices into a list
    prices = []
    for i in range(row_count):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()  # 6th column
        prices.append(price_text)

    print("Flight Prices:", prices)

    # 7. Sort the prices (string sort)
    sorted_prices = sorted(prices)
    lowest_price = sorted_prices[0]
    print("Lowest Price:", lowest_price) # Printing lowest price


    # 8. Find row with lowest price and click "Choose This Flight"
    for i in range(row_count):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()
        if price_text == lowest_price:
            rows.nth(i).locator('td input[type="submit"]').click()
            break

    # 9. Fill passenger details on the purchase page
    page.locator("#inputName").fill("John")
    page.locator("#address").fill("1403 American Beauty Ln")
    page.locator("#city").fill("Columbus")
    page.locator("#state").fill("OH")
    page.locator("#zipCode").fill("43240")
    page.locator("#cardType").select_option("American Express")
    page.locator("#creditCardNumber").fill("6789067345231267")
    page.locator("#creditCardMonth").fill("10")
    page.locator("#creditCardYear").fill("2024")
    page.locator("#nameOnCard").fill("John Canedy")

    # Click on Purchase Flight
    page.locator('input[value="Purchase Flight"]').click()

    # 10. Validate success message
    expect(page.locator("h1")).to_have_text("Thank you for your purchase today!")

    page.wait_for_timeout(3000)
