import pygame
from Fighter import Fighter
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
bg_image = pygame.image.load("asset/images/background/ngoquyenbg1.jpg").convert_alpha()

pygame.display.set_caption('Ngo Quyen Fighter')

#timer
clock = pygame.time.Clock( )
def current_time():
    return pygame.time.get_ticks
nhan_nut_time = 0
pressed_keys = pygame.key.get_pressed()

# Hàm vẽ background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0, 0))


# Hàm (thanh máu)
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))

# nhạc và hiệu ứng âm thanh
pygame.mixer.music.load("asset/audio/bgmusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
punch_fx = pygame.mixer.Sound("asset/audio/punch.mp3")
punch_fx.set_volume(0.1)

# Tạo 2 nhân vật
fighter_1 = Fighter(True,200, 350,False,0,punch_fx)
fighter_2 = Fighter(False,700, 350,True,0,punch_fx)


while True:

    # Vẽ background
    draw_bg()

    # Hiện thông tin nhân vật
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    # Di chuyển nhân vật
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)

    # Vẽ nhân vật
    fighter_1.draw(screen)
    fighter_2.draw(screen)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

   # cho máu giảm mượt
        if  pressed_keys[pygame.K_r] or  pressed_keys[pygame.K_t]:
            if current_time() - nhan_nut_time > 500:
                Fighter.__init__.attacking = False



    current_time()
    pygame.display.update()
    
    clock.tick(60)