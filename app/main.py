from fastapi import FastAPI
from app import database
from app.routers import file_routes


app=FastAPI(title="AI-Powered File Metadata & PII Detection System")

app.include_router(file_routes.router)

database.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "Welcome to the AI-Powered File Metadata & PII Detection System API"}