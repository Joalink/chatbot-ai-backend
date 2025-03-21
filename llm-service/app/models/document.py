from pydatic import BaseModel, Field
from datetime import datetime

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_time: datetime

class DeleteFileRequest(BaseModel):
    file_id: int