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

def send_auth(email: str, password: str) -> SignInReq:
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
        headers={ 'Content-type': 'application/json' }
    )
    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(SignInRes, jsonData)

def send_buildings_info(bearer_tok: str):
    res = requests.get(
        "https://hemisphere.ubiant.com/buildings/mine/infos",
        headers={ 'authorization': f"Bearer {bearer_tok}" }
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingsInfoRes, jsonData)

def send_building_auths(building_id: str, bearer_tok: str):
    res = requests.get(
        f"https://hemisphere.ubiant.com/buildings/{building_id}/authorizations",
        headers={ 'authorization': f"Bearer {bearer_tok}" }
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingAuthorizationsRes, jsonData)


def send_building_auth(email: str, building_tok: str):
    req = BuildingAuthReq(email=email, password=building_tok)
    res = requests.post(
        "https://tender-yonath-pu46isv5.eu-west.hemis.io/hemis/rest/WS_UserManagement/login?includeFeatures=true",
        data=urllib.parse.urlencode(req.dict()),
        headers={ 'Content-type': 'application/x-www-form-urlencoded' }
    )


    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(BuildingAuthRes, jsonData)


def send_zones(building_tok: str):
    res = requests.get(
        "https://tender-yonath-pu46isv5.eu-west.hemis.io/hemis/rest/zones",
        headers={ 'authorization': f"Bearer {building_tok}" }
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(ZonesRes, jsonData)

def send_iot_list(building_tok: str):
    res = requests.get(
        "https://tender-yonath-pu46isv5.eu-west.hemis.io/hemis/rest/intelligent-things/listV2",
        headers={ 'authorization': f"Bearer {building_tok}" }
    )

    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    jsonData = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(IotsRes, jsonData)
