from algorithms.paint_mixing import find_paint_mix
from app.models.schemas import MixResponse

def get_paint_mix(rgb: list[int]) -> MixResponse:
    mix = find_paint_mix(rgb)
    return MixResponse(mix=mix)