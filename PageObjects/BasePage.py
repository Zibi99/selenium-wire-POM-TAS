from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click_on_item(self, locator):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                        ((locator[1], locator[0]))).click()

    def get_page_item(self, locator):

        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                               ((locator[1], locator[0])))

    def quit(self):
        self.driver.quit()