from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models,schemas
import shutil
from app.schemas.file_schema import FileLogResponse


router = APIRouter(
    prefix="/files",
    tags=["File Upload & Logs"]
)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload", response_model=schemas.file_schema.FileLogResponse)
async def upload_file(
    file: UploadFile = File(...),
    uploader: str = Form(None),
    db: Session = Depends(get_db)
):
    # save uploaded file to local folder
    with open(f"uploads/{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # get file extension/type
    filetype = file.filename.split(".")[-1]

    # temporary dummy PII detection
    pii_detected = "no"
    action_taken = "allowed"

    #  create db record
    new_file=models.FileLog(
        filename=file.filename,
        filetype=filetype,
        uploader=uploader,
        pii_detected=pii_detected,
        action_taken=action_taken
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file
