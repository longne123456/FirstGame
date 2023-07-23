import pygame, sys

RED = (255, 0, 0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Healthbar(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.image.fill((RED))
		self.rect = self.image.get_rect(center = (500,300))
		self.current_health = 200
		self.target_health = 500
		self.max_health = 1000
		self.health_bar_length = 350
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 2

	def get_damage(self,amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health <= 0:
			self.target_health = 0

	def get_health(self,amount):
		if self.target_health < self.max_health:
			self.target_health += amount
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self):
		#self.basic_health()
		self.advanced_health(50,40)
		#self.advanced_health(600,40)
		
		
	def basic_health(self):
		pygame.draw.rect(screen,(RED),(10,10,self.target_health / self.health_ratio,25))
		pygame.draw.rect(screen,(YELLOW),(10,10,self.health_bar_length,25),4)

	def advanced_health(self,x,y):
		transition_width = 0
		transition_color = (RED)

		if self.current_health < self.target_health:
			self.current_health += self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (GREEN)

		if self.current_health > self.target_health:
			self.current_health -= self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (YELLOW)

		health_bar_width = int(self.current_health / self.health_ratio)
		health_bar = pygame.Rect(x,y,health_bar_width,25)
		transition_bar = pygame.Rect(health_bar.right,40,transition_width,25)
		
        
		pygame.draw.rect(screen,(RED),health_bar)
		pygame.draw.rect(screen,transition_color,transition_bar)
		pygame.draw.rect(screen,(WHITE),(x,y,self.health_bar_length,25),4)


healthbar = pygame.sprite.GroupSingle(Healthbar())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				healthbar.sprite.get_damage(100)

	screen.fill((30,30,30))
	healthbar.draw(screen)
	healthbar.update()
	pygame.display.update()
	clock.tick(60)