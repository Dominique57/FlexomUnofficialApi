from pydantic import BaseModel
from typing import Any, List, Optional


class Zone(BaseModel):
    id: str
    name: str
    type: Optional[str]
    parentId: Optional[str]
    metazone: bool
    hasImage: bool
    floor: Any
    external: bool
    surface: str


class ZonesRes(BaseModel):
    __root__: List[Zone]
