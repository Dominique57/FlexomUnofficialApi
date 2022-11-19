from ..models import SignInRes
from ..requests.auth import post_auth
from ..requests.request_handler import RequestHandler


class UserAuthenticator:
    """
    Class that centralizes credentials for user authentication
    """

    email: str
    password: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def get_user_token(self) -> str:
        sign_in_res: SignInRes = RequestHandler(
            lambda: post_auth(self.email, self.password),
            lambda: None,
            SignInRes
        ).handle_or_throw()
        return sign_in_res.token
