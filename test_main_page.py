from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_button_head_on_site()
    basket_page.press_to_basket_page()
    basket_page.basket_head_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_button_head_on_site()
    basket_page.press_to_basket_page()
    basket_page.basket_head_empty()
