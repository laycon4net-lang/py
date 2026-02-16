import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"

    response = requests.get(url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))
    return img


def post_process_image(image):
    image = ImageEnhance.Brightness(image).enhance(1.2)
    image = ImageEnhance.Contrast(image).enhance(1.3)
    return image.filter(ImageFilter.GaussianBlur(radius=2))


def download_image(image, filename="generated_image.png"):
    image.save(filename)
    print(f"Image saved successfully as {filename}")


img = generate_image("A cat flying in space")

processed_img = post_process_image(img)

processed_img.show()

download_image(processed_img, "cat_in_space.png")
