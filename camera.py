import pygame
from option import Option

SCREEN_WIDTH = Option.WITDH(0)
SCREEN_HEIGHT = Option.HEIGHT(0)

class CAMERAGROUP(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        #camera bị bẻ cong
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[0] // 2

        #background
        self.background = pygame.image.load('asset/images/background/truong.png').convert_alpha()
        self.scaled_bg = pygame.transform.scale(self.background, (2500, 650)) 
        self.background_rect = self.scaled_bg.get_rect(topleft = (0,0))
  
    def centerCamera(self, firstFighter, secondFighter):
        self.offset.x = ((firstFighter.hitbox.centerx - self.half_width) + (secondFighter.hitbox.centerx - self.half_width))/2

    def Camerabeh(self,Fighter1,Fighter2):
        if(Fighter1.centerx <= SCREEN_WIDTH/15 & Fighter2.centerx <= SCREEN_WIDTH/15):
            self.offset.x -= SCREEN_WIDTH/15
        if(Fighter1.centerx >= SCREEN_WIDTH - SCREEN_WIDTH/15 & Fighter2.centerx <= SCREEN_WIDTH - SCREEN_WIDTH/15 ):
            self.offset.x += SCREEN_WIDTH/15
        if(Fighter1.centerx < SCREEN_HEIGHT -10  & Fighter2.center < SCREEN_HEIGHT -10 ):
            self.offset.y -= SCREEN_HEIGHT/10
            
        
    def setCameraToCenter(self,Fighter1,Fighter2):
        #background 
        self.centerCamera(Fighter1,Fighter2)
        background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.scaled_bg,background_offset)

        #sort
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.hitbox.centery):
            offset_pos = sprite.hitbox.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
            