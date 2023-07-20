import pygame
from pygame.sprite import AbstractGroup
from Fighter import Fighter

class CAMERAGROUP(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
    
        self.display_surface = pygame.display.get_surface()
        #camera bi be cong
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[0] // 2

        #background
        self.background = pygame.image.load('asset/images/background/truong.png').convert_alpha()
        self.scaled_bg = pygame.transform.scale(self.background, (2500, 650)) 
        self.background_rect = self.scaled_bg.get_rect(topleft = (0,0))

    def center_target_camera(self,target):
        self.offset.x = target.hitbox.centerx - self.half_w
        #self.offset.y = target.hitbox.centery - self.half_h
        if self.offset.x <= 0:
            self.offset.x = 0
        elif self.offset.x >= 1000:
            self.offset.x = 1000

    def centerCamera(self, firstFighter, secondFighter):
        self.offset.x = ((firstFighter.hitbox.centerx - self.half_w) + (secondFighter.hitbox.centerx - self.half_w))/2
        if self.offset.x <= 0:
            self.offset.x = 0
        elif self.offset.x >= 1000:
            self.offset.x = 1000

    
    def custom_draw(self,Fighter1,Fighter2):
        self.centerCamera(Fighter1,Fighter2)
             
        #background 
        background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.scaled_bg,background_offset)

        #sort
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.hitbox.centery):
            offset_pos = sprite.hitbox.topleft - self.offset
            self.display_surface.blit(sprite.scaled_image,offset_pos)

    
