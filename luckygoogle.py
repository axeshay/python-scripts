import requests,bs4,sys,webbrowser

print("Googling.....>")
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html")
linkElements = soup.select(".r a")
numOpen = min(5,len(linkElements))
for i in range(numOpen):
    webbrowser.open("http://google.com" + linkElements[i].get("href"))                   
