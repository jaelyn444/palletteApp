# Defines the shape of data going in and out of the API

from pydantic import BaseModel 

class ColorResult(BaseModel):
    hex: str
    rgb: list[int]

class PaletteResponse(BaseModel):
    colors: list[ColorResult]

class MixRequest(BaseModel):
    rgb: list[int]

class MixResponse(BaseModel):
    mix: dict[str, float]