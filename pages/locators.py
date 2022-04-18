from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR ,"[name=\"login_submit\"]")
    FORM_REGISTER = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "[type = \"submit\"][value = \"Add to basket\"]")

