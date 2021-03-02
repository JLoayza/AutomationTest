from selenium.webdriver import Chrome, Firefox

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.dashboard_page import ConnectDashboardPage

from pages.base_page import BasePage
import time

class ConnectVenuesPage(BasePage):
    VENUE = (By.CSS_SELECTOR, 'input.form-control.js-listing-filter')
    LOGIN_VENUE = (By.XPATH, "//button[normalize-space()='Login']")


    def __init__(self, browser):
        super().__init__(browser)

    def getTitle(self):
        return self.browser.title

    def selectVenue(self, venue):
        time.sleep(5)
        self.type_on_element(self.VENUE, venue)
        time.sleep(5)
        self.click_on_element(self.LOGIN_VENUE)
        return ConnectDashboardPage(self.browser)




        
