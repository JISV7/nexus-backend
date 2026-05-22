from pydantic import BaseModel
from typing import List

class MicroserviceInput(BaseModel):
    name: str
    ram_requirement: int
    priority_value: int

class ServerLoadRequest(BaseModel):
    max_capacity: int = 16
    microservices: List[MicroserviceInput]

class SelectedItem(BaseModel):
    name: str
    weight: int
    value: int

class ServerLoadResponse(BaseModel):
    max_value: int
    total_weight: int
    selected_items: List[SelectedItem]
