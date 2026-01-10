from time import process_time_ns

from playwright.sync_api import Page, expect


def test_bootstrapdropdown(page:Page):
    # Launch the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login steps
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()

    page.wait_for_timeout(3000)
    # Click on PIM
    page.get_by_text("PIM").click()

    # Click on the job title dropdown
    page.locator("form i").nth(2).click()       #this will open options from the dropdown
    page.wait_for_timeout(4000)

    # capture all the option from dropdown
    options= page.locator("div[role='listbox'] span")

    count = options.count()
    print("Number of options in the dropdown:", count)

    expect(options).to_have_count(count)     #assertions for counting the options

    page.wait_for_timeout(4000)

    #print all the options
    print("All the options from the dropdown===> ", options.all_text_contents())

    #print all the options text using loop
    for i in range(count):
        print(options.nth(i).text_content())

    # select/click on specific option
    for i in range(count):
        text= options.nth(i).inner_text()
        print("option to be selected====> ", text)
        if text=="Automation Tester":
            print("Matching success.......")
            options.nth(i).click()
            break