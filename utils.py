from config import available_types


def is_available_type(info_json: dict) -> bool:
    if info_json['bear_type'] in available_types:
        return True


def is_response_status_good(resp):
    if resp.ok:
        print('Request completed successfully.')
