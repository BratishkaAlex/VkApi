from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from framework.browser.browser import Browser
from framework.custom_waites.mail_was_sent import mail_was_sent
from resources import config


class Waiter:
    @staticmethod
    def implicit_wait(timeout):
        Browser.get_driver().implicitly_wait(timeout)

    @staticmethod
    def wait_for_clickable(by, element):
        WebDriverWait(Browser.get_driver(), config.Timeout).until(
            expected_conditions.element_to_be_clickable((by, element)))

    @staticmethod
    def wait_until_captcha_is_visible(by, element):
        WebDriverWait(Browser.get_driver(), config.Timeout_for_captcha).until(
            expected_conditions.invisibility_of_element_located((by, element)))

    @staticmethod
    def wait_while_email_received(mail):
        WebDriverWait(Browser.get_driver(), config.Timeout_for_email, poll_frequency=1).until(
            mail_was_sent(mail))

    @staticmethod
    def wait_for_element_presence(by, element):
        WebDriverWait(Browser.get_driver(), config.Timeout).until(
            expected_conditions.presence_of_element_located((by, element)))

    @staticmethod
    def wait_for_element_disappearing(by, element):
        WebDriverWait(Browser.get_driver(), config.Timeout).until(
            expected_conditions.invisibility_of_element_located((by, element)))
