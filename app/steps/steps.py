from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from app.page_object.forms.post_form import PostForm
from app.page_object.pages.unauthorized_page import UnauthorizedPage
from framework.utils.comparison_utils import compare_two_images
from framework.utils.download_utils import download_file
from framework.utils.logger import info
from framework.utils.waiter import wait_for_element_disappearing
from resources import config

unauthorized_page = UnauthorizedPage()
post_form = PostForm()


def log_in(login, password):
    info("Authorize")
    unauthorized_page.type_login(login)
    unauthorized_page.type_password(password)
    unauthorized_page.click_submit()


def is_post_deleted(owner_id, post_id):
    info("Checking that post was deleted")
    try:
        wait_for_element_disappearing(By.ID, f"post{owner_id}_{post_id}")
        return True
    except TimeoutException:
        return False


def is_new_post_existing(owner_id, message):
    info("Checking that post was created")
    if owner_id in post_form.author_of_latest_post_href:
        return True and post_form.is_post_with_message_displayed(message)
    else:
        return False


def is_post_edited(owner_id, message, uploaded_photo_id):
    info("Checking that post was edited")
    download_picture(uploaded_photo_id)
    return compare_two_images(config.PATH_TO_PICTURE,
                              config.PATH_TO_DOWNLOAD_PICTURE) and is_new_post_existing(owner_id,
                                                                                        message)


def download_picture(uploaded_photo_id):
    photo = post_form.get_uploaded_photo(uploaded_photo_id)
    download_file(photo.link_to_download, config.PATH_TO_DOWNLOAD_PICTURE)
