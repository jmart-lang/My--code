import pygame
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(script_dir, '..', 'music', 'labirint.wav',)

# initialize the pygame library
pygame.init()

# load the music file
pygame.mixer.music.load(music_path)

# play the music on loop
pygame.mixer.music.play(-1)

# keep the program running
while True:
    continue