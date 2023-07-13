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
        self.background = pygame.image.load('asset/images/background/truong.png').convert()
        self.background_rect = self.background.get_rect(topleft = (0,0))

    def center_target_camera(self,target):
        self.offset.x = target.hitbox.centerx - self.half_w
        self.offset.y = target.hitbox.centery - self.half_h

    def custom_draw(self,Fighter):
        self.center_target_camera(Fighter)
        
        #background 
        

        background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background,background_offset)
        #sort
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)