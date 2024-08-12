import pygame
import time
import threading
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import datetime
import wave
import sys
import pyaudio

# Load environment variables from the .env file (if present)
# load_dotenv()

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')
client = OpenAI()

def play_music(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.play()

#play_music("/Users/jasminezhu/blindfold_chess_gpt/test/speech.mp3")

def wait_for_input():
    input()
    pygame.mixer.music.stop()

def play_audio(filepath):
    music_thread = threading.Thread(target= play_music, args=(filepath,))
    input_thread = threading.Thread(target = wait_for_input)

    music_thread.start()
    input_thread.start()

# text to audio
def text_to_audio(text , outputfile):
  speech_file_path = Path(__file__).parent / outputfile
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
  )

  response.stream_to_file(speech_file_path)

# audio to text
def audio_to_text(filepath):
  audio_file= open(filepath, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  print(transcription.text)
  return transcription.text

def record(output_file):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = 5

    with wave.open(output_file, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()
