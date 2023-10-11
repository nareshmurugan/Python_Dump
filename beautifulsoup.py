import requests
from bs4 import BeautifulSoup

URL="https://www.instagram.com/{}/"

def pic_downloader(username):
    r=requests.get(URL.format(username))
    s=BeautifulSoup(r.text,"html.parser")
    
    p=s.find("meta",property="og:image").attrs['content']
    with open(username+".jpg","wb") as pic:
        binary = requests.get(p).content
        pic.write(binary)
if __name__=="__main__":
    username="lawanya"
    pic_downloader(username)

