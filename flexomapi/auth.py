from pydantic import parse_obj_as
from .models.sign_in import SignInReq, SignInRes
from .models.buildings_info import BuildingsInfoRes
from .models.building_authorizations import BuildingAuthorizationsRes
from .models.building_auth import BuildingAuthReq, BuildingAuthRes
from .models.zones import ZonesRes
from .models.iot_list import IotsRes
import json
import requests
import urllib.parse


def send_auth(email: str, password: str) -> SignInRes:
    req = SignInReq(
        device=SignInReq.Device(
            uid="29c23c2aa953dc340f7525e57f0c8659",
            name="OnePlus 6",
            model="OnePlus ONEPLUS A6000",
            operating_system="Android",
            first_connection=0,
            last_connection=0
        ),
        email=email,
        password=password
    )

    res = requests.post(
        "https://hemisphere.ubiant.com/users/signin",
        data=req.json(),
        headers={'Content-type': 'application/json'}
    )
    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(SignInRes, json_data)


def send_buildings_info(bearer_tok: str) -> BuildingsInfoRes:
    res = requests.get(
        "https://hemisphere.ubiant.com/buildings/mine/infos",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingsInfoRes, json_data)


def send_building_auths(building_id: str, bearer_tok: str) -> BuildingAuthorizationsRes:
    res = requests.get(
        f"https://hemisphere.ubiant.com/buildings/{building_id}/authorizations",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingAuthorizationsRes, json_data)


def send_building_auth(base_url: str, hemis_kernel_id: str, email: str, building_tok: str)\
        -> BuildingAuthRes:
    req = BuildingAuthReq(email=email, password=building_tok, kernelId=hemis_kernel_id)
    res = requests.post(
        f"{base_url}/WS_UserManagement/login?includeFeatures=true",
        data=urllib.parse.urlencode(req.dict()),
        headers={'Content-type': 'application/x-www-form-urlencoded'}
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingAuthRes, json_data)


def send_zones(base_url: str, building_tok: str) -> ZonesRes:
    res = requests.get(
        f"{base_url}/zones",
        headers={'authorization': f"Bearer {building_tok}"}
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(ZonesRes, json_data)


def send_iot_list(base_url: str, building_tok: str) -> IotsRes:
    res = requests.get(
        f"{base_url}/intelligent-things/listV2",
        headers={'authorization': f"Bearer {building_tok}"}
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(IotsRes, json_data)
