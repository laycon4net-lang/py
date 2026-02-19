import requests
from PIL import Image, ImageDraw 
from io import BytesIO
API_KEY 
def detect_objects(image_path):
    response = requests.post(
        "https://api.deepai.org/api/object-detection",
        files = requests.post(
        headers={'image': open(image_path, 'b')},
        )
    )
    return response.json()
def draw_boxes(image_path, detecctions):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    for obj in detections["output"]["objects"]:
         x1  = obj["bounding_box"]["x1"]
         y1  = obj["bounding_box"]["y1"]
         x2  = obj["bounding_box"]["x2"]
         y2  = obj["bounding_box"]["y2"]
         label = obj["name"]
         draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
         draw.text ((x1, y1-10), label, fill="red")
    image.save("output.png")
    print("saved output.png")
path = input("enter image path:")
detections  = detect_objects(path)
draw_boxes(path, detections)