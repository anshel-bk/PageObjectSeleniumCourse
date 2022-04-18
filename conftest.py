import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser): # парсер инфы из параметров
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function") # формирует фикстуру/ декоратор для работы с браузером
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()