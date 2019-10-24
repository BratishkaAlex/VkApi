from app.page_object.forms.side_bar import SideBar
from framework.base.base_page import BasePage


class NewsPage(BasePage):
    def __init__(self, locator_type, locator):
        super().__init__(locator_type, locator)
        self.__side_bar = SideBar()

    @property
    def side_bar(self):
        return self.__side_bar
