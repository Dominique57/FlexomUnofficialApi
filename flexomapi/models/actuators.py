from __future__ import annotations
from typing import Any, List
from pydantic import BaseModel


class ActuatorStateReq(BaseModel):
    duration: int
    value: float


class ActuatorState(BaseModel):
    type: str
    itId: str
    actuatorId: str
    value: int
    timeStamp: int
    progressive: bool
    colorEnable: bool
    color: Any
    hsvColor: Any
    hue: Any
    saturation: Any
    ctEnable: bool
    ct: Any
    minActionValue: int
    maxActionValue: int
    remote: Any
    direct: bool
    transitionDuration: Any


class Actuator(BaseModel):
    actuatorId: str
    state: ActuatorState
    hardwareState: ActuatorState
    targetState: ActuatorState
    actionningRepresentation: Any
    itId: str
    factors: List[str]
    activated: bool
    external_modification_forbidden: Any
    com_type: str
    usableByUser: bool
    sourceId: Any
    connectors: List


class ActuatorsRes(BaseModel):
    __root__: List[Actuator]
