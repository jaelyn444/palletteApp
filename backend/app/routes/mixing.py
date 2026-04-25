from fastapi import APIRouter
from app.models.schemas import MixRequest, MixResponse
from app.services.color_service import get_paint_mix

router = APIRouter()

@router.post("/mix", response_model=MixResponse)
async def mix_color(request: MixRequest):
    result = get_paint_mix(request.rgb)
    return result