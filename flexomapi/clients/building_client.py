from __future__ import annotations

from ..models import BuildingInfo, ZonesRes, IotsRes, ActuatorsRes
from ..requests.request_handler import RequestHandler
from ..requests.building import get_zones, get_iots, get_actuators, put_actuator_state
from .user_client import UserClient
from .building_authenticator import BuildingAuthenticator


class BuildingClient:

    authenticator: BuildingAuthenticator
    building_info: BuildingInfo
    building_token: str

    @staticmethod
    def build_client(user_client: UserClient, building_info: BuildingInfo) -> BuildingClient:
        authenticator = BuildingAuthenticator(user_client, building_info)
        building_token = authenticator.get_building_token()
        return BuildingClient(authenticator, building_info, building_token)

    def __init__(self, authenticator: BuildingAuthenticator, building_info: BuildingInfo,
                 building_token: str):
        self.authenticator = authenticator
        self.building_info = building_info
        self.building_token = building_token

    def re_authenticate(self) -> None:
        self.building_token = self.authenticator.get_building_token()

    def get_zones(self) -> ZonesRes:
        return RequestHandler(
            lambda: get_zones(self.building_info.hemis_base_url, self.building_token),
            lambda: self.re_authenticate(),
            ZonesRes
        ).handle_or_throw()

    def get_iots(self) -> IotsRes:
        return RequestHandler(
            lambda: get_iots(self.building_info.hemis_base_url, self.building_token),
            lambda: self.re_authenticate(),
            IotsRes
        ).handle_or_throw()

    def get_actuators(self, iot_id: str) -> ActuatorsRes:
        return RequestHandler(
            lambda: get_actuators(self.building_info.hemis_base_url, self.building_token, iot_id),
            lambda: self.re_authenticate(),
            ActuatorsRes
        ).handle_or_throw()

    def put_actuator_state(self, iot_id: str, actuator_id: str, value: float) -> None:
        return RequestHandler(
            lambda: put_actuator_state(self.building_info.hemis_base_url, self.building_token,
                                       iot_id, actuator_id, value),
            lambda: self.re_authenticate(),
            None
        ).handle_or_throw()
