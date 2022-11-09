from typing import List
from pydantic import BaseModel, Extra


class BuildingsInfoRes(BaseModel):
    class BuildingsInfo(BaseModel, extra=Extra.ignore):
        authorizationToken: str
        authorizationId: str
        buildingId: str
        hemis_base_url: str
        hemis_stomp_url: str
        kernel_slot: str

    __root__: List[BuildingsInfo]
