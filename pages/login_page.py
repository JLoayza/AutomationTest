from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.venue_page import ConnectVenuesPage

from pages.base_page import BasePage


class ConnectLoginPage(BasePage):
    URL = 'https://connect.qa.appetize-dev.com'
    USERNAME_FIELD = (By.ID, 'login')
    PASSWORD_FIELD = (By.ID, 'password')

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)

    def log_in(self, username, password):
        self.type_on_element(self.USERNAME_FIELD, username)
        time.sleep(2)
        self.type_on_element(self.PASSWORD_FIELD, password + Keys.RETURN)
        time.sleep(2)
        return ConnectVenuesPage(self.browser)
