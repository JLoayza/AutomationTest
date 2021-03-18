from selenium.webdriver.support.wait import WebDriverWait

from generics.config import TestData

from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element):
        return WebDriverWait(self.driver, TestData.WAIT_TIME).until(ec.visibility_of_element_located(element))

    def get_elements(self, element):
        return self.driver.find_elements(*element)

    def click_on_element(self, element):
        self.get_element(element).click()

    def type_on_element(self, element, value):
        elem = self.get_element(element)
        elem.clear()
        elem.send_keys(value)