from pages.base_page import Page
from selenium.webdriver.common.by import By


class TopNav(Page):
    #Locators
    ADD_TO_CART_BUTTON_XPATH = (By.XPATH, "//button[@name='add-to-cart']")
    CART_ICON_CSS_SELECTOR = (By.CSS_SELECTOR, '.cart-icon')
    CART_PRICE_CSS_SELECTOR = (By.CSS_SELECTOR, '.cart-price')
    CHECK_OUT_BUTTON_XPATH = (By.XPATH, "//a[contains(text(), 'Checkout')]")
    MAC_CSS_SELECTOR = (By.CSS_SELECTOR, '#menu-item-468')
    MACBOOK_AIR_CSS_SELECTOR = (By.CSS_SELECTOR, '#menu-item-379')
    REMOVE_BUTTON_CSS_SELECTOR = (By.CSS_SELECTOR, '.remove_from_cart_button')
    VIEW_CART_XPATH = (By.XPATH, "//a[contains(text(), 'View cart')]")

    def click_cart_icon(self):
        self.click_element(*self.CART_ICON_CSS_SELECTOR)

    def hover_cart_icon(self):
        self.hover(*self.CART_ICON_CSS_SELECTOR)

    def hover_category(self):
        self.hover(*self.MAC_CSS_SELECTOR)

    def click_product(self):
        self.click_element(*self.MACBOOK_AIR_CSS_SELECTOR)

    def add_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BUTTON_XPATH)

    def click_view_cart_button(self):
        self.click_element(*self.VIEW_CART_XPATH)

    def click_remove_button(self):
        self.click_element(*self.REMOVE_BUTTON_CSS_SELECTOR)

    def click_checkout_button(self):
        self.click_element(*self.CHECK_OUT_BUTTON_XPATH )