'''
tag id          tag#id
tag class       tag.class
tag attribute   tag[attribute=value]
tag class attribute     tag.class[attribute=value]

'''

import pytest
from playwright.sync_api import Page

def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    
