"""
Librarys:
1. requests => Get and Post Method (HTTP/1.1 Request)
2. bs4 => BeautifulSoup (Scraping 3asq Site)
3. img2pdf => Convert (Convert Imgae To PDF)
"""

import time
import requests
from bs4 import BeautifulSoup
from utility import ConvertPDF, Search, Chapters, Images

class MangaDL4:

    def __init__(self, name: str = None, url: str = None, start: int = None, end: int = None):
        if name is None and url is None:
            raise Exception('"name" Or "url" Parameter Not Found')

        self.name = name
        self.url = url
        self.start = start
        self.end = end

    

    def Cover(self):
        """Get Manga Cover URL From 3asq"""

        if self.url is None:
            self.url = Search(self.name)[0]['url']
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        cover = soup.find_all('img', {'class': "img-responsive"})[1]['src'].strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Cover": cover}

    def Rating(self):
        """Get Manga Rating From 3asq"""
        
        global url
        if self.url is None:
            self.url = Search()[0]
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        rating = soup.find('div', {"class": "summary-content vote-details"}).text.strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Rating": rating}

    def Status(self):
        """Get Manga Status From 3asq"""

        if self.url is None:
            self.url = Search()[0]
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        status = soup.find_all('div', {"class": "summary-content"})[-1].text.strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Status": status}

    def Synonyms(self):
        """Get Manga Synonyms From 3asq"""

        global url
        if self.url is None:
            self.url = Search(self.name)[0]['url']

        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        synonyms = soup.find_all('div', {"class": "summary-content"})[2].text.strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Synonyms": synonyms}

    def Categories(self):
        """Get Manga Categories From 3asq"""

        if self.url is None:
            self.url = Search(self.name)[0]['url']
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        categories = soup.find('div', {"class": "genres-content"}).text.strip()
        return {"Title:": f"{self.url.split('/')[4]}", "categories": categories}

    def Year(self):
        """Get Manga Year From 3asq"""

        if self.url is None:
            self.url = Search(self.name)[0]['url']
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        year = soup.find_all('div', {"class": "summary-content"})[-2].text.strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Year": year}


    def Info(self):
        """Get Manga Info 
        (Cover, Categories, Synonyms, Status, year, rating, Title.)"""

        if self.url is None:
            self.url = Search(self.name)[0]['url']
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')

        summary_content = soup.find_all('div', {"class": "summary-content"})
        year = summary_content[-2].text.strip()
        synonyms = summary_content[2].text.strip()
        status = summary_content[-1].text.strip()
        categories = soup.find('div', {"class": "genres-content"}).text.strip()
        rating = soup.find('div', {"class": "summary-content vote-details"}).text.strip()
        cover = soup.find_all('img', {'class': "img-responsive"})[1]['src'].strip()
        return {"Title:": f"{self.url.split('/')[4]}", "Year": year, "Rating": rating, "Categories": categories,
                "Synonyms": synonyms, "Status": status, "Cover": cover}


    def DownloadManga(self):
        """Download All Manga Chapters From 3asq"""

        if self.start is None or self.end is None:
            raise Exception('"Start" Or "End" Parameter Not Found')
        
        if self.url is None:
            chapters = Chapters(url=Search(self.name)[0]['url'])
        else:
            chapters = Chapters(url=str(self.url[0]['url']))

        print("[$] Download..")
        for chapter in chapters:
            images = [requests.get(img).content for img in Images(chapter)]
            print(f"[+] Found {len(images)} Image For Chapter {chapter}")
            try:
                print("[+] Convert Image To PDF..")
                ConvertPDF(images, f"@{str(self.name).title()}{str(chapter).split('/')[5]}")
                print("[+] Images Converted Successfully")
            except:
                print("[+] Convert Image To PDF..")
                a = self.url.split("/")
                num = a[5]
                manga = a[4]
                ConvertPDF(images, f"@{manga}{num}")
                time.sleep(1)
                print("[+] Images Converted Successfully ! \n\n")


    def DownloadChapters(self):
        """Download Custom Manga Chapter From 3asq"""

        if self.start is None or self.end is None:
            raise Exception('"Start" Or "End" Parameter Not Found')

        if self.url is None:
            chapters = Chapters(url=str(Search(self.name)[0]))
        else:
            chapters = Chapters(url=self.url)

        print("[$] Download..")
        for chapter in chapters[self.start:self.end + 1]:
            images = [requests.get(img).content for img in Images(chapter)]
            print(f"[+] Found {len(images)} Image For Chapter {chapter}")
            time.sleep(1)
            print("[+] Images Downloaded Successfully !")
            time.sleep(1)

            try:
                print("[+] Convert Image To PDF..")
                ConvertPDF(images, f"@{str(self.name).title()}{str(chapter).split('/')[5]}")
                print("[+] Images Converted Successfully")

            except:
                print("[+] Convert Image To PDF..")
                a = self.url.split("/")
                num = a[5]
                manga = a[4]
                ConvertPDF(images, f"@{manga}{num}")
                time.sleep(1)
                print("[+] Images Converted Successfully ! \n\n")

    def LastUpdates(self):
        """Get Last Updates From 3asq"""
        soup = BeautifulSoup(requests.get('https://3asq.org/').text, 'html.parser')
        manga = [i.text.strip() for i in soup.find_all('h3', {'class': 'h5'})]
        chapters = [i.text.strip() for i in soup.find_all('a', {'class': "btn-link"})]
        result = {}
        for i, j in zip(manga, chapters):
            result[i] = j
        return result

