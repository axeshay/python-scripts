import bs4 as bs
import os
import requests
os.makedirs('pexels', exist_ok=True)
user_input = str(input("Enter the search term: "))
res = requests.get("https://pexels.com/search/" + user_input)
soup = bs.BeautifulSoup(res.text, "lxml")
image_element = soup.select("article a img")
for i in range(0, len(image_element)):
    image_url = image_element[i].get('src').split("?")[0]
    print("Downloading image %s ...." % (image_url))
    image = requests.get(image_url)
    image.raise_for_status()
    imageFile = open(os.path.join('pexels',os.path.basename(image_url)),"wb")
    for img in image.iter_content(1000000):
        imageFile.write(img)
    imageFile.close()
print("Done")      
