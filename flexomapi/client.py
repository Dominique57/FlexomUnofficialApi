from pydantic import parse_obj_as
import json
import requests
from urllib.parse import urlencode
from .models import *


# TODO: move this elsewhere
def handle_res(res: requests.Response, result_class):
    if not 200 <= res.status_code < 300:
        raise Exception('Login token request error', res, res.content)

    json_data = json.JSONDecoder().decode(res.content.decode('utf-8'))
    return parse_obj_as(result_class, json_data)


class BuildingClient:
    @staticmethod
    def send_building_auth(base_url: str, hemis_kernel_id: str, email: str,
                           building_auth_token: str) -> BuildingAuthRes:
        req = BuildingAuthReq(email=email, password=building_auth_token, kernelId=hemis_kernel_id)
        res = requests.post(
            f"{base_url}/WS_UserManagement/login?includeFeatures=true",
            data=urlencode(req.dict()),
            headers={'Content-type': 'application/x-www-form-urlencoded'}
        )
        return handle_res(res, BuildingAuthRes)

    base_url: str
    building_tok: str

    def __init__(self, base_url: str, building_tok: str):
        self.base_url = base_url
        self.building_tok = building_tok

    def send_zones(self) -> ZonesRes:
        res = requests.get(
            f"{self.base_url}/zones",
            headers={'authorization': f"Bearer {self.building_tok}"}
        )
        return handle_res(res, ZonesRes)

    def send_iot_list(self) -> IotsRes:
        res = requests.get(
            f"{self.base_url}/intelligent-things/listV2",
            headers={'authorization': f"Bearer {self.building_tok}"}
        )
        return handle_res(res, IotsRes)
