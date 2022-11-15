from __future__ import annotations
from typing import Optional

from .user_authenticator import UserAuthenticator


class UserClient:
    authenticator: UserAuthenticator
    user_token: str

    def __init__(self, authenticator: UserAuthenticator, user_token: str):
        self.authenticator = authenticator
        self.user_token = user_token

    @staticmethod
    def build_user_client(email: str, password: str) -> Optional[UserClient]:
        authenticator = UserAuthenticator(email, password)
        user_token = authenticator.get_user_token()
        if not user_token:
            return None
        return UserClient(authenticator, user_token)

    def re_authenticate(self) -> None:
        self.user_token = self.authenticator.get_user_token()

    def get_building(self):
        # TODO: make requests, if failure due to 401, re-authenticate and retry
        pass

    def get_building_authorizations(self, building_id: str):
        # TODO: make requests, if failure due to 401, re-authenticate and retry
        pass
