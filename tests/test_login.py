from pages.login_page import ConnectLoginPage
from pages.venue_page import ConnectVenuesPage

# def test_connect_login(browser):
#
#     #Test DATA
#     USER = 'jloayza'
#     PASS = '@ppetiz3!'
#
#     FAILED_USER = 'jlayza'
#
#     login_page = ConnectLoginPage(browser)
#     login_page.load()
#     venue_page = login_page.log_in(USER, PASS)
#
#     assert venue_page.getTitle() == "Appetize Connect - Venues"
#
#
#
# def test_failed_login(browser):
#     # Test DATA
#     USER = 'jlayza'
#     PASS = '@ppetiz3!'
#
#     login_page = ConnectLoginPage(browser)
#     login_page.load()
#     venue_page = login_page.log_in(USER, PASS)
#
#     assert venue_page.getTitle() == "Appetize Connect - Login"
#
# def test_bad_password(browser):
#     # Test DATA
#     USER = 'jloayza'
#     PASS = 'thisisatest'
#
#     login_page = ConnectLoginPage(browser)
#     login_page.load()
#     venue_page = login_page.log_in(USER, PASS)
#
#     assert venue_page.getTitle() == "Appetize Connect - Login"

