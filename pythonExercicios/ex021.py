import pygame
# iniciando pygame
pygame.init()
# chamando a musica
pygame.mixer.music.load('ex021.mp3')
# play na musica
pygame.mixer.music.play()
input()
pygame.event.wait()


'''Forma de colocar audio ou musica'''