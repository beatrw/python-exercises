#Programa que toca uma música (usando biblioteca de jogos)

import pygame
pygame.init()
pygame.mixer.music.load('vini.mmp3')
pygame.mixer.music.play()
pygame.event.wait()