from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class VerifyResults(Page):
    CART_PRICE_CSS_SELECTOR = (By.CSS_SELECTOR, '.cart-price')
    CART_SUBTOTAL_XPATH = (By.XPATH, "//*[@class='cart-subtotal']")
    CHECK_OUT_PAGE_LINK_TEXT = (By.LINK_TEXT, 'CHECKOUT DETAILS')
    EMPTY_CART_XPATH = (By.XPATH, "//p[contains(text(), 'Your cart is currently empty.')]")
    ITEMS_AMOUNT_CSS_SELECTOR = (By.CSS_SELECTOR, '.cart-icon strong')
    HOVER_EMPTY_CART_XPATH = (By.XPATH, "//p[contains(text(), 'No products in the cart.')]")
    SHOPPING_CART_PAGE_LINK_TEXT = (By.LINK_TEXT, 'SHOPPING CART')
    SUBTOTAL_PRICE_CSS_SELECTOR = (By.CSS_SELECTOR, '.woocommerce-mini-cart__total')

    def verify_results(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_XPATH)

    def verify_hover_results(self, expected_text):
        self.verify_text(expected_text, *self.HOVER_EMPTY_CART_XPATH)

    def verify_subtotal(self, expected_price):
        self.verify_text(expected_price, *self.CART_PRICE_CSS_SELECTOR)

    def verify_items_amount(self, expected_amount):
        self.verify_text(expected_amount, *self.ITEMS_AMOUNT_CSS_SELECTOR)

    def verify_product(self, expected_products):
        self.verify_text(expected_products, *self.CART_SUBTOTAL_XPATH)

    def verify_shopping_cart_page(self, expected_text):
        self.verify_text(expected_text, *self.SHOPPING_CART_PAGE_LINK_TEXT)

    def verify_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.HOVER_EMPTY_CART_XPATH)

    def verify_checkout_page(self, expected_text):
        self.verify_text(expected_text, *self.CHECK_OUT_PAGE_LINK_TEXT)