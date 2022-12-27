from moviepy.editor import VideoFileClip
import urllib.request
import os
from datetime import datetime

channel = [193, 304, 171, 211, 131, 335, 1600]

url = "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_512_" + str(channel[datetime.now().weekday()]).zfill(4) + ".mp4"
print(url)

urllib.request.urlretrieve(url, "sdo_vid.mp4")
videoClip = VideoFileClip("sdo_vid.mp4")
videoClip.speedx(3).fadein(1).fadeout(1).write_gif("sdo_vid.gif", fps=10)
