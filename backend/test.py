from algorithms.kmeans import extract_colors
from algorithms.kmeans import extract_colors
from algorithms.paint_mixing import find_paint_mix

results = extract_colors("test_image.jpg", k=6)

for color in results:
    print(color)

for color in results:
    print(f"\nColor: {color['hex']}")
    mix = find_paint_mix(color['rgb'])
    print(f"Mix: {mix}")


