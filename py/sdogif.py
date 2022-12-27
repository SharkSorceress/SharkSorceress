from moviepy.editor import VideoFileClip
import urllib.request
import os

channel = os.environ["SDO_CHANNEL"]

urllib.request.urlretrieve("https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_512_" + channel + ".mp4", "sdo_vid.gif")
videoClip = VideoFileClip("sdo_vid.gif")
videoClip.speedx(10).write_gif("sdo_vid.gif", fps=10)
