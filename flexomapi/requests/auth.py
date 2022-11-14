from urllib.parse import urlencode
import requests

from . import SignInReq, BuildingAuthReq


def post_auth(email: str, password: str) -> requests.Response:
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
    return res


def get_building_auths(building_id: str, bearer_tok: str) -> requests.Response:
    res = requests.get(
        f"https://hemisphere.ubiant.com/buildings/{building_id}/authorizations",
        headers={'authorization': f"Bearer {bearer_tok}"}
    )
    return res


def post_building_auth(base_url: str, hemis_kernel_id: str, email: str,
                       building_auth_token: str) -> requests.Response:
    req = BuildingAuthReq(email=email, password=building_auth_token, kernelId=hemis_kernel_id)
    res = requests.post(
        f"{base_url}/WS_UserManagement/login?includeFeatures=true",
        data=urlencode(req.dict()),
        headers={'Content-type': 'application/x-www-form-urlencoded'}
    )
    return res
