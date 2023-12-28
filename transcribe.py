# import speech_recognition as sr
# from pydub import AudioSegment
#
#
# audio_seg = AudioSegment.from_file('cut.webm')
# audio_seg.export('audio.wav',format='wav')
#
#
# rr = sr.Recognizer()
# with sr.AudioFile('audio.wav') as source:
#     audio = rr.record(source)
#     text = rr.recognize_google_cloud(audio)
# print(text)

import deep