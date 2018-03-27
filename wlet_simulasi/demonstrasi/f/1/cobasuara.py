import pygame
import time
for i in range(1,10):

    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()

    time.sleep(15)
