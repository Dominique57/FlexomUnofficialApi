from typing import List
from pydantic import BaseModel, Extra


class BuildingsInfoRes(BaseModel):
    class BuildingsInfo(BaseModel, extra=Extra.ignore):
        authorizationToken: str
        authorizationId: str
        buildingId: str

    __root__: List[BuildingsInfo]
