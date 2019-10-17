from framework.models.vk_api_request import VkApiRequest
from framework.vk_api.enums.vk_like_methods import VkLikeMethods
from framework.vk_api.enums.vk_wall_methods import VkWallMethods
from framework.vk_api.vk_upload_photo_utils import VkUploadPhotoUtils
from framework.vk_api.vk_utils.vk_response_parser import VkResponseParser
from resources import vk_config


class VkApiUtils:

    @staticmethod
    def create_new_post(message):
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("message", message))
        parameters.append(("v", vk_config.Api_version))
        return VkResponseParser.get_new_post_id(VkApiRequest(VkWallMethods.POST, dict(parameters)).request_result)

    @staticmethod
    def edit_post_and_attach_file(message, post_id, photo):
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("post_id", post_id))
        parameters.append(("message", message))
        parameters.append(("v", vk_config.Api_version))
        photo_id = VkUploadPhotoUtils.upload_wall_photo(photo)
        parameters.append(("attachments", "photo" + photo_id))
        VkApiRequest(VkWallMethods.EDIT, dict(parameters))
        return photo_id

    @staticmethod
    def add_comment_to_post(message, post_id):
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("post_id", post_id))
        parameters.append(("message", message))
        parameters.append(("v", vk_config.Api_version))
        VkApiRequest(VkWallMethods.CREATE_COMMENT, dict(parameters))

    @staticmethod
    def is_item_liked_by_user(item_type, post_id, user_id):
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("type", item_type.value))
        parameters.append(("item_id", post_id))
        parameters.append(("user_id", user_id))
        parameters.append(("v", vk_config.Api_version))
        return VkResponseParser.is_item_liked(VkApiRequest(VkLikeMethods.IS_LIKED, dict(parameters)).request_result)

    @staticmethod
    def delete_post(post_id):
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("post_id", post_id))
        parameters.append(("v", vk_config.Api_version))
        VkApiRequest(VkWallMethods.DELETE, dict(parameters))
