from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    class Company(BaseModel):
        id: str
        name: str
        validated: bool

    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    user_brand: str
    email: str
    locale: Optional[str] = None
    creation_date: int
    activated: bool
    pass_reset: Optional[bool] = None
    last_login: Optional[int] = None
    birth_date: Optional[str] = None
    newsletter: Optional[bool] = None
    grantedRoles: List[str]
    roles: List[str]
    nb_connexion: int
    tags: List[str]
    company: Optional[Company] = None
    user_json: Optional[str] = None


class BuildingAuthorization(BaseModel):
    id: str
    name: str
    level: str
    token: str
    activated: bool
    transfer: bool
    user: User
    type: str
    active: bool
    expired: bool
    permanent: bool
    hemis_level: str
    creation_date: int
    last_update: int
    entity_id: str


class BuildingAuthorizationsRes(BaseModel):
    __root__: List[BuildingAuthorization]
