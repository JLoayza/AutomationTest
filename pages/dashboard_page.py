from selenium.webdriver import Chrome, Firefox

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.suites_page import SuitesPage

from pages.base_page import BasePage
import time


class ConnectDashboardPage(BasePage):
    SUITES_SECTION = (
        By.XPATH, "//a[@class='page-nav-link page-nav-suites js-subnav-toggle'][normalize-space()='Suites']")
    SUITES_SUB_SECTION = (By.XPATH, "//a[@class='page-subnav-link'][normalize-space()='Suites']")

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.driver.title

    def selectSuites(self):
        self.click_on_element(self.SUITES_SECTION)
        self.click_on_element(self.SUITES_SUB_SECTION)
        return SuitesPage(self.driver)
