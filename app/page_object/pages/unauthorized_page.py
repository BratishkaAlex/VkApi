from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input_field import InputField


class UnauthorizedPage(BasePage):
    def __init__(self, locator_type, locator):
        super().__init__(locator_type, locator)

    def type_login(self, login):
        self.input_login_field.send_keys(login)

    def type_password(self, password):
        self.input_password_field.send_keys(password)

    def click_submit(self):
        self.submit_button.click()

    @property
    def input_login_field(self):
        return InputField(By.ID, "index_email", "Login")

    @property
    def input_password_field(self):
        return InputField(By.ID, "index_pass", "Password")

    @property
    def submit_button(self):
        return Button(By.ID, "index_login_button", "Submit credentials")
