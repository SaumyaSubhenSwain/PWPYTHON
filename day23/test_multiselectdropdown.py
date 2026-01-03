from cProfile import label

from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from teh dropdown - 3 ways

    # page.locator("#colors").select_option(["Red", "Blue", "Green"])       # By label
    page.locator("#colors").select_option(label= ["Red", "Blue", "Green"])  # By label

    page.locator("#colors").select_option(value=["red","white","green"])    #By value
    page.locator("#colors").select_option(index=[2,4])      #by index

    dropdown_options = page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)


    page.wait_for_timeout(5000)