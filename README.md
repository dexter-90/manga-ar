# 🦉 manga-dl0

> This Is A Python Library That Allows You To Interact With 3asq

## ⚙ Installation :
[![Total Downloads](https://static.pepy.tech/personalized-badge/manga-dl0?period=total&units=none&left_color=black&right_color=blue&left_text=Total-Downloads)](https://pepy.tech/project/manga-dl0)
```bash
pip3 install manga-dl0
```

## ❓ Usage :
```python
from manga_dl0 import MangaDL

# Name Or URL (we recommend url)
obj = MangaDL(name='jujutsu kaisen', url="https://3asq.org/manga/jujutsu-kaisen/")

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

obj = MangaDL(url="https://3asq.org/manga/jujutsu-kaisen/", start=1, end=2)
obj.DownloadChapters()
```
## 🪐 Credits:
* [Dexter](https://github.com/dexter-90) For [Manga-dl0](https://github.com/dexter-90/manga-dl0)
# 
* ملاحظة لست مسؤولا عما تفعله بهذه المكتبة وما تقوم بتنزيله منها ولا أسامح من يحمل مانجا إباحية أو مانجا غير أخلاقية
