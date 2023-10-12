from pytube import YouTube
link=input("Enter your youtube url:")
yt=YouTube(link)
videos=yt.streams.all()
video=list(enumerate(videos))
for i in video:
    print(i)
print("Enter the desired option to download")
dn_option=int(input("Enter the option:"))
dn_video=videos[dn_option]
dn_video.download()
print("dowloaded successfully")
