from pydantic import parse_obj_as
from .models.sign_in import SignInReq, SignInRes
from .models.buildings_info import BuildingsInfoRes
from .models.building_authorizations import BuildingAuthorizationsRes
import json
import requests


# TODO: move this elsewhere
def handle_res(res: requests.Response, result_class):
    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(result_class, json_data)


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

    return handle_res(res, SignInRes)


def send_buildings_info(bearer_tok: str) -> BuildingsInfoRes:
    res = requests.get(
        "https://hemisphere.ubiant.com/buildings/mine/infos",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )

    return handle_res(res, BuildingsInfoRes)


def send_building_auths(building_id: str, bearer_tok: str) -> BuildingAuthorizationsRes:
    res = requests.get(
        f"https://hemisphere.ubiant.com/buildings/{building_id}/authorizations",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )
    return handle_res(res, BuildingAuthorizationsRes)
