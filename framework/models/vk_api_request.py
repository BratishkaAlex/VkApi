from framework.models.post_request import PostRequest


class VkApiRequest(PostRequest):
    Request_url_pattern = "https://api.vk.com/method/%s"

    def __init__(self, method, parameters):
        super().__init__(self.Request_url_pattern % method.value, parameters)
