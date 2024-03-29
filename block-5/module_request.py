class ApiRequest:
    def __init__(self, req_type: str, payload: str):
        self.req_type = req_type
        self.payload = payload

    def change_payload(self, new_payload):
        self.payload = new_payload
        return self.payload
