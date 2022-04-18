import time

from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_product_button()
        self.press_to_basket_page()

    def should_be_product_page_url(self):
        # реализуйте проверку на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "Слово promo отсутствует в url"

    def should_be_product_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button на сайте отсутствует"

    def press_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

