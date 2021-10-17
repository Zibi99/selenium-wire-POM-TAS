from PageObjects.BasePage import BasePage


class Page_Object1(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.coockies = ("//button[@id='onetrust-accept-btn-handler']", "xpath")