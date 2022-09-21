from utils import is_available_type
from requester import Requester
from utils import is_response_status_good

info_json_1 = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 17.5}
info_json_2 = {"bear_type": "red", "bear_name": "mikhail", "bear_age": 17.5}
info_json_3 = {"bear_type": "GUMMY", "bear_name": "fedya", "bear_age": 1}


class BearService(Requester):

    def create_bear(self, info_json: dict):
        if is_available_type(info_json):
            self.post(info_json)

    def get_all_bears(self):
        return self.get()

    def get_bear(self, bear_id: int):
        return self.get(item_id=bear_id)

    def update_bear(self, info_json: dict, bear_id: int):
        self.put(info_json, item_id=bear_id)

    def del_all_bears(self):
        self.delete()

    def del_bear(self, bear_id: int):
        self.delete(item_id=bear_id)


if __name__ == '__main__':
    bs = BearService()
    # bs.create_bear(info_json_1)
    # bs.update_bear(info_json_3, 5)
    # bs.del_all_bears()
    # print(bs.get_all_bears().json())
