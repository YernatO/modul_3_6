import pytest
import time
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose the language for the tests")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    time.sleep(30)