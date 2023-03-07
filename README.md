# manga-dl4

- ***Developer => Dexter***

### To install:

```bash
pip3 install manga-dl0
```

### How to use:
```bash
from manga_dl0 import MangaDL

# Name Or URL (we recommend url)
obj = MangaDL(name='attack on titan no requiem', url="https://3asq.org/manga/attack-on-titan-no-requiem/")

obj.DownloadManga()  # Download All Manga Chapter From 3asq
info = obj.Info()  # Get Manga Info From 3asq
year = obj.Year()  # Get Manga Year From 3asq
Status = obj.Status()  # Get Manga Status From 3asq
rating = obj.Rating()  # Get Manga Rating From 3asq
Synonyms = obj.Synonyms()  # Get Manga Synonyms From 3asq (not accurate)
Categories = obj.Categories()  # Get Manga Categories From 3asq
Cover = obj.Cover()  # Get Manga Cover URL From 3asq
Last_Update = obj.LastUpdates()  # Get Last Chapters Upload In 3asq Manga (not accurate)
FirstChapter = obj.FirstChapter()  # Get Last Chapter In Manga From 3asq
LastChapter = obj.LastChapter()  # Get Last Chapter In Manga From 3asq

# Download Custom Chapters From 3asq
# Name Or URL, Start And URL
# Mean => Download "Attack On Titan" Manga From Chapter 1 To Chapter 2
# Note => It will download the first chapter on the site (the existing), not the real first chapter

obj = MangaDL(url="https://3asq.org/manga/attack-on-titan-no-requiem/", start=1, end=2)
obj.DownloadChapters()
```