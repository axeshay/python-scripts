import pyperclip,requests,bs4,sys
res = requests.get("http://en.wikipedia.org/wiki/" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html")
obj = soup.select(".mw-parser-output p")
file = open("wikiinfo.txt","wb")
for data in obj:
    dataa = pyperclip.copy(data)
file.write(dataa)



''' STACKOVERFLOW


from bs4 import BeautifulSoup
import requests

respond = requests.get("http://pl.wikipedia.org/wiki/StackOverflow")
soup = BeautifulSoup(respond.text)
l = soup.find_all('p')
print l[0].text '''

    
