"""
Librarys:
1. requests => Get and Post Method (HTTP/1.1 Request)
2. bs4 => BeautifulSoup (Scraping 3asq Site)
3. img2pdf => Convert (Convert Imgae To PDF)
"""

import requests
from bs4 import BeautifulSoup
import img2pdf

def Chapters(url: str=None, name: str=None, ):
    """Get All Existing Chapters URL"""

    if url is None:
        link = 'https://3asq.org/manga/' + name + '/ajax/chapters/'
    else:
        manga_name = url.split('/')[4]
        link = 'https://3asq.org/manga/' + manga_name + '/ajax/chapters/'
    r = requests.post(link, headers={
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://3asq.org',
        'referer': 'https://3asq.org/manga/' + manga_name + '/',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    })
    soup = BeautifulSoup(r.text, 'html.parser')
    data_link = [child for child in soup.findAll("li", {"class": "wp-manga-chapter"})]
    links = [link.find('a')['href'] for link in data_link]
    links.reverse()
    return links


def Images(url: str):
    """Get All Images From Chapter URL"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    image_data = [child['src'] for child in soup.findAll("img", {"class": "wp-manga-chapter-img"})]
    image_links = [link.strip() for link in image_data]
    return image_links


def Search(name: str):
    """Search Manga Name On 3asq And Return All Result In List"""
    if name.startswith("http"):
        raise Exception("Enter A Manga Name Not URL")
    name = name.replace(' ', '+')
    url = "https://3asq.org/wp-admin/admin-ajax.php"
    data = f"action=wp-manga-search-manga&title={name}"
    r = requests.post(url, data, headers={
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://3asq.org',
        'referer': 'https://3asq.org/?s=Hero&post_type=wp-manga',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    })
    data = [url['url'] for url in r.json()['data']]
    titles = [url['title'] for url in r.json()['data']]
    manga = [{'title': a, 'url': b, } for a, b in zip(titles, data)]
    manga.reverse()
    return manga

def ConvertPDF(images: list, name: str):
    """Convert Image List To PDF"""

    with open(f"{name}.pdf", 'wb') as file:
        file.write(img2pdf.convert(images))
        file.close()
