from os.path import abspath

from framework.models.post_request import PostRequest
from framework.models.vk_api_request import VkApiRequest
from framework.vk_api.enums.vk_upload_photos_methods import VkUploadPhotosMethod
from framework.vk_api.vk_utils.vk_response_parser import VkResponseParser
from resources import vk_config


class VkUploadPhotoUtils:
    @staticmethod
    def get_wall_upload_server():
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("v", vk_config.Api_version))
        return VkResponseParser.get_upload_server_url(
            VkApiRequest(VkUploadPhotosMethod.GET_WALL_UPLOAD_SERVER, dict(parameters)).request_result)

    @staticmethod
    def get_uploaded_photo_attributes(photo_name):
        files = list()
        files.append(("photo", open(abspath(photo_name), "rb")))
        parameters = dict()
        return VkResponseParser.get_uploaded_photo_attributes(
            PostRequest(VkUploadPhotoUtils.get_wall_upload_server(), parameters, dict(files)).request_result)

    @staticmethod
    def upload_wall_photo(photo_name):
        server, photo, photo_hash = VkUploadPhotoUtils.get_uploaded_photo_attributes(photo_name)
        parameters = list()
        parameters.append(("access_token", vk_config.Access_token))
        parameters.append(("v", vk_config.Api_version))
        parameters.append(("server", server))
        parameters.append(("photo", photo))
        parameters.append(("hash", photo_hash))
        return VkResponseParser.get_uploaded_photo_id(
            VkApiRequest(VkUploadPhotosMethod.SAVE_WALL_PHOTO, parameters).request_result)
