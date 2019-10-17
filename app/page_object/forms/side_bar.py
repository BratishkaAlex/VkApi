from selenium.webdriver.common.by import By

from framework.elements.button import Button


class SideBar:
    def navigate_to(self, item):
        self.get_side_bar_item(item).click()

    def get_side_bar_item(self, item):
        return Button(By.ID, item.value, "Button to navigate to side bar item")
