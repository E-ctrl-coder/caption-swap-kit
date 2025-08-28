import os

input_video = "input/original.mp4"
input_subs = "output/translated.srt"
output_video = "output/final_video.mp4"

command = f'ffmpeg -i "{input_video}" -vf subtitles="{input_subs}" -c:a copy "{output_video}"'
os.system(command)

print("✅ Final video created with burned-in captions: output/final_video.mp4")
