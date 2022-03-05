from pydantic import BaseModel, Extra
from typing import List, Optional
from .zones import Zone


class Iot(BaseModel, extra=Extra.ignore):
    id: str
    comID: str
    firmwareVersion: Optional[str]
    version: Optional[str]
    creationTimeStamp: int
    embodiment: str
    name: str
    zoneInformation: Zone
    gateways: List[str]
    specifiedGateway: str
    specifiedGatewayEnable: bool
    state: str
    rssi: Optional[int]
    hasImage: bool
    locked: bool


class IotsRes(BaseModel):
    __root__: List[Iot]
