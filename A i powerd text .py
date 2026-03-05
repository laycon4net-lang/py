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
def generate_Caption(tags):
   return truncate_text(", ".join(tags), 5)
def generate_descrption(tags):
   sentence = (
      f"This image show {tags[0]}."
      f"it includes elements such as {', '.join(tags[1:6])}."
      f"The scene appears visunlly clear and well composed."
   )
   return truncate_text(sentence, 30)
def generate_summary(tags):
   sentence =(
      f"The image primarily features {tags[0]}."
      f"Other visible element include {', '.join(tags[1:7])}"
      f"The object are clerly distinguishable and form a meaningful scene."
      f"The image provides a simple yet informative visual representation."
   )
   return trucante_text(sentence, 50)
def print_menu():
    print(f"""{Style.BRIGHT}
================ IMAGE-TO-TEXT CONVERSION =================

Select output type:

1. Caption (5 words)

2. Description (30 words)

3. Summary (50 words)

4. Exit

===========================================================

""")
 
def main():
   image_path = input (f"{Fore.BLUE}Enter image path: (Style.RESET_ALL)")
   if not os.path.exists(image_path):
      print(f"{Fore.RED} Image file not found.")
      return
   try:
      Image.open(image_path)
   except:
      print(f"{Fore.RED} Invalid image file.")
      return
   print(f"{Fore.YELLOW}")