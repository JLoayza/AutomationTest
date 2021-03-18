from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class SuitesPage(BasePage):
    CREATE = (By.XPATH, "//button[normalize-space()='Create']")
    NAME_FIELD = (By.ID, 'name')
    VENDOR_BUTTON = (By.XPATH, "//select[@name='vendor']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    TABLE = (By.XPATH, "//table[@class='table table-striped table-hover listing-table']")
    DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='OK']")
    SEARCH_BAR = (By.XPATH, "//input[@type='search' and @name='search_text']")

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.driver.title

    def createSuite(self, suiteName, suiteVendor):
        self.click_on_element(self.CREATE)
        self.type_on_element(self.NAME_FIELD, suiteName)
        select = Select(self.get_element(self.VENDOR_BUTTON))
        select.select_by_visible_text(suiteVendor)
        self.click_on_element(self.SAVE_BUTTON)

    def getSuiteFromTable(self, suiteName):
        xPathRoute = (By.XPATH, f"//tr[@class='js-edit' and contains(., '" + suiteName + "')]/td[1]")
        elem = self.get_element(xPathRoute)
        return elem

    def deleteSuite(self, suiteName):
        xPathRoute = (
        By.XPATH, f"//tbody/tr[@class='js-edit' and contains(., '" + suiteName + "')]/td[3]/div[1]/button[1]")
        self.click_on_element(xPathRoute)
        self.click_on_element(self.DELETE_BUTTON)

    def findSuitesInTable(self, suiteName):
        xPathRoute = (
        By.XPATH, f"//tbody/tr[@class='js-edit' and contains(., '" + suiteName + "')]/td[3]/div[1]/button[1]")
        suiteList = self.get_elements(xPathRoute)
        return suiteList

    def searchSuitesBySearchBar(self, phrase):
        self.type_on_element(self.SEARCH_BAR, phrase)
        xPathRoute = (By.XPATH, f"//tbody/tr[@class='js-edit' and contains(., '" + phrase + "')]")
        suitesList = self.get_elements(xPathRoute)
        return suitesList

    def failedSearchBar(self, phrase):
        self.type_on_element(self.SEARCH_BAR, phrase)
        xPathRoute = (By.XPATH, f"//td[@class='table-message' and contains(., 'No matching records found')]")
        message = self.get_element(xPathRoute)
        return message
