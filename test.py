import pygame
from pygame import display, event
pygame.init()
display.set_caption('Test')
screen= display.set_mode((512,512))
running=True
while running:
    current_events=event.get()
    for x in current_events:
        if x.type==pygame.QUIT:
            running= False
print('Thanks for Playing')