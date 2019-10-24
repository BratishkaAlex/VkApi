from selenium.webdriver.common.by import By

from app.page_object.forms.post_form import PostForm
from framework.base.base_page import BasePage
from framework.elements.link import Link


class MyPage(BasePage):
    def __init__(self, locator_type, locator):
        super().__init__(locator_type, locator)
        self.__post_form = PostForm()

    @property
    def post_form(self):
        return self.__post_form

    @property
    def owner_id(self):
        return self.top_profile_link.href[self.top_profile_link.href.rfind("id") + len("id"):]

    @property
    def top_profile_link(self):
        return Link(By.ID, "top_profile_link", "Top profile")
