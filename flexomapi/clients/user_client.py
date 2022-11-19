from __future__ import annotations
from typing import Optional

from ..models import BuildingsInfoRes, BuildingAuthorizationsRes
from ..requests.request_handler import RequestHandler
from ..requests.building import get_buildings_info
from ..requests.auth import get_building_auths
from .user_authenticator import UserAuthenticator


class UserClient:

    authenticator: UserAuthenticator
    user_token: str

    @staticmethod
    def build_client(email: str, password: str) -> Optional[UserClient]:
        authenticator = UserAuthenticator(email, password)
        user_token = authenticator.get_user_token()
        if not user_token:
            return None
        return UserClient(authenticator, user_token)

    def __init__(self, authenticator: UserAuthenticator, user_token: str):
        self.authenticator = authenticator
        self.user_token = user_token

    def re_authenticate(self) -> None:
        self.user_token = self.authenticator.get_user_token()

    def get_buildings_info(self) -> BuildingsInfoRes:
        return RequestHandler(
            lambda: get_buildings_info(self.user_token),
            lambda: self.re_authenticate(),
            BuildingsInfoRes
        ).handle_or_throw()

    def get_building_authorizations(self, building_id: str) -> BuildingAuthorizationsRes:
        return RequestHandler(
            lambda: get_building_auths(building_id, self.user_token),
            lambda: self.re_authenticate(),
            BuildingAuthorizationsRes
        ).handle_or_throw()
