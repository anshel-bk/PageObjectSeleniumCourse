import time

import faker
import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from .pages.main_page import MainPage


# # http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019 второй линк

@pytest.mark.auth_user
class TestUserAddToBasketFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()  # экземляп класса для фейковых данных
        email = f.email()  # фейковый эмэйл
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=NewYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.cant_see_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
        product_page = BasePage(browser, link)
        product_page.open()
        product_page = ProductPage(browser, link)
        product_page.cant_see_success_message()
        product_page.should_be_product_page()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_expected_result()


@pytest.mark.xfail(reason="Изначально выданы неверные условия")
def test_guest_see_messages(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.cant_see_success_message()
    product_page.should_be_product_page()
    product_page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    product_page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
