import time

from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_product_button()
        self.press_to_basket_page()

    def should_be_expected_result(self):
        self.should_be_name_product_add_basket()
        self.should_be_price_product_add_basket()


    def should_be_product_page_url(self):
        # реализуйте проверку на корректный url адрес
        assert "catalogue" in self.browser.current_url, "Слово catalogue отсутствует в url"

    def should_be_product_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button на сайте отсутствует"

    def press_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_name_product_add_basket(self):
        message_add_book = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert message_add_book == book_name, f"Неверное имя книги в корзине {message_add_book} а должно быть {book_name}"

    def should_be_price_product_add_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_size = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == cart_size, f"цена {book_price} не равна {cart_size}"
