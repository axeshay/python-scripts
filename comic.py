#downloadXkcd.py - Downloads every single XKCD comic.

import requests,bs4,os
url = "https://xkcd.com"
os.makedirs("xkcd",exist_ok = True)
while not url.endswith("#"):
    print("Downloading the page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"lxml")
    element = soup.select("#comic img")
    if(element) == []:
        print("image not found")
    else:
        comicUrl = element[0].get('src').strip("http://")
        comicUrl="http://"+comicUrl
        if 'xkcd' not in comicUrl:
            comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]

        print("comic url",comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        #save image to ./xkcd
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select("a[rel='prev']")[0]
    url = "http://xkcd.com" + prevLink.get("href")
print("Done")    
