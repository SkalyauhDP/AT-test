import requests

RESPONSE_CONTENT_TYPE = "application/json"


class ApiClient:
    def __init__(self, api_server):
        self.api_server = api_server

    def call_api_post(self, api_url=None, request_body=None):
        if not api_url:
            headers = {
                "accept": RESPONSE_CONTENT_TYPE,
                "Content-Type": RESPONSE_CONTENT_TYPE
            }
        else:
            headers = {
                "accept": RESPONSE_CONTENT_TYPE,
                "Content-Type": "application/x-www-form-urlencoded"
            }
            self.api_server += f'/{api_url}'
        response = requests.post(self.api_server, headers=headers, data=request_body)
        return response

    def call_api_put(self, request_body):
        headers = {
            "accept": RESPONSE_CONTENT_TYPE,
            "Content-Type": RESPONSE_CONTENT_TYPE
        }
        response = requests.put(self.api_server, data=request_body, headers=headers)
        return response

    def call_api_get(self, api_data, status=None):
        headers = {
            "accept": RESPONSE_CONTENT_TYPE
        }
        response = requests.get(self.api_server + '/' + api_data, headers=headers, params={'status': status})
        return response

    def call_api_delete(self, api_data):
        headers = {
            "accept": RESPONSE_CONTENT_TYPE
        }
        response = requests.delete(self.api_server + '/' + api_data, headers=headers)
        return response
