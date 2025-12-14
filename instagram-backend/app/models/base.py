from typing import Annotated, Any, Callable
from pydantic import BaseModel, BeforeValidator, Field

# Helper to map MongoDB _id to string
PyObjectId = Annotated[str, BeforeValidator(str)]

class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default=None, alias="_id")