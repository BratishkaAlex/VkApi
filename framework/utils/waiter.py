from selenium.webdriver.support import expected_conditions

from framework.browser.browser import Browser
from framework.custom_waites.mail_was_sent import MailWasSent
from framework.models.web_driver_wait import DriverWait
from resources import config

browser = Browser()


def implicit_wait(timeout):
    browser.driver.implicitly_wait(timeout)


def wait_for_clickable(by, element):
    DriverWait(config.TIMEOUT).wait.until(
        expected_conditions.element_to_be_clickable((by, element)))


def wait_until_captcha_is_visible(by, element):
    DriverWait(config.TIMEOUT_FOR_CAPTCHA).wait.until(
        expected_conditions.invisibility_of_element_located((by, element)))


def wait_while_email_received(mail):
    DriverWait(config.TIMEOUT_FOR_EMAIL, 1).wait.until(
        MailWasSent(mail))


def wait_for_element_presence(by, element):
    DriverWait(config.TIMEOUT).wait.until(
        expected_conditions.presence_of_element_located((by, element)))


def wait_for_element_disappearing(by, element):
    DriverWait(config.TIMEOUT).wait.until(
        expected_conditions.invisibility_of_element_located((by, element)))
