import yt_dlp
import os
import subprocess
import ffmpeg
import speech_recognition as sr
#Downloading of the Youtube Video
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# download_video('https://youtu.be/KkCXLABwHP0?si=x84qF2-yybqAsCNF')
#Download Successfull

#Extraction of Audio
def extract_audio(video_path, audio_path):
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return
    try:
        ffmpeg_path = 'C:\\z\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'  # Update this path to your ffmpeg location
        command = [ffmpeg_path, '-i', video_path, audio_path]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Audio extraction completed!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during audio extraction: {e}")
        print(e.stderr)

# Example usage
# extract_audio('video.mp4', 'audio.wav')
#Extraction successfull

#Speech Recognition (Generating in text)

def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        return
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription completed!")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Example usage
transcript = transcribe_audio('audio.wav')
if transcript:
    print("Transcript:", transcript)


