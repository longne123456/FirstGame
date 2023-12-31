# Làm nhân vật
import pygame
from option import Option
SCREEN_WIDTH = Option.WITDH(0)
SCREEN_HEIGHT = Option.HEIGHT(0)

ATTACK_WIDTH = 0
ATTACK_Y = 1
ATTACK_HEIGHT = 0
RED = (255, 0, 0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)


#pygame.Rect((x, y, 80, 180))
class Fighter(pygame.sprite.Sprite):
    def __init__(self, player, x, y, flip, data, player_sheet, player_animation_steps, sound, group):
        super().__init__(group)
        self.player = player
        self.flip = False
        self.hitbox = pygame.Rect((x, y, SCREEN_WIDTH / 25,SCREEN_HEIGHT /6))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.dmg = 0
        self.attack_type = 0
        self.health = 100
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.running = False
        self.alive = True
        self.size = data[0]
        self.player_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(player_sheet, player_animation_steps)
        self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        
        
    
    def load_images(self, player_sheet, player_animation_steps):
        animation_list = []
        for y, animation in enumerate(player_animation_steps):
            temp_images_list = []
        for x in range(animation):
            temp_img = player_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
            temp_images_list.append(pygame.transform.scale(temp_img, (self.size * self.player_scale, self.size * self.player_scale)))
        animation_list.append(temp_images_list)
        return animation_list
    

    # animation
    def move(self, screen_width, screen_height, surface, target):

        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Nhấn phím
        key = pygame.key.get_pressed()

        if self.attacking is False:
            if self.player == 1:
                # Di chuyển
                self.choose = 0
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                # Nhảy
                if key[pygame.K_w] and self.jump is False :
                    self.vel_y = - SCREEN_HEIGHT / 20
                    self.jump = True
            
                if key[pygame.K_r] or key[pygame.K_t]:
                    
                    # Xác định kiểu tấn công nào được sử dụng
                    if key[pygame.K_r]:
                        self.attack(surface, target,1,SCREEN_WIDTH / 6.666666667,SCREEN_HEIGHT/6)
                        self.attack_type = 1
                        self.dmg = 1
                        self.attack_cooldown = 20

                    if key[pygame.K_t]:
                        self.attack(surface, target,1.35,SCREEN_WIDTH/ 5,SCREEN_HEIGHT /12)
                        self.attack_type = 2
                        self.dmg = 3
                        self.attack_cooldown = 100                                           
                    self.attacking = False

            if self.player == 2:
                # Di chuyển
                self.choose = 1
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                # Nhảy
                if key[pygame.K_UP] and self.jump is False :
                    self.vel_y = -SCREEN_HEIGHT /20
                    self.jump = True
                       
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

             
#BACKGROUND 2500x600

        self.vel_y += GRAVITY
        dy += self.vel_y
        #Đảm bảo ng chơi dell ra ngoài
        if self.hitbox.left + dx < 0:
            dx = -self.hitbox.left
        if self.hitbox.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.hitbox.right
        if self.hitbox.bottom + dy > SCREEN_HEIGHT - 70:
            self.vel_y = 0
            self.jump = False
            dy = SCREEN_HEIGHT - 70 - self.hitbox.bottom
        
        

        # Đảm bảo người chơi luôn đối "mặt" với nhau
        if target.hitbox.centerx > self.hitbox.centerx:
            self.flip = False
        else:
            self.flip = True

        # Vị trí nhân vật khi chuyển động
        self.hitbox.x += dx
        self.hitbox.y += dy

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

    def update_animation(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6) #6:death
        elif self.hit == True:
            self.update_action(5) #5:hit
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3) #3:attack1
            elif self.attack_type == 2:
                self.update_action(4) #4:attack2
        elif self.jump == True:
            self.update_action(2) #2:jump
        elif self.running == True:
            self.update_action(1) #1:run
        else:
            self.update_action(0) #0:idle

        animation_cooldown = 50
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # Kiểm tra thời gian animation
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # Kiểm tra animation đã xong chưa
        if self.frame_index >= len(self.animation_list[self.action]):
        # Nếu nhân vật chết thì kết thúc animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                # Kiểm tra kiểu tấn công
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                # Kiểm tra nếu chịu sát thương
                if self.action == 5:
                    self.hit = False
                    # Attack cooldown
                    self.attacking = False
                    self.attack_cooldown = 20

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False) 
        surface.blit(img, (self.hitbox.x - (self.offset[0] * self.player_scale), self.hitbox.y - (self.offset[1] * self.player_scale)))
        