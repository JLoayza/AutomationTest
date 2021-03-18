import pytest
from selenium.webdriver import Chrome, Firefox
from generics.config import TestData
from pages.login_page import ConnectLoginPage


@pytest.fixture(scope='class')
def init_driver(request):
    # Initialize ChromeDriver
    if TestData.BROWSER == 'chrome':
        web_driver = Chrome('/Users/juan.loayza/Documents/chromedriver')
    elif TestData.BROWSER == 'firefox':
        web_driver = Firefox()
    else:
        raise Exception(f'"{TestData.BROWSER}" is not a supported browser')

    request.cls.driver = web_driver
    web_driver.maximize_window()
    login_page = ConnectLoginPage(web_driver)
    login_page.log_in(TestData.USER, TestData.PASS)

    # Return the driver object at the end of setup
    yield web_driver

    # For cleanup, quit the driver
    web_driver.quit()
