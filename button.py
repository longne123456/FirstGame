import pygame
from option import Option

screen = pygame.display.set_mode((Option.SCREEN_WIDTH,Option.SCREEN_HEIGHT))
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw_button(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        screen.blit(self.image,(self.rect.x,self.rect.y))