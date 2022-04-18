from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def press_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_HAT_BUTTON)
        link.click()

    def basket_button_head_on_site(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_HAT_BUTTON), "Basket button на сайте в шапке отсутствует"

    def basket_head_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT), "Текст не совпадает с тем что должен быть при пустой корзине"
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_EMPTY_BUTTON), "Корзина по неизвестной причине не пуста"
