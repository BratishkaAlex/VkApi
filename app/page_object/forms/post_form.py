from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.link import Link
from framework.elements.photo import Photo
from framework.utils.logger import info


class PostForm:
    def see_comments_under_created_post(self):
        self.button_to_see_comments.click()

    def like_post(self, post_id):
        self.get_like_button(post_id).click()

    def is_post_with_message_displayed(self, message):
        return self.get_post_with_message(message).is_displayed()

    def is_comment_added(self, owner_id, message):
        info("Checking that comment was added")
        return self.get_comment(owner_id, message).is_displayed()

    def get_uploaded_photo(self, uploaded_photo_id):
        return Photo(By.XPATH, f"//a[contains(@href,'{uploaded_photo_id}')]", "Uploaded  photo")

    def get_like_button(self, post_id):
        return Button(By.XPATH, f"//a[contains(@class,'_like') and contains(@onclick,'{post_id}')]",
                      "Like icon for VK post")

    def get_post_with_message(self, message):
        return Label(By.XPATH, f"//div[contains(@class,'wall_post_text') and text()='{message}']",
                     "Created post's text")

    def get_comment(self, owner_id, message):
        self.see_comments_under_created_post()
        return Label(By.XPATH, f"//a[@class='author' and contains(@href,'{owner_id}')]//..//..//"
                               f"div[@class='wall_reply_text' and text()='{message}']", "Added comment")

    @property
    def author_of_latest_post_href(self):
        return Link(By.CSS_SELECTOR, ".author", "Name of latest post's author").href

    @property
    def button_to_see_comments(self):
        return Button(By.CSS_SELECTOR, "a.replies_next_main", "See comments")
