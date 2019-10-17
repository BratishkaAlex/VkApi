from selenium.webdriver.common.by import By

from app.page_object.forms.post_form import PostForm
from framework.elements.link import Link
from framework.enums.web_element_attributes import WebElementAttributes


class MyPage:
    Top_profile_link_loc = "top_profile_link"

    def __init__(self):
        self.__post_form = PostForm()

    @property
    def post_form(self):
        return self.__post_form

    @property
    def owner_id(self):
        top_profile_link_href = self.top_profile_link.get_attribute(WebElementAttributes.HREF.value)
        return top_profile_link_href[top_profile_link_href.rfind("id") + len("id"):]

    @property
    def top_profile_link(self):
        return Link(By.ID, self.Top_profile_link_loc, "Top profile link")
