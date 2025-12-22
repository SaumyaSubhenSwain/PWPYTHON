'''
//button[text()='START' or text()='STOP']
//button[@name='start' or @name='stop']
//button[contains(@name,'st')]
//button[starts-with(@name,'st')]


'''


from playwright.sync_api import Page


def test_handle_dynamic_elements(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #
    #     for i in range(5):
    #         button=page.locator("//button[text()='START' or text()='STOP']")
    #         button.click()
    #         page.wait_for_timeout(2000)