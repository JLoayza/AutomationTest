# from pages.login_page import ConnectLoginPage
# from pages.dashboard_page import ConnectDashboardPage
# import time
#
# def test_select_venue(browser):
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
#     #assert dashboard_page.getTitle() == "Appetize Connect - Dashboard - Dashboard"
#
#     dashboard_page.selectSuites()
#     time.sleep(10)