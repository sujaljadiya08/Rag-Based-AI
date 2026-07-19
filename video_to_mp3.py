#convert all mp4 to mp3

import os
import subprocess

files = os.listdir("videos")
os.makedirs("audios", exist_ok=True)
for file in files:
    #print(files)
    tutorial_number = file.split('Tutorial #')[1].split()[0]
    file_name = file.split('_')[0].strip()
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])