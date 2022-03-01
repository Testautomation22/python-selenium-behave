from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductsPage(Page):
    #Locators
    CLOSE_QUICK_VIEW_BUTTON_CSS_SELECTOR = (By.CSS_SELECTOR, '.mfp-close')
    IPHONE_SE_QUICK_VIEW_CSS_SELECTOR = (By.XPATH, "(//a[@href='#quick-view'])[2]")
    IPHONE_SE_XPATH = (By.XPATH, "(//*[@class='image-fade_in_back'])[2]")
    NEXT_PREVIOUS_ARROWS_XPATH = (By.XPATH, "(//*[@type='button'])[2]")
    PAGE_DOTS_CSS_SELECTOR = (By.CSS_SELECTOR, ".flickity-page-dots")

    def hover_iphone_se(self):
        self.hover(*self.IPHONE_SE_XPATH)

    def click_quick_view(self):
        self.click_element(*self.IPHONE_SE_QUICK_VIEW_CSS_SELECTOR)

    def close_quick_view(self):
        self.click_element(*self.CLOSE_QUICK_VIEW_BUTTON_CSS_SELECTOR)

    def click_arrows(self):
        self.click_element(*self.NEXT_PREVIOUS_ARROWS_XPATH)

    def click_page_dots(self):
        self.click_element(*self.PAGE_DOTS_CSS_SELECTOR)
