from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.models.schemas import PaletteResponse
from app.services.image_service import process_uploaded_image

router = APIRouter()

@router.post("/upload", response_model=PaletteResponse)
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(status_code=400, detail="File must be an image")
    
    temp_path = f"/tmp/{file.filename}"
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        result = process_uploaded_image(temp_path)
        return result
    finally:
        os.remove(temp_path)