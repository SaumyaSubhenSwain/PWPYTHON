from playwright.sync_api import Page, expect


def test_pagination_table(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages=True
    # file=open("C:\\Automation\\automationFiles\\myfile.txt",'a') # we will use this file for writing data
    while has_more_pages:
        rows=page.locator('#example tbody tr').all()
        for row in rows:
            print(row.inner_text())
            # file.write("\n" + row.inner_text()) # writing data into file
        page.wait_for_timeout(3000)

        next_button=page.locator("button[aria-label='Next']")
        is_disabled=next_button.get_attribute("class") # extract the value of class attribute

        if "disabled" in is_disabled:
            has_more_pages=False
        else:
            next_button.click()
    # file.close() # closing file

def test_filter_rows(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    dropdown=page.locator("#dt-length-0")
    dropdown.select_option(label="25")

    rows=page.locator('#example tbody tr')
    print("Number of rows Filtered:", rows.count())
    expect(rows).to_have_count(25)