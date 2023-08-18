from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    WELCOME_PANEL = (By.XPATH, "//*[contains(text(), 'Swag')]")
    INVENTORY_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")

    def __init__(self, driver):
        super().__init__(driver)

    def get_welcome_text(self):
        return self.get_text(self.WELCOME_PANEL)

    def click_invetory(self):
        self.do_click(self.INVENTORY_BUTTON)


