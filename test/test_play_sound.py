import pygame
import time
import threading

def play_music(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.play()

#play_music("/Users/jasminezhu/blindfold_chess_gpt/test/speech.mp3")

def wait_for_input():
    input()
    pygame.mixer.music.stop()

music_thread = threading.Thread(target= play_music, args=("/Users/jasminezhu/blindfold_chess_gpt/test/speech.mp3",))
input_thread = threading.Thread(target = wait_for_input)

music_thread.start()
input_thread.start()