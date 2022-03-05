from typing import List
from pydantic import BaseModel


class SignInReq(BaseModel):
    class Device(BaseModel):
        uid: str
        name: str
        model: str
        operating_system: str
        first_connection: int
        last_connection: int

    device: Device
    email: str
    password: str


class SignInRes(BaseModel):
    class Device(BaseModel):
        uid: str
        name: str
        model: str
        validated: bool
        first_connection: int
        last_connection: int
        operating_system: str

    id: str
    first_name: str
    last_name: str
    username: str
    user_brand: str
    email: str
    locale: str
    token: str
    creation_date: int
    activated: bool
    pass_reset: bool
    last_login: int
    birth_date: str
    newsletter: bool
    grantedRoles: List[str]
    roles: List[str]
    nb_connexion: int
    tags: List[str]
    current_device: Device
