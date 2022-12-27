from moviepy.editor import VideoFileClip
import urllib.request
import os
from datetime import datetime

channel = [193, 304, 171, 211, 131, 335, 1600]

urllib.request.urlretrieve("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_512_" + str(channel[datetime.now().weekday()]) + ".mp4", "sdo_vid.gif")
videoClip = VideoFileClip("sdo_vid.gif")
videoClip.speedx(10).write_gif("sdo_vid.gif", fps=10)
