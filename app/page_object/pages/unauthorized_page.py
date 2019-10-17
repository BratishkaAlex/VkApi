from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.input_field import InputField


class UnauthorizedPage:
    input_login_loc = "index_email"
    input_password_loc = "index_pass"
    submit_button_loc = "index_login_button"

    def type_login(self, login):
        self.input_login_field.send_keys(login)

    def type_password(self, password):
        self.input_password_field.send_keys(password)

    def click_submit(self):
        self.submit_button.click()

    @property
    def input_login_field(self):
        return InputField(By.ID, self.input_login_loc, "Input field for login")

    @property
    def input_password_field(self):
        return InputField(By.ID, self.input_password_loc, "Input field for password")

    @property
    def submit_button(self):
        return Button(By.ID, self.submit_button_loc, "Submit button")
