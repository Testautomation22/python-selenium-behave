from pages.top_nav_menu import TopNav
from pages.home_page import HomePage
from pages.results import VerifyResults
from pages.products_page import ProductsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.top_nav = TopNav(self.driver)
        self.home = HomePage(self.driver)
        self.empty_cart_results = VerifyResults(self.driver)
        self.subtotal = VerifyResults(self.driver)
        self.items_amount = VerifyResults(self.driver)
        self.products = VerifyResults(self.driver)
        self.click_view = TopNav(self.driver)
        self.checkout_button = TopNav(self.driver)
        self.remove = TopNav(self.driver)
        self.verify_shopping_cart = VerifyResults(self.driver)
        self.verify_checkout= VerifyResults(self.driver)
        self.quick_view = ProductsPage(self.driver)
        self.click_close = ProductsPage(self.driver)
        self.hover_iphone = ProductsPage(self.driver)
        self.verify_prod= VerifyResults(self.driver)
        self.arrows = ProductsPage(self.driver)
        self.dots = ProductsPage(self.driver)