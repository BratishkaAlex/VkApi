from framework.browser.browser_factory import BrowserFactory
from framework.utils.logger import Logger


class Browser:
    driver = None

    @staticmethod
    def get_driver():
        if Browser.driver is None:
            Logger.debug("Creating webDriver instance")
            Browser.driver = BrowserFactory.get_driver()
        return Browser.driver

    @staticmethod
    def maximize():
        Logger.debug("Maximize browser window")
        Browser.get_driver().maximize_window()

    @staticmethod
    def enter_url(url):
        Logger.debug("Entering url")
        Browser.get_driver().get(url)

    @staticmethod
    def close_browser():
        Logger.debug("Close browser")
        Browser.get_driver().close()
        Browser.get_driver().quit()
        Browser.driver = None

    @staticmethod
    def get_current_url():
        Logger.debug("Get current browser")
        return Browser.get_driver().current_url
