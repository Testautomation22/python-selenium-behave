from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductsPage(Page):
    IPHONE_SE_QUICK_VIEW_CSS_SELECTOR = (By.XPATH, "(//a[@href='#quick-view'])[2]")
    CLOSE_QUICK_VIEW_BUTTON_CSS_SELECTOR = (By.CSS_SELECTOR, '.mfp-close')
    IPHONE_SE_XPATH = (By.XPATH, "(//div[@class='product-small box '])[2]")
    NEXT_PREVIOUS_ARROWS_CSS_SELECTOR = (By.CSS_SELECTOR, '.flickity-button-icon')
    #LEFT_ARROW_XPATH = (By.XPATH, "(//*[@class='flickity-button-icon'])[1]")

    #RIGHT_ARROW_XPATH = (By.XPATH, "(//*[@class='flickity-button-icon'])[2]")
    PAGE_DOTS_CSS_SELECTOR = (By.CSS_SELECTOR, ".flickity-page-dots")

    def hover_iphone_se(self):
        self.hover(*self.IPHONE_SE_XPATH)

    def click_quick_view(self):
        self.click(*self.IPHONE_SE_QUICK_VIEW_CSS_SELECTOR)

    def close_quick_view(self):
        self.click(*self.CLOSE_QUICK_VIEW_BUTTON_CSS_SELECTOR)

    def click_arrows(self):
        self.click(*self.NEXT_PREVIOUS_ARROWS_CSS_SELECTOR)

    def click_page_dots(self):
        self.click(*self.PAGE_DOTS_CSS_SELECTOR)