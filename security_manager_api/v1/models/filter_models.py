from typing import Any
from pydantic.fields import Field
from pydantic.main import BaseModel as PydanticBaseModel
from pydantic.types import StrictStr


class FilterItem(PydanticBaseModel):
    key: StrictStr = Field(..., example="field", description="field to use to filter")
    operator: StrictStr = Field(
        "=", example="=", description="operator type fo filter (e.g `=`,`!=`)"
    )
    value: Any = Field(
        ...,
        example="foo",
        description="value of the filter (Not allowed SQL statement)",
    )
    data_type: str
