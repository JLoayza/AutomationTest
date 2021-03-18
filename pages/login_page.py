from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from generics.config import TestData
from pages.base_page import BasePage


class ConnectLoginPage(BasePage):

    USERNAME_FIELD = (By.ID, 'login')
    PASSWORD_FIELD = (By.ID, 'password')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    def log_in(self, username, password):
        self.type_on_element(self.USERNAME_FIELD, username)
        self.type_on_element(self.PASSWORD_FIELD, password + Keys.RETURN)
