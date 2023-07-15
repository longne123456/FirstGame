import pygame
from button import Button
from Fighter import Fighter
from camera import CAMERAGROUP
from sys import exit

#màu
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (100,205,0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption('Ngo Quyen Fighter')

#timer
clock = pygame.time.Clock()
def current_time():
    return pygame.time.get_ticks
nhan_nut_time = 0   
pressed_keys = pygame.key.get_pressed()


# nhạc và hiệu ứng âm thanh
pygame.mixer.music.load("asset/audio/bgmusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
punch_fx = pygame.mixer.Sound("asset/audio/punch.mp3")
punch_fx.set_volume(0.1)
################################################################################# CAMERA ##########################################################################
camera_group = CAMERAGROUP()

fighter_1 = Fighter(1, 680, 200, False, 0,  punch_fx, camera_group)
fighter_2 = Fighter(2, 1180, 200, True, 0, punch_fx, camera_group)


##################################################################################################################################################

# Hàm (thanh máu)

run = True

while run:
    screen.fill('#71ddee')

    # Di chuyển nhân vật 
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
    fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1)


################################################################# Vẽ nhân vật ######################################################################
    fighter_1.draw(screen)
    fighter_2.draw(screen)


####################################################################################################################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()

   # cho máu giảm mượt
        if  pressed_keys[pygame.K_r] or  pressed_keys[pygame.K_t]:
            if current_time() - nhan_nut_time > 500:
                Fighter.__init__.attacking = False

    current_time()
   
    camera_group.update()
    #camera di theo ng choi nao
    camera_group.custom_draw(fighter_1)
    
    
    pygame.display.update()
    clock.tick(60)
    