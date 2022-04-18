import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла

from pages.product_page import ProductPage
from .pages.main_page import MainPage,BasePage



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser,link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
    product_page.solve_quiz_and_get_code()

