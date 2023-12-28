import assemblyai as aai
from moviepy.editor import VideoFileClip


aai.settings.api_key ='8abfcb3c51c045e6aed9ec97a757ed5d'
video = VideoFileClip('blue_green.mp4')
vido_audio = video.audio
vido_audio.write_audiofile('blue_green.mp3')


# FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
FILE_URL = 'blue_green.mp3'
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript.text)