class VkResponseParser:
    @staticmethod
    def is_item_liked(request_result):
        if request_result["response"]["liked"] == 1:
            return True
        else:
            return False

    @staticmethod
    def get_new_post_id(request_result):
        return int(request_result["response"]["post_id"])

    @staticmethod
    def get_upload_server_url(request_result):
        return request_result["response"]["upload_url"]

    @staticmethod
    def get_uploaded_photo_attributes(request_result):
        return request_result["server"], request_result["photo"], request_result["hash"]

    @staticmethod
    def get_uploaded_photo_id(request_result):
        return str(request_result["response"][0]["owner_id"]) + "_" + str(request_result["response"][0]["id"])
