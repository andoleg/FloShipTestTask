import requests


class CommunicationException(BaseException):
    ...


class CommunicationService:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, data, order_id, request_method="POST"):
        if request_method == "POST":
            response = requests.post(f"{self.base_url}/orders/", json=data)
        elif request_method == "PUT":
            response = requests.put(f"{self.base_url}/orders/{order_id}/", json=data)
        else:
            return
        if response.status_code == 400:
            return
        elif response.status_code not in (200, 201):
            raise CommunicationException
