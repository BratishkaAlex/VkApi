from framework.base.base_element import BaseElement
from framework.utils.waiter import Waiter


class InputField(BaseElement):
    def __init__(self, by, loc, name):
        super().__init__(by, loc, name)

    def send_keys(self, text):
        Waiter.wait_for_clickable(super().by, super().loc)
        super().web_element.send_keys(text)
