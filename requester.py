import requests
from config import host, endpoint1


class Requester:

    def send_request(self, method, url=host, endpoint=endpoint1, data=None, json=None):
        return method(f'{url}{endpoint}', data=data, json=json)

    def get(self, item_id=0):
        if item_id == 0:
            return self.send_request(requests.get)
        else:
            return self.send_request(requests.get, url=f'{host}{endpoint1}/{item_id}')

    def post(self, info_json: dict):
        return self.send_request(requests.post, json=info_json)

    def delete(self, item_id=0):
        if item_id == 0:
            return self.send_request(requests.delete)
        else:
            return self.send_request(requests.delete, url=f'{host}{endpoint1}/{item_id}')

    def put(self, info_json: dict, item_id: int):
        return self.send_request(requests.put, url=f'{host}{endpoint1}/{item_id}', json=info_json)

    def head(self):
        pass

    def options(self):
        pass

    def patch(self):
        pass

