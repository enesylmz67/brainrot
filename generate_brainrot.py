from moviepy.editor import *
import numpy as np
import random
import os

print("BRAINROT FABRİKASI ÇALIŞIYOR...")

W, H = 1920, 1080
FPS = 60
DURATION = 30

def flashing_bg(t):
    if random.random() < 0.15:
        return np.ones((H, W, 3), dtype=np.uint8) * 255
    colors = [[255,0,100],[0,255,100],[100,0,255],[255,255,0]]
    color = np.array(random.choice(colors))
    return np.tile(color.reshape(1,1,3), (H, W, 1)).astype(np.uint8)

bg = VideoClip(flashing_bg, duration=DURATION).set_fps(FPS)

clips = [bg]
if os.path.exists("images"):
    for f in random.sample(os.listdir("images"), min(60, len(os.listdir("images")))):
        if f.lower().endswith(('.png','.jpg','.jpeg')):
            try:
                img = ImageClip(f"images/{f}").set_duration(random.uniform(0.1,0.6))
                img = img.resize(height=random.randint(300,900))
                img = img.set_pos(lambda t: (random.randint(-200,W), random.randint(-200,H)))
                img = img.rotate(lambda t: t*360*random.uniform(5,15))
                img = img.resize(lambda t: 1 + 0.6*np.sin(t*20))
                clips.append(img)
            except: pass

video = CompositeVideoClip(clips, size=(W,H)).set_fps(FPS)

audios = []
if os.path.exists("audio"):
    for f in os.listdir("audio"):
        if f.lower().endswith(('.mp3','.wav')):
            try:
                a = AudioFileClip(f"audio/{f}").volumex(random.uniform(0.8,2.5))
                audios.append(a.audio_loop(DURATION))
            except: pass

if audios:
    video = video.set_audio(CompositeAudioClip(audios).set_duration(DURATION))

video.write_videofile("brainrot_kaos.mp4", fps=FPS, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4, bitrate="8000k", logger=None)
print("BRAINROT HAZIR!")
