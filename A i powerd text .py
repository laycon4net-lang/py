import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
import os 
from colorama import init, Fore, Style
init(autorest=True)
API_KEY = "acc_6963c06af4a4f41"
API_SECRET = "767a1857b8879787b49cca2083334187"
IMAGGA_URL = "https://api.imagga.com/v2/tags"
def truncate_text(text, word_limit):
    words = text.split()
    return " ".join(words[:word_limit])
def get_imaga_tags_tags(image_path, limit=10 ):
    with open(image_path, "rb") as img:
     response = requests.post(
     IMAGGA_URL,
     auth=HTTPBasicAuth(API_KEY, API_SECRET),
     files={"image": img}

    )
    data = response.json()
    tags = data.get("result", {}).get("tags", [])
    return [tag["tag"]["en"] for tag in tags[:limit]]