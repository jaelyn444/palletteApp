from pydantic import BaseModel 

class ColorResult(BaseModel):
    hex: str
    rgb: list[int]

class PalletteResponse(BaseModel):
    colors: list[ColorResult]

class MixRequest(BaseModel):
    rgb: list[int]

class MixResponse(BaseModel):
    mix: dict[str, float]