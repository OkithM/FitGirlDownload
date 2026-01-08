from bs4 import BeautifulSoup
import requests
import webbrowser


fileCount = 5

Count = 1
urlStart = "https://fuckingfast.co"
urlEnd = ")"

file = open("links.txt", "r")
urls = file.readlines()

for url in urls:
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    scripts = soup.find_all("script")

    scripts = str(scripts)

    startindex = scripts.find(urlStart)

    scriptsLast = scripts[startindex:]

    endindex = scriptsLast.find(urlEnd) - 1

    downLink = scriptsLast[:endindex]
    
    print("Downloading : " + url + "\n")

    webbrowser.open(downLink)

    if Count%fileCount == 0:
        input("Press Enter to Download Next " + str(fileCount) + " File")
    Count += 1


input("Download Complete. Press Enter to Exit")
