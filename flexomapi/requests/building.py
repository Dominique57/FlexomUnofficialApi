import requests

from . import IotsRes, ZonesRes, BuildingsInfoRes
from .utils import handle_res_throw


def get_buildings_info(bearer_tok: str) -> BuildingsInfoRes:
    res = requests.get(
        "https://hemisphere.ubiant.com/buildings/mine/infos",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )
    return handle_res_throw(res, BuildingsInfoRes)


def get_zones(base_url: str, building_tok: str) -> ZonesRes:
    res = requests.get(
        f"{base_url}/zones",
        headers={'authorization': f"Bearer {building_tok}"}
    )
    return handle_res_throw(res, ZonesRes)


def get_iots(base_url: str, building_tok: str) -> IotsRes:
    res = requests.get(
        f"{base_url}/intelligent-things/listV2",
        headers={'authorization': f"Bearer {building_tok}"}
    )
    return handle_res_throw(res, IotsRes)
