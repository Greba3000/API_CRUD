import requests

info_json_1 = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 17.5}
info_json_2 = {"bear_type": "red", "bear_name": "mikhail", "bear_age": 17.5}
info_json_3 = {"bear_type": "GUMMY", "bear_name": "fedya", "bear_age": 1}
available_types = ['POLAR', "BROWN", "BLACK", "GUMMY", ]


class BearService:

    def create_bear(self, info_json: dict):
        if info_json['bear_type'] in available_types:
            r = requests.post('http://127.0.0.1:8000/bear', json=info_json)

    def get_all_bears(self) -> dict:
        r = requests.get('http://127.0.0.1:8000/bear')
        return r.json()

    def get_bear(self, bear_id: int) -> dict:
        r = requests.get(f'http://127.0.0.1:8000//bear/{bear_id}')
        return r.json()

    def update_bear(self, info_json: dict, bear_id: int):
        if info_json['bear_type'] in available_types:
            r = requests.put(f'http://127.0.0.1:8000//bear/{bear_id}', json=info_json)

    def del_all_bears(self):
        r = requests.delete('http://127.0.0.1:8000/bear')

    def del_bear(self, bear_id: int):
        r = requests.delete(f'http://127.0.0.1:8000/bear/{bear_id}')


if __name__ == '__main__':
    bs = BearService()
    # bs.create_bear(info_json_1)
    # bs.update_bear(info_json_3, 5)
    # bs.del_all_bears()
