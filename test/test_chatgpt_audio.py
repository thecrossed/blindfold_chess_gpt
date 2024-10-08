from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
import datetime

# Load environment variables from the .env file (if present)
# load_dotenv()

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')
client = OpenAI()

# audio to text
def audio_to_text(filepath):
  audio_file= open(filepath, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  print(transcription.text)

# text to audio
def text_to_audio(text , outputfile):
  speech_file_path = Path(__file__).parent / "speech.mp3"
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
  )

  response.stream_to_file(speech_file_path)