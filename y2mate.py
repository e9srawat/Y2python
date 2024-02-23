"""
YOUTUBE TO MP4
"""

import requests

# https://www.youtube.com/watch?v=dQw4w9WgXcQ
youtube = input("Enter YouTube link: ")
youpak = "https://youpak.com" + youtube[23:]
print("processing...")
data = (requests.get(youpak).text).split('<div class="btn-group btn-group-justified">')[
    1
]

flag = True
while flag:
    resolution = input("Select resolution \n1. 720p \n2. 360p \n")
    if resolution == "1":
        data = data.split("720P HD (mp4)")[0]
        link = data[10:-97]
        flag = False
    elif resolution == "2":
        data = data.split("720P HD (mp4)")[1]
        data = data.split("360P (mp4)")[0]
        link = data[14:-91]
        flag = False
    else:
        print("Illegal selection")


print("Downloading File...")
vid = requests.get(link)
print(link)
print("File Downloaded")
with open("video.mp4", "wb") as f:
    print("Writing file...")
    f.write(vid.content)
    print("File Created!")
