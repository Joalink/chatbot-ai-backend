from pydatic import BaseModel, Field
from enum import  Enum
from datetime import datetime

class ModelName(str, Enum):
    GPT4_o = "gpt-4o"
    GPTA_O_MINI = "gpt-4o-mini"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GPTA_O_MINI)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_time: datetime

class DeleteFileRequest(BaseModel):
    file_id: int