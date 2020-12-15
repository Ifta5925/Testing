from tests.acceptance.locators.home_page import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1.5000'


    @property
    def title(self):
        return self.driver.find_element(*HomePageLocators.TITLE)