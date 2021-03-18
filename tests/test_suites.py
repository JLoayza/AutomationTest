from generics.test_base import BaseTest
from pages.dashboard_page import ConnectDashboardPage
from pages.suites_page import SuitesPage


class TestSuites(BaseTest):

    def test_suites_page(self):
        dashboard_page = ConnectDashboardPage(self.driver)
        suites_page = dashboard_page.selectSuites()
        assert suites_page.getTitle() == "Appetize Connect - Suites - Suites"

    def test_create_suite(self):
        dashboard_page = ConnectDashboardPage(self.driver)
        suites_page = dashboard_page.selectSuites()
        suites_page.createSuite("Juan Test", "Suites")
        assert suites_page.getSuiteFromTable("Juan Test").text == "Juan Test"

    # def test_delete_suite(browser):
    #     USER = 'jloayza'
    #     PASS = '@ppetiz3!'
    #
    #     login_page = ConnectLoginPage(browser)
    #     login_page.load()
    #     venue_page = login_page.log_in(USER, PASS)
    #     dashboard_page = venue_page.selectVenue('1166')
    #
    #     time.sleep(5)
    #
    #     suites_page = dashboard_page.selectSuites()
    #     suites_page.deleteSuite("Juan Test")
    #     time.sleep(5)
    #     suitesList = suites_page.findSuitesInTable("Juan Test")
    #     assert len(suitesList) == 0
    #
    # def test_search_bar(browser):
    #     USER = 'jloayza'
    #     PASS = '@ppetiz3!'
    #
    #     login_page = ConnectLoginPage(browser)
    #     login_page.load()
    #     venue_page = login_page.log_in(USER, PASS)
    #     dashboard_page = venue_page.selectVenue('1166')
    #
    #     suites_page = dashboard_page.selectSuites()
    #     suitesList = suites_page.searchSuitesBySearchBar("Prueba")
    #     time.sleep(3)
    #     assert len(suitesList) > 0
    #
    # def test_search_bar_items_not_found(self):
    #
    #     dashboard_page = ConnectDashboardPage(self.driver)
    #     suites_page = dashboard_page.selectSuites()
    #     elem = suites_page.failedSearchBar('Juan')
    #     assert elem.text == 'No matching records found'
