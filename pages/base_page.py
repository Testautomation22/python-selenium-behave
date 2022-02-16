from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



class Page:
    # Driver init
    def __init__(self,driver):
        self.driver = driver

    # Get url
    def open_page(self,url):
        self.driver.get(url)

    # Click method
    def click(self, *locator):
        self.driver.find_element(*locator).click()

    # Hover method
    def hover(self, *locator):
        a = ActionChains(self.driver)
        m = self.driver.find_element(*locator)
        a.move_to_element(m).perform()

    # Assertion
    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f'Error! Expected {expected_text} but got {actual_text}'