import yt_dlp

# İndirmek istediğin video URL'si
url = input("Enter video URL: ")

# Ayarlar
ydl_opts = {
    "format": "best",  # En iyi çözünürlükte indir
    "outtmpl": "%(title)s.%(ext)s",  # Dosya adı video başlığı olacak
}

# İndirme işlemi
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("İndirme tamamlandı!")


