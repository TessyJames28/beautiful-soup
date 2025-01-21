from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

# Download an image from the website
url = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = BeautifulSoup(url.content, 'lxml')

# Find the image
image_link = "https://keithgalli.github.io/web-scraping/"
images = soup.select("img")
for image in images[:4]:
    image_url = image['src']
    if image_url.startswith("./"):
        image_url = image_url[2:]
    image_name = image_url.split("/")[-1]

    image_path = image_link + image_url
    image_response = requests.get(image_path) # open the image with the request method
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image.save(image_name)
        print(f"Image {image_name} downloaded successfully")
    else:
        print(f"Failed to download image {image_name}")