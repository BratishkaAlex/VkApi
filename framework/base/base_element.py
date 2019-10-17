from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.waiter import Waiter


class BaseElement:
    def __init__(self, by, loc, name):
        self.__by = by
        self.__loc = loc
        self.__name = f"{name}, class {type(self).__name__} "
        Logger.debug(f"Creating instance of {self.__name}")

    def is_displayed(self):
        return self.web_element.is_displayed()

    def click(self):
        self.web_element.click()

    def wait_and_click(self):
        Waiter.wait_for_clickable(self.by, self.__loc)
        self.web_element.click()

    def get_attribute(self, attribute):
        return self.web_element.get_attribute(attribute)

    def get_text(self):
        return self.web_element.text

    @property
    def web_element(self):
        return Browser.get_driver().find_element(self.by, self.loc)

    @property
    def by(self):
        return self.__by

    @property
    def loc(self):
        return self.__loc
