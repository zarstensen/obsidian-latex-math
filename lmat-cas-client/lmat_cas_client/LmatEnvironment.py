from typing import Optional

from pydantic import BaseModel, Field


class EnvDefinition(BaseModel):
    name_expr: str
    value_expr: str


## The LmatEnvironment type represents a dictionary
## parsed from a json encoded LmatEnvironment typescript class.
class LmatEnvironment(BaseModel):
    symbols: dict[str, list[str]] = Field(default_factory=dict)

    definitionsv2: list[str] = Field(default_factory=list)
    definitions: list[EnvDefinition] = Field(default_factory=list)

    unit_system: Optional[str] = None

    solve_domain: Optional[str] = None
