from bs4 import BeautifulSoup
import requests


def getPlaylistLinks(url):
    r = requests.get(url)
    n = 1
    dominio = "www.youtube.com"
    soup = BeautifulSoup(r.text, 'html.parser')
    # for link in soup.find_all("a", class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):

    for link in soup.find_all("a", class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):
        titulo = link.string.strip()
        enla =  dominio + link.get("href")[:20]
        print(str(n) + "." + titulo)
        print(enla)
        print("")
        n += 1


getPlaylistLinks(
    'https://www.youtube.com/playlist?list=PLhixgUqwRTjywPzsTYz28I-qezFOSaUYz')

