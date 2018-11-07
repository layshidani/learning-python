
# coding: utf-8

# In[6]:

!pip3 install pygame
import pygame
pygame.init()
pygame.mixer.load('Exercício Python #021 - Tocando um MP3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
                   

