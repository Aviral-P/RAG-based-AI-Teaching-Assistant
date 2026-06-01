import os
import subprocess

files= os.listdir("videos")
for file in files:
    file_name = os.path.splitext(file)[0]
    output_file = f"audios/{file_name}.mp3"
    subprocess.run(["ffmpeg","-i", f"videos/{file}", output_file])