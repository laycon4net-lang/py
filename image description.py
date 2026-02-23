import requests 
from requests.auth import HTTPBasicAuth
API_kEY = "acc_6963c06af4a4f41"
API_SECRET = "767a1857b8879787b49cca2083334187"
def caption_single_image(image_path):
    url = "https://api.imagga.com/v2/tags"
    with open(image_path, "rb")as img:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(API_kEY, API_SECRET),
            files={"image": img}
        )
    data = response.json()
    tags = data ["result"]["tags"][:5]
    caption =", ".join(tag["tag"]["en"]for tag in tags)
    print("Image:", image_path)
    print("Caption (generated from tags):", caption)
def main():
        image_path = input("Enter image path:")
        caption_single_image(image_path)
if __name__ == "__main__":

 main()
