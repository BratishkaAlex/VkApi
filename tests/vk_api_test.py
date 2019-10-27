import os

from app.enums.side_bar_items import SideBarItems
from app.page_object.pages.my_page import MyPage
from app.page_object.pages.news_page import NewsPage
from app.steps.steps import *
from framework.browser.browser import Browser
from framework.utils.logger import step
from framework.utils.random_utils import get_random_string
from framework.vk_api.enums.vk_items import VkItems
from framework.vk_api.vk_api_utils import *
from resources import config, vk_config

browser = Browser()


class TestVkApi:
    counter = 1

    def setup_method(self):
        if os.path.exists(config.PATH_TO_DOWNLOAD_PICTURE):
            os.remove(config.PATH_TO_DOWNLOAD_PICTURE)
        browser.set_implicitly_wait(config.TIMEOUT)
        browser.maximize()

    def teardown_method(self):
        browser.close()

    def test_vk(self):
        browser.enter_url(config.URL)
        log_in(vk_config.LOGIN, vk_config.PASSWORD)
        news_page = NewsPage()
        news_page.side_bar.navigate_to(SideBarItems.MY_PAGE)
        my_page = MyPage()
        random_string = get_random_string()
        owner_id = my_page.owner_id

        step("Creating post with random line and getting post's id", self.counter)
        self.counter += 1
        post_id = create_new_post(random_string)
        assert is_new_post_existing(owner_id, random_string), "Post wasn't published"

        step("Editing post and upload picture", self.counter)
        self.counter += 1
        edited_random_string = "edited_%s" % random_string
        uploaded_photo_id = edit_post_and_attach_file(edited_random_string, post_id, config.PATH_TO_PICTURE)
        assert is_post_edited(owner_id, edited_random_string, uploaded_photo_id), "Post wasn't edited"

        step("Adding random comment to the post", self.counter)
        self.counter += 1
        random_comment = get_random_string()
        add_comment_to_post(random_comment, post_id)
        assert my_page.post_form.is_comment_added(owner_id, random_comment), "Comment wasn't added"

        step("Like edited post", self.counter)
        self.counter += 1
        my_page.post_form.like_post(post_id)
        assert is_item_liked_by_user(VkItems.POST, post_id, owner_id), "Post wasn't liked"

        step("Delete created post", self.counter)
        delete_post(post_id)
        assert is_post_deleted(owner_id, post_id), "Post wasn't deleted"
