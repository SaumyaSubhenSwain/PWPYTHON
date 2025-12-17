from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")  #passing URL

    myUrl= page.url
    print("URL of the application:", myUrl)

    expect(page).to_have_url("http://www.automationpractice.pl/index.php") #expected url

def test_verifyTitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")

    myTitle = page.title()
    print("Title of the page: ", myTitle)

    expect(page).to_have_title("My Shop")

