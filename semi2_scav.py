import os
from imageio.plugins import ffmpeg


#  cut a 10 second clip
os.system("ffmpeg -ss 00:00:00 -i bbb_original.mp4 -c copy -t 00:00:10.0 bbb_cut.mp4".format("mp4"))
#  show YUV histogram
os.system("ffplay bbb_cut.mp4 -vf histogram".format("mp4"))
#  show YUV histogram over clip
os.system("ffplay bbb_cut.mp4 -vf “split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay”".format("mp4"))
#  resize to 720p
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=1280:720 bbb_720p.mp4".format("mp4"))
#  resize to 480p
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=720:480 bbb_480p.mp4".format("mp4"))
#  resize to 360x240
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=360:240 bbb_360x240.mp4".format("mp4"))
#  resize to 160x120
os.system("ffmpeg -i bbb_cut.mp4 -vf scale=160:120 bbb_160x120.mp4".format("mp4"))
#  audio to mono and change the audio codec
os.system("ffmpeg -i bbb_cut.mp4 -ac 1 bbb_mono.flac".format("mp4"))
