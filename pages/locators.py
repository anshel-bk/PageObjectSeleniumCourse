from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR ,"[name=\"login_submit\"]")
    FORM_REGISTER = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "[type = \"submit\"][value = \"Add to basket\"]")
    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

