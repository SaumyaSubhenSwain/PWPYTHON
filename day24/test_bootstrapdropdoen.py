from playwright.sync_api import Page

def test_bootstrapdropdown(page:Page):
    # Launch the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login steps
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()