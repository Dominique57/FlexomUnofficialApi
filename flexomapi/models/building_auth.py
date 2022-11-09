from pydantic import BaseModel, Extra
from typing import Dict, List


class BuildingAuthReq(BaseModel):
    email: str
    password: str
    kernelId: str


class BuildingAuthRes(BaseModel, extra=Extra.ignore):
    token: str
    role: str
    hemisVersion: str
    timeZone: str
    offset: int
    permissions: List[str]
    features: List[str]
    zoneRoles: Dict
    stompEnabled: bool
