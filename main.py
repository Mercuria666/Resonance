from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 设置输入音频文件路径
audio_path = "assets/123.mp3"

# 设置输出视频文件名
output_video_path = "output_video.mp4"

# 加载音频
audio = AudioFileClip(audio_path)

# 音频数据
audio_data = audio.to_soundarray()

# 视频时长
video_duration = audio.duration

# 设置视频的帧率和分辨率
fps = 24
width, height = 640, 480

# 创建一个空白图像作为背景
fig, ax = plt.subplots(figsize=(8, 6))
plt.axis('off')


# 定义用于生成视频帧的函数
def make_frame(t):
    # 计算音频索引
    audio_index = int(t * len(audio_data) / video_duration)

    # 在图像上绘制音频数据
    ax.clear()
    ax.plot(audio_data[:, 0])

    # 将Matplotlib图像转换为NumPy图像
    fig.canvas.draw()
    frame = np.array(fig.canvas.renderer.buffer_rgba())

    return frame


# 创建视频剪辑对象
video = VideoClip(make_frame, duration=video_duration)

# 将音频与视频进行合并
video = video.set_audio(audio)

# 设置视频的分辨率
video = video.resize((width, height))

# 生成最终的视频文件
video.write_videofile(output_video_path, fps=fps, codec="libx264")