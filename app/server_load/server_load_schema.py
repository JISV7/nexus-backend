from typing import List

from pydantic import BaseModel, Field


class MicroserviceInput(BaseModel):
    name: str
    ram_requirement: int = Field(ge=0)
    priority_value: int = Field(ge=0)


class ServerLoadRequest(BaseModel):
    max_capacity: int = Field(default=16, ge=0)
    microservices: List[MicroserviceInput]


class SelectedItem(BaseModel):
    name: str
    weight: int
    value: int


class ServerLoadResponse(BaseModel):
    max_value: int
    total_weight: int
    selected_items: List[SelectedItem]
