
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920,1080))

pygame.display.set_caption('The chosen one')

clock = pygame.time.Clock( )

while True:

    #draw bg
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    #move fighter
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)

    #draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    
    clock.tick(60)