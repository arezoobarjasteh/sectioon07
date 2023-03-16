import moviepy 
import editor
video=editor.VideoFileClip('hatef.mp4')
video.audio.write_audiofile ('hattef.mp3')