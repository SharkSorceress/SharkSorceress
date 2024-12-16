#from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_writer import ffmpeg_write_video
from moviepy.video.fx import MutiplySpeed, FadeOut
import urllib.request
import os
from datetime import datetime

channel = [193, 304, 171, 211, 131, 335, 1600]

url = "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_512_" + str(channel[datetime.utcnow().weekday()]).zfill(4) + ".mp4"
print(url)

urllib.request.urlretrieve(url, "sdo_vid.mp4")
videoClip = VideoFileClip("sdo_vid.mp4", target_resolution=(256, 256))
videoClip = MultiplySpeed.MultiplySpeed(2).apply(videoClip)
videoClip = FadeOut.FadeOut(0.5).apply(videoClip)
ffmpeg_write_video.ffmpeg_write_video(videoClip, "sdo_vid.gif", 10)
# videoClip = VideoFileClip("sdo_vid.mp4").resize(height=256)
#videoClip.speedx(2).fadeout(0.5).write_gif("sdo_vid.gif", fps=10)
