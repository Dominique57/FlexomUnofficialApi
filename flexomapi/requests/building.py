import requests


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
