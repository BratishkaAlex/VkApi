from app.page_object.forms.side_bar import SideBar


class NewsPage:
    def __init__(self):
        self.__side_bar = SideBar()

    @property
    def side_bar(self):
        return self.__side_bar
