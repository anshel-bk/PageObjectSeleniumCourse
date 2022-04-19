import random
from datetime import time
from time import time
from time import sleep
from random import choice
from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from string import ascii_lowercase


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Слово login отсутствует в url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login button на сайте отсутствует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Registration button на сайте отсутствует"

    def register_new_user(self, email, password):
        assert self.send_keys_element(*LoginPageLocators.REGISTER_EMAIL, email), "Reg email is not exist"
        assert self.send_keys_element(*LoginPageLocators.REGISTER_PASSWORD, password), "Reg password is not exist"
        assert self.send_keys_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD,
                                      password), "Reg confirm password is not exist"
        try:
            assert self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        except Exception as ex:
            print("Ошибка", ex)

