import requests

from config import host, endpoint1
from utils import is_available_type, is_response_status_good

info_json_1 = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 17.5}
info_json_2 = {"bear_type": "red", "bear_name": "mikhail", "bear_age": 17.5}
info_json_3 = {"bear_type": "GUMMY", "bear_name": "fedya", "bear_age": 1}


class BearService:

    def create_bear(self, info_json: dict):
        if is_available_type(info_json):
            resp = requests.post(host, json=info_json)
            is_response_status_good(resp)

    def get_all_bears(self):
        resp = requests.get(host)
        is_response_status_good(resp)

    def get_bear(self, bear_id: int):
        resp = requests.get(f'{host}{endpoint1}{bear_id}')
        is_response_status_good(resp)

    def update_bear(self, info_json: dict, bear_id: int):
        if is_available_type(info_json):
            resp = requests.put(f'{host}{endpoint1}{bear_id}', json=info_json)
            is_response_status_good(resp)

    def del_all_bears(self):
        resp = requests.delete(host)
        is_response_status_good(resp)

    def del_bear(self, bear_id: int):
        resp = requests.delete(f'{host}{endpoint1}{bear_id}')
        is_response_status_good(resp)

    # def new_method(self):
    #     resp = requests.type_request(f'{host}{endpoint1}')
    #     is_response_status_good(resp)

if __name__ == '__main__':
    bs = BearService()
    # bs.create_bear(info_json_1)
    # bs.update_bear(info_json_3, 5)
    # bs.del_all_bears()
