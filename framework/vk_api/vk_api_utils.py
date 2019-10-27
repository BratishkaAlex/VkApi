from framework.utils.logger import info
from framework.vk_api.enums.vk_like_methods import VkLikeMethods
from framework.vk_api.enums.vk_wall_methods import VkWallMethods
from framework.vk_api.vk_upload_photo_utils import *
from resources import vk_config


def create_new_post(message):
    parameters = {
        "access_token": vk_config.ACCESS_TOKEN,
        "message": message,
        "v": vk_config.API_VERSION
    }
    return int(VkApiRequest(VkWallMethods.POST, parameters).request_result["response"]["post_id"])


def edit_post_and_attach_file(message, post_id, photo):
    photo_id = upload_wall_photo(photo)
    parameters = {
        "access_token": vk_config.ACCESS_TOKEN,
        "post_id": post_id,
        "message": message,
        "v": vk_config.API_VERSION,
        "attachments": "photo" + photo_id
    }
    VkApiRequest(VkWallMethods.EDIT, parameters)
    return photo_id


def add_comment_to_post(message, post_id):
    parameters = {
        "access_token": vk_config.ACCESS_TOKEN,
        "post_id": post_id,
        "message": message,
        "v": vk_config.API_VERSION
    }
    VkApiRequest(VkWallMethods.CREATE_COMMENT, parameters)


def is_item_liked_by_user(item_type, post_id, user_id):
    info("Checking that post was liked")
    parameters = {
        "access_token": vk_config.ACCESS_TOKEN,
        "type": item_type.value,
        "item_id": post_id,
        "user_id": user_id,
        "v": vk_config.API_VERSION
    }
    return VkApiRequest(VkLikeMethods.IS_LIKED, parameters).request_result["response"]["liked"] == 1


def delete_post(post_id):
    parameters = {
        "access_token": vk_config.ACCESS_TOKEN,
        "post_id": post_id,
        "v": vk_config.API_VERSION
    }
    VkApiRequest(VkWallMethods.DELETE, parameters)
