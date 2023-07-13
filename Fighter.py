# Làm nhân vật
import pygame


class Fighter():
    def __init__(self, player, x, y, flip, data):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100


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
            # Tấn công
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
                # Xác định kiểu tấn công nào được sử dụng
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2
                self.attacking = False
             

        # Thực hiện trọng lực
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Đảm bảo người chơi ở trên màn hình
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 70:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 70 - self.rect.bottom

        # Đảm bảo người chơi luôn đối "mặt" với nhau
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # Vị trí nhân vật khi chuyển động
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True

        attacking_rect = pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip), self.rect.y, 2*self.rect.width, self.rect.height)  # noqa: E501
        if attacking_rect.colliderect(target.rect):
            target.health -= 2
        
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)


    def draw(seft, surface):
        pygame.draw.rect(surface, (255, 0, 0), seft.rect)
