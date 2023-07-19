import pygame
from button2 import Button2
from Fighter import Fighter
from camera import CAMERAGROUP
from sys import exit
#from menu import mainMenu

#background font
BG = pygame.image.load("asset/menu.png")
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font/font.ttf", size)

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
#mainMenu(screen)
#mainMenu.main_menu()
def after_playbutton():
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



def play():
    while True:
        after_playbutton()
        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button2(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button2(image=pygame.image.load("asset/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button2(image=pygame.image.load("asset/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button2(image=pygame.image.load("asset/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()