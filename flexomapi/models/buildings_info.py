from typing import List
from pydantic import BaseModel, Extra


class BuildingInfo(BaseModel, extra=Extra.ignore):
    authorizationToken: str
    authorizationId: str
    buildingId: str
    hemis_base_url: str
    hemis_stomp_url: str
    kernel_slot: str


class BuildingsInfoRes(BaseModel):
    __root__: List[BuildingInfo]
