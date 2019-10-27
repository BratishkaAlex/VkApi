from selenium.webdriver.common.by import By

from app.page_object.forms.post_form import PostForm
from framework.base.base_page import BasePage
from framework.elements.link import Link


class MyPage(BasePage):
    def __init__(self):
        super().__init__(By.ID, "page_info_wrap")
        self.__post_form = PostForm()

    @property
    def post_form(self):
        return self.__post_form

    @property
    def owner_id(self):
        top_profile_link = self.top_profile_link.href
        return top_profile_link[top_profile_link.rfind("id") + len("id"):]

    @property
    def top_profile_link(self):
        return Link(By.ID, "top_profile_link", "Top profile")
