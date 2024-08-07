from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
# load_dotenv()

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

OPENAI_API_KEY  = os.getenv('OPENAI_API_KEY')
client = OpenAI()

audio_file= open("/Users/jasminezhu/blindfold_chess_gpt/resource/test_audio.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=transcription.text
)

response.stream_to_file(speech_file_path)