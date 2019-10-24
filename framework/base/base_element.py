from framework.browser.browser import Browser
from framework.utils.logger import debug
from framework.utils.waiter import wait_for_clickable

browser = Browser()


class BaseElement:
    def __init__(self, by, loc, name):
        self.__by = by
        self.__loc = loc
        self.__name = f"{type(self).__name__}, '{name}'"
        debug(f"Creating instance of {self.__name}")

    def is_displayed(self):
        return self.web_element.is_displayed()

    def click(self):
        self.web_element.click()

    def wait_and_click(self):
        wait_for_clickable(self.by, self.__loc)
        self.web_element.click()

    def get_attribute(self, attribute):
        return self.web_element.get_attribute(attribute)

    def get_text(self):
        return self.web_element.text

    @property
    def web_element(self):
        return browser.driver.find_element(self.by, self.loc)

    @property
    def by(self):
        return self.__by

    @property
    def loc(self):
        return self.__loc
