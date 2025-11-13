from pydantic import BaseModel
from datetime import datetime

class FileLogBase(BaseModel):
    filename: str
    filetype: str | None = None
    uploader: str | None = None
    pii_detected: str | None = None  # yes/no
    action_taken: str | None = None  # Blocked/allowed
    
class FileLogCreate(FileLogBase):
    pass   # used when inserting a new record

class FileLogResponse(FileLogBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True  #allows ORM objects to return as dict/json

        