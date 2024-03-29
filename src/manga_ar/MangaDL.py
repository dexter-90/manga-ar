"""
Library's:
1. requests => Get and Post Method (HTTP/1.1 Request)
2. bs4 => BeautifulSoup (Scraping 3asq Site)
3. PIL => Convert (Convert Image To PDF)
"""

import requests
from bs4 import BeautifulSoup
from PIL import Image

try:
    import img2pdf
except:
    pass



class MangaDL:

    def __init__(self, name: str = None, url: str = None, start: int = None, end: int = None):

        if url is not None and "https" not in url:
            if '3asq.org' not in url:
                raise ValueError(
                    "Enter A 3asq Link Not A Name Or Other Sites Link ! \nExample: https://3asq.org/manga/bleach/")
            raise ValueError("Enter A 3asq Link Start With HTTPS !")

        if url is None:
            self.url = str(Utility.Search(name=name))
        else:
            self.url = str(url)

        self.name = self.url.split('/')[4]
        self.start = start
        self.end = end
        self.info = Utility.Info(url=self.url)
        Utility.Check(self.Categories)

    @property
    def Cover(self):
        """Get Manga Cover URL From 3asq"""

        return {"Title": self.name.title(), "Cover": self.info["Cover"]}

    @property
    def Rating(self):
        """Get Manga Rating From 3asq"""

        return {"Title": self.name.title(), "Rating": self.info["Rating"]}

    @property
    def Status(self):
        """Get Manga Status From 3asq"""

        return {"Title": self.name.title(), "Status": self.info["Status"]}

    @property
    def Synonyms(self):
        """Get Manga Synonyms From 3asq"""

        return {"Title": self.name.title(), "Synonyms": self.info["Synonyms"]}

    @property
    def Categories(self):
        """Get Manga Categories From 3asq"""

        return {"Title": self.name.title(), "Categories": self.info["Categories"]}

    @property
    def Year(self):
        """Get Manga Year From 3asq"""

        return {"Title": self.name.title(), "Year": self.info["Year"]}

    @property
    def FirstChapter(self):
        """Get First Chapter In Manga From 3asq"""

        return {"Title": self.name.title(), "Last-Chapter": self.info["First-Chapter"]}

    @property
    def LastChapter(self):
        """Get Last Chapter In Manga From 3asq"""

        if self.name is None and self.url is None:
            raise Exception('"name" Or "url" Parameter Not Found')

        return {"Title": self.name, "Last-Chapter": self.info["Last-Chapter"]}

    def DownloadManga(self):
        """Download All Manga Chapters From 3asq"""

        chapters = Utility.Chapters(url=self.url)

        print("[$] Download..")
        for chapter in chapters:
            images = [img for img in Utility.Images(chapter)]
            num = str(chapter).split('/')[5]

            print(f"[+] Found {len(images)} Image For Chapter {num}")

            images = [requests.get(img).content for img in images]
            print("[+] Images Downloaded Successfully !")
            print("[+] Convert Image To PDF..")

            try:
                name = f"@{str(self.name).title()}" + num
                try:
                    Utility.ConvertPDF(images, name)
                except NameError:
                    try:
                        Utility.ConvertPDF2(images, name)
                    except:
                        raise Exception("Error With Convert To PDF !")

                print("[+] Images Converted Successfully !")
                print(f"[+] Chapter {num} Downloaded Successfully.\n\n")
            except Exception:
                a = chapter.split("/")
                name = f"@{a[4]}{a[5]}"

                try:
                    Utility.ConvertPDF(images, name)
                except NameError:
                    try:
                        Utility.ConvertPDF2(images, name)
                    except:
                        raise Exception("Error With Convert To PDF !")

                print("[+] Images Converted Successfully !")
                print(f"[+] Chapter {num} Downloaded Successfully.\n\n")

    def DownloadChapters(self):
        """Download Custom Manga Chapter From 3asq"""

        chapters = Utility.Chapters(url=self.url)

        try:
            a = chapters[self.start - 1:self.end]
        except IndexError:
            raise IndexError("Chapters Index Error")

        if not a:
            raise ValueError(f"Manga \"{self.url}\" Is Not Found")

        for chapter in a:
            num = str(chapter).split('/')[5]
            images = [img for img in Utility.Images(chapter)]
            print(f"[+] Found {len(images)} Image For Chapter {num}")

            images = [requests.get(img).content for img in images]
            print("[+] Images Downloaded Successfully !")

            try:
                print("[+] Convert Image To PDF..")
                name = f"@{str(self.name).title()}{num}"
                try:
                    Utility.ConvertPDF(images, name)
                except:
                    Utility.ConvertPDF2(images, name)

                print("[+] Images Converted Successfully")
                print(f"[+] Chapter {num} Downloaded Successfully.\n\n")

            except:
                print("[+] Convert Image To PDF..")
                a = self.url.split("/")
                name = f"@{a[4]}{a[5]}"

                try:
                    Utility.ConvertPDF(images, name)
                except NameError:
                    try:
                        Utility.ConvertPDF2(images, name)
                    except:
                        raise Exception("Error With Convert To PDF !")

                print("[+] Images Converted Successfully ! \n\n")
                print(f"[+] Chapter {a[5]} Downloaded Successfully.\n\n")

    @staticmethod
    def LastUpdates():
        """Get Last Updates From 3asq"""

        soup = BeautifulSoup(requests.get('https://3asq.org/').text, 'html.parser')
        manga = [i.text.strip() for i in soup.find_all('h3', {'class': 'h5'})]
        chapters = [i.text.strip() for i in soup.find_all('a', {'class': "btn-link"})]

        result = {}
        for i, j in zip(manga, chapters):
            result[i] = j
        return result


class Utility:

    @staticmethod
    def Chapters(url: str = None, name: str = None):
        """Get All Existing Chapters URL"""

        if url == "None":
            link = 'https://3asq.org/manga/' + name + '/ajax/chapters/'

        else:
            name = str(url.split('/')[4])
            link = 'https://3asq.org/manga/' + name + '/ajax/chapters/'

        r = requests.post(link, headers={
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://3asq.org',
            'referer': 'https://3asq.org/manga/' + name + '/',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        })
        soup = BeautifulSoup(r.text, 'html.parser')
        data_link = [child for child in soup.findAll("li", {"class": "wp-manga-chapter"})]
        links = [link.find('a')['href'] for link in data_link]
        links.reverse()

        return links

    @staticmethod
    def Images(url: str):
        """Get All Images From Chapter URL"""

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image_data = [child['src'] for child in soup.findAll("img", {"class": "wp-manga-chapter-img"})]
        image_links = [link.strip() for link in image_data]
        return image_links

    @staticmethod
    def Search1(name: str):

        """Search Manga Name On 3asq And Return All Result In List"""

        if name.startswith("http"):
            raise ValueError("Enter A Name In The Name Parameter, Not A Link")

        name = name.replace(' ', '+')

        url = "https://3asq.org/wp-admin/admin-ajax.php"
        data = f"action=wp-manga-search-manga&title={name}"

        r = requests.post(url, data, headers={
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://3asq.org',
            'referer': 'https://3asq.org/?s=Hero&post_type=wp-manga',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'})

        try:
            data = [url['url'] for url in r.json()['data']]
            titles = [url['title'] for url in r.json()['data']]
            manga = [{'title': a, 'url': b, } for a, b in zip(titles, data)]
            manga.reverse()
        except KeyError:
            manga = [{'title': None, 'url': None, }]

        return manga

    @staticmethod
    def Search2(name: str):
        """Search Manga Name On 3asq And Return All Result In List (2)"""

        params = {
            's': name,
            'post_type': 'wp-manga',
            'op': '',
            'author': '',
            'artist': '',
            'release': '',
            'adult': '',
        }

        response = requests.get('https://3asq.org/', params=params)
        soup = BeautifulSoup(response.text, 'html.parser').find('h3', {'class': "h4"})
        if soup is not None:
            soup = soup.find('a')['href']

        return soup

    @staticmethod
    def Search3(name: str):
        """Search Manga Name On 3asq And Return All Result In List (3)"""

        response = requests.get(f"https://3asq.org/manga/{name.replace(' ', '-')}")
        return response.url if response.status_code != 404 else None

    @staticmethod
    def Search(name: str):
        url = Utility.Search1(name)[0]["url"]
        if url is None:
            url = Utility.Search2(name)
            if url is None:
                url = Utility.Search3(name)
                if url is None:
                    raise NameError(f"Name \"{name}\" is not found")
        return url

    @staticmethod
    def ConvertPDF(images: list, name: str):
        """Convert Image List To PDF (1)"""

        with open(name + ".pdf", "wb") as pdf:
            pdf.write(img2pdf.convert(images))

    @staticmethod
    def ConvertPDF2(images: list, name: str):
        """Convert Image List To PDF (2)"""

        images2 = [
            Image.open(f).convert('RGB')
            for f in images]
        images2[0].save(name + ".pdf", save_all=True, append_images=images2[1:])

    @staticmethod
    def Info(url):
        """Get Manga Info
        (Cover, Categories, Synonyms, Status, year, rating, Title.)"""

        soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        summary_content = soup.find_all('div', {"class": "summary-content"})
        year = summary_content[-2].text.strip()
        synonyms = summary_content[2].text.strip()
        status = summary_content[-1].text.strip()
        categories = soup.find('div', {"class": "genres-content"}).text.strip().split(",")
        rating = soup.find('div', {"class": "summary-content vote-details"}).text.strip()
        cover = soup.find_all('img', {'class': "img-responsive"})[1]['src'].strip()
        chapters = Utility.Chapters(url=url)
        return {"Title:": f"{url.split('/')[4]}", "Year": year, "Rating": rating, "Categories": categories,
                "Synonyms": synonyms, "Status": status, "Cover": cover, "First-Chapter": chapters[0],
                "Last-Chapter": chapters[-1]}

    @staticmethod
    def Check(categories):
        """Check If The Manga Unethical"""
        if "حريم" in categories or "إيتشي" in categories['Categories']:
            raise Exception("Sorry We Can't Help You, Because Your Manga Is An Unethical.")
