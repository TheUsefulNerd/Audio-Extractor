from pytube import YouTube
import os

yt = YouTube(input("Paste the Youtube link here: "))

vid = yt.streams.filter(only_audio=True).first()

destination = "C:\\Users\\ADVAIT\\Music"

output = vid.download(output_path=destination)

base, ext = os.path.split(output)
new_file = os.path.join(base, os.path.splitext(ext)[0] + ".mp3")
os.rename(output, new_file)

print(yt.title + "has been successfully downloaded!!")
