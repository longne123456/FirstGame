import pygame
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

#load ảnh background
#bg_image = pygame.image.load("asset/images/background/truong.png").convert_alpha()

pygame.display.set_caption('Ngo Quyen Fighter')

#timer
clock = pygame.time.Clock()
def current_time():
    return pygame.time.get_ticks
nhan_nut_time = 0   
pressed_keys = pygame.key.get_pressed()

# Hàm vẽ background
#def draw_bg():
    #scaled_bg = pygame.transform.scale(bg_image, (80, 100))
    #screen.blit(bg_image,(0, 0))



# nhạc và hiệu ứng âm thanh
pygame.mixer.music.load("asset/audio/bgmusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
punch_fx = pygame.mixer.Sound("asset/audio/punch.mp3")
punch_fx.set_volume(0.1)
################################################################################# CAMERA ##########################################################################
camera_group = CAMERAGROUP()


fighter_1 = Fighter(1, 680, 400, False, 0,  punch_fx, camera_group)
fighter_2 = Fighter(2, 1180, 400, True, 0, punch_fx, camera_group)


##################################################################################################################################################

# Hàm (thanh máu)
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))



while True:
    screen.fill('#71ddee')
    # Hiện thông tin nhân vật
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


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
    