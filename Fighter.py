# Làm nhân vật
import pygame


ATTACK_WIDTH = 0
ATTACK_Y = 1
ATTACK_HEIGHT = 0

#pygame.Rect((x, y, 80, 180))
class Fighter(pygame.sprite.Sprite):
    def __init__(self, player, x, y, flip, data, sound, group):
        super().__init__(group)
        self.player = player
        self.flip = False
        self.hitbox = pygame.Rect((x, y, 40, 100))
        self.image = pygame.image.load("asset/images/player/KhoaNgo.png").convert_alpha()
        self.scaled_image = pygame.transform.scale(self.image, (80, 100))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.dmg = 0
        self.attack_type = 0
        self.health = 100
        self.attack_cooldown =0
        self.attack_sound = sound
        

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Nhấn phím
        key = pygame.key.get_pressed()

        if self.attacking is False:
########################################################## player 1 dk ##########################################################

            if self.player == 1:


                # Di chuyển
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]:
                    dx = SPEED
                # Nhảy
                if key[pygame.K_w] and self.jump is False :
                    self.vel_y = -30
                    self.jump = True
           
########################################################## TẤN CÔNG 1 ##############################################################
            
                if key[pygame.K_r] or key[pygame.K_t]:
                    
                    # Xác định kiểu tấn công nào được sử dụng
                    if key[pygame.K_r]:
                        self.attack(surface, target,1,150,100)
                        self.attack_type = 1
                        self.dmg = 1
                        self.attack_cooldown = 20

                    if key[pygame.K_t]:
                        self.attack(surface, target,1.35,200,50)
                        self.attack_type = 2
                        self.dmg = 3
                        self.attack_cooldown = 100                   
                    
                        
                    self.attacking = False
########################################################## player 2 dk ##########################################################

            if self.player == 2:
                # Di chuyển
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                # Nhảy
                if key[pygame.K_UP] and self.jump is False :
                    self.vel_y = -30
                    self.jump = True
           
########################################################## TẤN CÔNG 2 ##############################################################
            
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    
                    # Xác định kiểu tấn công nào được sử dụng
                    if key[pygame.K_KP1]:
                        self.attack(surface, target,1,150,100)
                        self.attack_type = 1
                        self.dmg = 1
                        self.attack_cooldown = 20

                    if key[pygame.K_KP2]:
                        self.attack(surface, target,1.35,200,50)
                        self.attack_type = 2
                        self.dmg = 3
                        self.attack_cooldown = 100                   
                    
                        
                    self.attacking = False

             
####################################################################################################################################################
#BACKGROUND 2000x600
########################################################## Vật lý ############################################################################################################################################
        self.vel_y += GRAVITY
        dy += self.vel_y



########################################################################################################################################################################################################################################
        # Đảm bảo người chơi ở trên màn hình
        if self.hitbox.left + dx < 0:
            dx = -self.hitbox.left
        if self.hitbox.right + dx > 2000:
            dx = 2000 - self.hitbox.right
        if self.hitbox.bottom + dy > screen_height - 70:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 70 - self.hitbox.bottom
        
        

        # Đảm bảo người chơi luôn đối "mặt" với nhau
        if target.hitbox.centerx > self.hitbox.centerx:
            self.flip = False
        else:
            self.flip = True

        # Vị trí nhân vật khi chuyển động
        self.hitbox.x += dx
        self.hitbox.y += dy
########################################################################################################################################################################################################################################
        # attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 2
    
    def attack(self, surface, target,ATTACK_Y,ATTACK_WIDTH,ATTACK_HEIGHT):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_sound.play()
            attacking_hitbox = pygame.Rect(self.hitbox.centerx,self.hitbox.y*ATTACK_Y,ATTACK_WIDTH,ATTACK_HEIGHT)
            pygame.draw.rect(surface, (0, 255, 0), attacking_hitbox)
            if attacking_hitbox.colliderect(target.hitbox):
                target.health -= self.dmg
    
    def draw(seft, surface):
        pygame.draw.rect(surface, (255, 0, 0), seft.hitbox)

        
########################################################################################################################################################################################################################################