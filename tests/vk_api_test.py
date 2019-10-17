import os

from app.enums.side_bar_items import SideBarItems
from app.page_object.pages.my_page import MyPage
from app.page_object.pages.news_page import NewsPage
from app.page_object.pages.unauthorized_page import UnauthorizedPage
from app.steps.steps import Steps
from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.random_utils import RandomUtils
from framework.utils.waiter import Waiter
from framework.vk_api.enums.vk_items import VkItems
from framework.vk_api.vk_api_utils import VkApiUtils
from resources import config, vk_config


class TestVkApi:
    counter = 1

    def setup_method(self):
        if os.path.exists(config.Path_to_download_picture):
            os.remove(config.Path_to_download_picture)
        Waiter.implicit_wait(config.Timeout)
        Browser.maximize()

    def teardown_method(self):
        Browser.close_browser()

    def test_vk(self):
        Logger.info(f"Enter {config.Url}")
        Browser.enter_url(config.Url)
        unauthorized_page = UnauthorizedPage()
        Logger.info("Authorize")
        Steps.log_in(unauthorized_page, vk_config.Login, vk_config.Password)
        news_page = NewsPage()
        Logger.info("Go to the 'My Page'")
        news_page.side_bar.navigate_to(SideBarItems.MY_PAGE)
        my_page = MyPage()
        random_string = RandomUtils.get_random_string()
        owner_id = my_page.owner_id

        Logger.step("Creating post with random line and getting post's id", self.counter)
        self.counter += 1
        post_id = VkApiUtils.create_new_post(random_string)
        Logger.info("Checking that post was created")
        assert Steps.check_for_new_post_existing(my_page.post_form, owner_id, random_string), "Post wasn't published"

        Logger.step("Editing post and upload picture", self.counter)
        self.counter += 1
        edited_random_string = "edited_%s" % random_string
        uploaded_photo_id = VkApiUtils.edit_post_and_attach_file(edited_random_string, post_id, config.Path_to_picture)
        Logger.info("Checking that post was edited")
        assert Steps.check_for_post_editing(my_page.post_form, owner_id, edited_random_string,
                                            uploaded_photo_id), "Post wasn't edited"

        Logger.step("Adding random comment to the post", self.counter)
        self.counter += 1
        random_comment = RandomUtils.get_random_string()
        VkApiUtils.add_comment_to_post(random_comment, post_id)
        Logger.info("Checking that comment was added")
        assert Steps.check_for_comment_adding(my_page.post_form, owner_id, random_comment), "Comment wasn't added"

        Logger.step("Like edited post", self.counter)
        self.counter += 1
        my_page.post_form.like_post(owner_id, post_id)
        Logger.info("Checking that post was liked")
        assert VkApiUtils.is_item_liked_by_user(VkItems.POST, post_id, owner_id), "Post wasn't liked"

        Logger.step("Delete created post", self.counter)
        VkApiUtils.delete_post(post_id)
        assert Steps.check_for_post_deleted(owner_id, post_id), "Post wasn't deleted"
