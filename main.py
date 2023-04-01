import pygame
import random

#Useful later if we want to read from file, more files to read
import os

pygame.init()

# Potentially create an array of emotions and map them to the sound files if we have enough emotions
# and sounds

while True:
    ui = input("Please enter an emotion: ")
    ui = ui.strip().lower()
    rand = random.randint(0, 99)

    if ui == "quit":
        # Clean up the pygame library
        sound = pygame.mixer.Sound('Sounds/powerdown.mp3')
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
        pygame.quit()
        break

    if ui == "happy":
        sound = pygame.mixer.Sound('Sounds/happy.mp3')
    elif ui == "nervous":
        if rand < 49:
            sound = pygame.mixer.Sound('Sounds/cute.mp3')
        else:
            sound = pygame.mixer.Sound('Sounds/cute2.mp3')
    else:
        if rand < 49:
            sound = pygame.mixer.Sound('Sounds/beep.mp3')
        else:
            sound = pygame.mixer.Sound('Sounds/hi-tech beep.mp3')

    sound.play()

    # Wait for the sound to finish playing
    pygame.time.wait(int(sound.get_length() * 1000))