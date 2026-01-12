from playwright.sync_api import expect, Page

def test_pagination_table_lab_print_all_data_from_paginated_table(page:Page):
    # Navigate to the page
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all pagination links
    pages = page.locator("ul#pagination li").all()
    page_count=len(pages)
    print("Number of Pages:", page_count)

    for page_index in range(page_count):
        pages[page_index].click()  # Click on each page link

        # Get all rows in the current page
        rows = page.locator("table#productTable tbody tr").all()
        for row in rows:
            # Extract ID, Name, Price
            id = row.locator("td").nth(0).inner_text()
            name = row.locator("td").nth(1).inner_text()
            price = row.locator("td").nth(2).inner_text()

            # Click checkbox for each row
            row.locator("td").nth(3).locator("input").check()

            # Print row details
            print(id,"\t",name,"\t",price)

        page.wait_for_timeout(3000)
