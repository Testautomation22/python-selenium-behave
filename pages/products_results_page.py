from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProdResults(Page):
    IPHONE_SE_XPATH = (By.XPATH, "//h1[contains(text(), 'iPhone SE')]")

    def verify_prod(self, expected_text):
        self.verify_text(expected_text, *self.IPHONE_SE_XPATH)