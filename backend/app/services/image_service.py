from algorithms.kmeans import extract_colors
from algorithms.paint_mixing import find_paint_mix
from app.models.schemas import PaletteResponse, ColorResult

def process_uploaded_image(image_path: str) -> PaletteResponse:
    colors = extract_colors(image_path, k=6)
    
    color_results = []
    for color in colors:
        color_results.append(
            ColorResult(
                hex=color["hex"],
                rgb=color["rgb"]
            )
        )
    
    return PaletteResponse(colors=color_results)