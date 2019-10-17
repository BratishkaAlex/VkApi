from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from framework.enums.web_element_attributes import WebElementAttributes
from framework.utils.comparison_utils import ComparisonUtils
from framework.utils.download_utils import DownloadUtils
from framework.utils.logger import Logger
from framework.utils.regex_utils import RegexUtils
from framework.utils.waiter import Waiter
from resources import config


class Steps:
    Uploaded_photo_url_regex = "http.+\\.jpg"
    Post_loc_pattern = "post%s_%s"

    @staticmethod
    def log_in(unauthorized_page, login, password):
        unauthorized_page.type_login(login)
        unauthorized_page.type_password(password)
        unauthorized_page.click_submit()

    @staticmethod
    def download_picture(uploaded_photo):
        uploaded_photo_style = uploaded_photo.get_attribute(WebElementAttributes.STYLE.value)
        uploaded_photo_url = RegexUtils.get_desired_line_from_string(Steps.Uploaded_photo_url_regex,
                                                                     uploaded_photo_style)
        DownloadUtils.download_file(uploaded_photo_url, config.Path_to_download_picture)

    @staticmethod
    def check_for_post_deleted(owner_id, post_id):
        try:
            Waiter.wait_for_element_disappearing(By.ID, Steps.Post_loc_pattern % (owner_id, post_id))
            return True
        except TimeoutException:
            Logger.error("Post wasn't deleted")
            return False

    @staticmethod
    def check_for_new_post_existing(post_form, owner_id, message):
        if owner_id in post_form.author_of_latest_post_href:
            return True and post_form.is_post_with_message_displayed(message)
        else:
            Logger.error("Post wasn't created")
            return False

    @staticmethod
    def check_for_post_editing(post_form, owner_id, message, uploaded_photo_id):
        Steps.download_picture(post_form.get_uploaded_photo(uploaded_photo_id))
        return ComparisonUtils.compare_two_images(config.Path_to_picture,
                                                  config.Path_to_download_picture) and \
               Steps.check_for_new_post_existing(post_form, owner_id, message)

    @staticmethod
    def check_for_comment_adding(post_form, owner_id, message):
        post_form.see_comments_under_created_post()
        return post_form.is_comment_added(owner_id, message)
