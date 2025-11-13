from sqlalchemy import Column,Integer, String, DateTime
from datetime import datetime
from app.database import Base

class FileLog(Base):
    __tablename__="file_logs"

    id=Column(Integer, primary_key=True, index=True)
    filename=Column(String(255), nullable=False)
    filetype=Column(String(100))
    uploader=Column(String(100))
    pii_detected=Column(String(500))  #yes/no
    action_taken=Column(String(500))  # Blocked/allowed
    timestamp=Column(DateTime, default=datetime.utcnow)