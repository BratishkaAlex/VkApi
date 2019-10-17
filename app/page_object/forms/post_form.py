from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from framework.enums.web_element_attributes import WebElementAttributes


class PostForm:
    Author_loc = ".author"
    Button_to_see_comment_loc = "a.replies_next_main"
    Post_message_loc_pattern = "//div[contains(@class,'wall_post_text') and text()='%s']"
    Added_comment_loc_pattern = "//a[@class='author' and contains(@href,'%s')]//..//..//div[@class='wall_reply_text' " \
                                "and text()='%s']"
    Latest_post_like_loc_pattern = "//a[contains(@class,'_like') and contains(@onclick,'%s_%s')]"
    Uploaded_photo_loc_pattern = "//a[contains(@href,'%s')]"

    def get_uploaded_photo(self, uploaded_photo_id):
        return Button(By.XPATH, self.Uploaded_photo_loc_pattern % uploaded_photo_id, "Uploaded  photo")

    def see_comments_under_created_post(self):
        self.button_to_see_comments.click()

    def like_post(self, owner_id, post_id):
        self.get_like_button(owner_id, post_id).click()

    def is_post_with_message_displayed(self, message):
        return self.get_post_with_message(message).is_displayed()

    def is_comment_added(self, owner_id, message):
        return self.get_comment(owner_id, message).is_displayed()

    def get_like_button(self, owner_id, post_id):
        return Button(By.XPATH, self.Latest_post_like_loc_pattern % (owner_id, post_id), "Like icon for VK post")

    def get_post_with_message(self, message):
        return Label(By.XPATH, self.Post_message_loc_pattern % message, "Created post's test")

    def get_comment(self, owner_id, message):
        return Label(By.XPATH, self.Added_comment_loc_pattern % (owner_id, message),
                     "Added comment")

    @property
    def author_of_latest_post_href(self):
        return Label(By.CSS_SELECTOR, self.Author_loc, "Label with name of latest post's author").get_attribute(
            WebElementAttributes.HREF.value)

    @property
    def button_to_see_comments(self):
        return Button(By.CSS_SELECTOR, self.Button_to_see_comment_loc, "Button to see comments")
