import requests
from .urllib_hashtag_extension import ensure_extension_enabled

from . import ActuatorStateReq


def get_buildings_info(bearer_tok: str) -> requests.Response:
    res = requests.get(
        "https://hemisphere.ubiant.com/buildings/mine/infos",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )
    return res


def get_zones(base_url: str, building_tok: str) -> requests.Response:
    res = requests.get(
        f"{base_url}/zones",
        headers={'authorization': f"Bearer {building_tok}"}
    )
    return res


def get_iots(base_url: str, building_tok: str) -> requests.Response:
    res = requests.get(
        f"{base_url}/intelligent-things/listV2",
        headers={'authorization': f"Bearer {building_tok}"}
    )
    return res


def get_actuators(base_url: str, building_tok: str, iot_id: str) -> requests.Response:
    res = requests.get(
        f"{base_url}/intelligent-things/{iot_id}/actuators",
        headers={'authorization': f"Bearer {building_tok}"}
    )
    return res


def put_actuator_state(base_url: str, building_tok: str, iot_id: str, actuator_id: str,
                       value: float) -> requests.Response:
    ensure_extension_enabled()
    req = ActuatorStateReq(duration=4000000000000, value=value)
    res = requests.put(
        f"{base_url}/intelligent-things/{iot_id}/actuator/{actuator_id}/state",
        data=req.json(),
        headers={
            'authorization': f"Bearer {building_tok}",
            'Content-type': 'application/json; charset=utf8',
        }
    )
    return res
