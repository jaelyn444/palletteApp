from PIL import Image # opens image files and lets us read their pixel data
import numpy as np  # lets us work with large arrays of numbers efficiently (1000 x1000 images)
from sklearn.cluster import KMeans  # the K-means algorithm itself, pre-built so we dont have to write from scratch 

def extract_colors (image_path: str, k: int = 6) -> list [dict]: # -> list [dict]: is a return type hint 
    image = Image.open(image_path)
    image = image.convert("RGB")

    image = image.resize ((150,150)) #Shrinks the image to 150x150 pixels before processing since K-means has to calculate distances between every cluster center
    pixels = np.array (image) #Converts the image into a numpy array.
    pixels = pixels.reshape(-1,3) #flattened list of colours

    kmeans = KMeans(n_clusters = k, random_state = 42, n_init = 10) #After fitting, cluster_centers_ contain the final K colours/center of each cluster
    kmeans.fit(pixels) # rounds of assign, average, repeat happen here 
    colors = kmeans.cluster_centers_.astype(int)

    result = []
    for color in colors:
        r, g, b = int(color[0]), int(color[1]), int(color[2])
        result.append({
            "rgb": [r,g,b],
            "hex": f"#{r:02x}{g:02x}{b:02x}"
        })
    return result 





