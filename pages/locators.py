from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "[name=\"login_submit\"]")
    FORM_REGISTER = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "[type = \"submit\"][value = \"Add to basket\"]")
    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCESS_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1) .alertinner > strong")


class BasketPageLocators:
    BASKET_HAT_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_EMPTY_BUTTON = (By.CSS_SELECTOR, "col-sm-4.col-sm-offset-8")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")
