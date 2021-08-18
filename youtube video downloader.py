from pytube import YouTube 


link = input("Paste the youtube link here: ")
yt = YouTube(link)

print("Title: ",yt.title)
print("Number of Views: ",yt.views)

length = yt.length
if length > 60 or length == 60:
    print("length of video approx: ",round(length//60),"minutes")
else:
    print("length of video: ",length,"seconds")

print("Rating: ",yt.rating)
print("descpription",yt.description)
ys = yt.streams.get_highest_resolution()

print("Downloading..")
ys.download("C:/Users/DELL/Desktop/Python projects/Projects/youtube video downloader/Downloaded youtube video")
print("Download is complete")
