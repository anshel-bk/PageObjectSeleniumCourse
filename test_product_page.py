import math

import pytest
from selenium.common.exceptions import NoAlertPresentException # в начале файла

from pages.product_page import ProductPage
from .pages.main_page import MainPage,BasePage


# http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear первый проверочный линк
# http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019 второй линк

@pytest.mark.parametrize('offer', [i for i in range(0,10)])
@pytest.mark.xfail(reason="Не совпадающее название книги на оффере номер 7")
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.test_guest_cant_see_success_message()
    product_page.should_be_product_page()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_expected_result()

@pytest.mark.xfail(reason="Изначально выданы неверные условия")
def test_guest_see_messages(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.test_guest_cant_see_success_message()
    product_page.should_be_product_page()
    product_page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    product_page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()