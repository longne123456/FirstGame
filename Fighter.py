# Làm nhân vật
import pygame
ATTACK_WIDTH = 0
ATTACK_Y = 1
ATTACK_HEIGHT = 0

class Fighter():
    def __init__(self, player, x, y, flip, data):
        self.flip = False
        self.hitbox = pygame.Rect((x, y, 80, 180)) # hinh chu nhat nguoi choi
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.dmg = 0
        self.attack_type = 0
        self.health = 100
        self.attack_cooldown =0
        

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Nhấn phím
        key = pygame.key.get_pressed()

        if self.attacking is False:
            # Di chuyển
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # Nhảy
            if key[pygame.K_w] and self.jump is False :
                self.vel_y = -30
                self.jump = True
           
########################################################## TẤN CÔNG #################################################################################################################################################
            
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
                    self.dmg = 30
                    self.attack_cooldown = 20                   
                
                    
                self.attacking = False


             
###########################################################################################################################################################################################################

########################################################## Vật lý ############################################################################################################################################
        self.vel_y += GRAVITY
        dy += self.vel_y





########################################################################################################################################################################################################################################
        # Đảm bảo người chơi ở trên màn hình
        if self.hitbox.left + dx < 0:
            dx = -self.hitbox.left
        if self.hitbox.right + dx > screen_width:
            dx = screen_width - self.hitbox.right
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
            attacking_hitbox = pygame.Rect(self.hitbox.centerx,self.hitbox.y*ATTACK_Y,ATTACK_WIDTH,ATTACK_HEIGHT)
            pygame.draw.rect(surface, (0, 255, 0), attacking_hitbox)
            if attacking_hitbox.colliderect(target.hitbox):
                target.health -= self.dmg
    
    def draw(seft, surface):
        pygame.draw.rect(surface, (255, 0, 0), seft.hitbox)

        
########################################################################################################################################################################################################################################