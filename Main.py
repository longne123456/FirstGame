import sys
import pygame
from option import Option
from button2 import Button2
from Fighter import Fighter
from camera import CAMERAGROUP

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (100,205,0)

SCREEN_WIDTH = Option.WITDH(0)
SCREEN_HEIGHT = Option.HEIGHT(0)

player1_size = 162
player1_scale = 4
player1_offset = [72, 56]
player1_data = [player1_size, player1_scale, player1_offset]
player1_animation_steps = [10, 8, 1, 7, 7, 3, 7]
player1_sheet =  pygame.image.load("asset/images/player/warrior/Sprites/warrior.png")
player2_size = 250
player2_scale = 3
player2_offset = [112, 107]
player2_data = [player2_size, player2_scale, player2_offset]
player2_animation_steps = [8, 8, 1, 8, 8, 3, 7]
player2_sheet =  pygame.image.load("asset/images/player/wizard/Sprites/wizard.png")

# Background vs Font
BG = pygame.image.load("asset/menu.png")
scaled_BG = pygame.transform.scale(BG, (SCREEN_WIDTH , SCREEN_HEIGHT))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font/font.ttf", size)

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption('BẮP QUYỀN')

# Timer
clock = pygame.time.Clock()
def current_time():
    return pygame.time.get_ticks
pressedKeyTime = 0   
pressedKeys = pygame.key.get_pressed()


# Music and Sound Effect
pygame.mixer.music.load("asset/audio/bgmusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
punchSound = pygame.mixer.Sound("asset/audio/punch.mp3")
punchSound.set_volume(0.1)



# Camera
cameraGroup = CAMERAGROUP()

firstFighter = Fighter(1, 250, 100, False, player1_data, player1_sheet, player1_animation_steps, punchSound, cameraGroup)
secondFighter = Fighter(2, 500, 100, True, player2_data , player2_sheet, player2_animation_steps,punchSound, cameraGroup)


def after_playbutton():
        
        firstFighter.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,secondFighter)
        secondFighter.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,firstFighter)

        firstFighter.draw(screen)
        secondFighter.draw(screen)

        # Receive event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                exit()

            # Smoothen blood descend
            if  pressedKeys[pygame.K_r] or  pressedKeys[pygame.K_t]:
                if current_time() - pressedKeyTime > 500:
                    Fighter.__init__.attacking = False

        current_time()

        cameraGroup.update()
        cameraGroup.setCameraToCenter(firstFighter, secondFighter)        
        
        pygame.display.update()
        clock.tick(60)



def play():
    while True:
        after_playbutton()
        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(35).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 200))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button2(image=None, pos=(500, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH/2, 100))

        PLAY_BUTTON = Button2(image=pygame.image.load("asset/Play Rect.png"), pos=(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-75), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button2(image=pygame.image.load("asset/Options Rect.png"), pos=(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+75), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button2(image=pygame.image.load("asset/Quit Rect.png"), pos=(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+(75*3)), 
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