from selenium.webdriver.common.by import By
from pages.dashboard_page import ConnectDashboardPage

from pages.base_page import BasePage


class ConnectVenuesPage(BasePage):
    VENUE = (By.CSS_SELECTOR, 'input.form-control.js-listing-filter')
    LOGIN_VENUE = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.driver.title

    def selectVenue(self, venue):
        self.type_on_element(self.VENUE, venue)
        self.click_on_element(self.LOGIN_VENUE)
        return ConnectDashboardPage(self.driver)
