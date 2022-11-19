from ..models import BuildingAuthRes, BuildingInfo, BuildingAuthorizationsRes, BuildingAuthorization
from ..requests.request_handler import RequestHandler
from ..requests.auth import post_building_auth
from .user_client import UserClient
from typing import Optional, Union


class BuildingAuthenticator:
    """
    Class that requests new building token from the user client
    """

    user_client: UserClient
    building_info: BuildingInfo
    building_auth_token: str

    def __init__(self, user_client: UserClient, building_info: BuildingInfo, /,
                 bauth_token: Union[list, str, None] = None):
        self.user_client = user_client
        self.building_info = building_info

        if bauth_token is None:
            self.building_auth_token = self._get_building_auth_token().token
        elif type(bauth_token) == str:
            self.building_auth_token = bauth_token
        elif type(bauth_token) == list:
            self.building_auth_token = self._get_building_auth_token(bauth_token).token
        else:
            raise Exception(f"bauth_token is not of valid type: {type(bauth_token)}")

    def _get_building_auth_token(
            self, /, bauths: Optional[BuildingAuthorizationsRes] = None
    ) -> BuildingAuthorization:
        # Fetch auths if not provided
        if bauths is None:
            bauths = self.user_client.get_building_authorizations(self.building_info.buildingId)
        # Filter for user-client specific auth
        user_email = self.user_client.authenticator.email
        for auth in bauths.__root__:
            if auth.user.email == user_email:
                return auth
        raise Exception(f"User ({user_email}) was not found in building "
                        f"({self.building_info.buildingId}) auth list !")

    def _re_authenticate_auth_token(self):
        self.building_auth_token = self._get_building_auth_token().token

    def get_building_token(self) -> str:
        res_bauth: BuildingAuthRes = RequestHandler(
            lambda: post_building_auth(
                self.building_info.hemis_base_url, self.building_info.kernel_slot,
                self.user_client.authenticator.email, self.building_auth_token),
            lambda: self._re_authenticate_auth_token(),
            BuildingAuthRes
        ).handle_or_throw()
        return res_bauth.token
