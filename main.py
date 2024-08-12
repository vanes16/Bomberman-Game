import pygame
from pygame.locals import *
from datetime import datetime, timedelta

pygame.init()
#pygame.mixer.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bomberman Project')

tile_size = 40

bomb_img = pygame.image.load('bomb.png')
pillar_img = pygame.image.load('1.png')
block_img = pygame.image.load('block.png')
brick_img = pygame.image.load('0.png')
exp_img = pygame.image.load('explotion.png')
explou_img = pygame.image.load('explou.png')
explol_img = pygame.image.load('explol.png')
explod_img = pygame.image.load('explod.png')
explor_img = pygame.image.load('explor.png')

#gameSound = pygame.mixer.Sound('sounds/multiplayer.wav')

def draw_grid():
	for line in range(0, 15):
		pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, screen_height))

class World():
	def __init__(self, data):
		self.tile_list = []

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(pillar_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(block_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(brick_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size 
					img_rect.y = row_count * tile_size 
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])


world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,3,3,3,3,3,3,3,3,3,0,0,1],
[1,0,2,3,2,3,2,3,2,3,2,3,2,0,1],
[1,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
[1,3,2,3,2,3,2,3,2,3,2,3,2,3,1],
[1,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
[1,3,2,3,2,3,2,0,2,3,2,3,2,3,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,3,2,3,2,3,2,0,2,3,2,3,2,3,1],
[1,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
[1,3,2,3,2,3,2,3,2,3,2,3,2,3,1],
[1,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
[1,0,2,3,2,3,2,3,2,3,2,3,2,0,1],
[1,0,0,3,3,3,3,3,3,3,3,3,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Player():
	def __init__(self, world):
		img = pygame.image.load('player1r.png')
		self.image = pygame.transform.scale(img,[40,40])
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.x = 40
		self.rect.y = 520
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.direction = self.image


	def update(self,direction):
		x = 0
		y = 0
		if direction == "KARAKTER":
			self.direction
		if direction == "RIGHT":
			x += 40
			self.image = pygame.image.load('player1r.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "LEFT":
			x -= 40
			self.image = pygame.image.load('player1l.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "UP":
			y -= 40
			self.image = pygame.image.load('player1u.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "DOWN":
			y += 40
			self.image = pygame.image.load('player1d.png')
			self.image.set_colorkey((255, 255, 255))

		for tile in world.tile_list:
			if tile[1].colliderect(self.rect.x +x, self.rect.y, self.width,self.height):
				x = 0
			if tile[1].colliderect(self.rect.x, self.rect.y + y, self.width, self.height):
				y = 0


		self.rect.x += x
		self.rect.y += y

		screen.blit(self.image, self.rect)
    

class Player2():
	def __init__(self, world):
		img = pygame.image.load('player2l.png')
		self.image = pygame.transform.scale(img,[40,40])
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.x = 520
		self.rect.y = 40
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.direction = self.image


	def update(self,direction):
		x = 0
		y = 0
		if direction == "KARAKTER":
			self.direction
		if direction == "RIGHT":
			x += 40
			self.image = pygame.image.load('player2r.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "LEFT":
			x -= 40
			self.image = pygame.image.load('player2l.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "UP":
			y -= 40
			self.image = pygame.image.load('player2u.png')
			self.image.set_colorkey((255, 255, 255))
		if direction == "DOWN":
			y += 40
			self.image = pygame.image.load('player2d.png')
			self.image.set_colorkey((255, 255, 255))

		for tile in world.tile_list:
			if tile[1].colliderect(self.rect.x +x, self.rect.y, self.width,self.height):
				x = 0
			if tile[1].colliderect(self.rect.x, self.rect.y + y, self.width, self.height):
				y = 0


		self.rect.x += x
		self.rect.y += y

		screen.blit(self.image, self.rect)

class Bomb():
	def __init__(self, world, player1 , player2):
		self.image = pygame.transform.scale(bomb_img,[40,40])
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.x = 1000
		self.rect.y = 1000
		self.case_x = 255
		self.case_y = 255
		self.world = world
		self.player1 = player1
		self.player2 = player2
		self.time_created = datetime.now()
		self.bomb = self.image
		self.explotion = 0 
	
	def update(self,x,y,bomb):
		if bomb == "MOVE":
			self.rect.x = x
			self.rect.y = y
			self.image = pygame.transform.scale(bomb_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.time_created = datetime.now()

		screen.blit(self.image,self.rect)

	def meledak(self):
		if timedelta(seconds=3) < datetime.now() -self.time_created:
			self.image = pygame.transform.scale(exp_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.explotion = 1

			for tile in world.tile_list:
				if self.rect.y - tile_size :
					if tile == 3:
						tile == 1
				if self.rect.y + tile_size :
					if tile  == 3:
						tile == 1

			if self.player1.rect.x == self.rect.x and self.rect.y - tile_size <= self.player1.rect.y <= self.rect.y + tile_size:
				return 1
			if self.rect.x - tile_size <= self.player1.rect.x <= self.rect.x + tile_size and self.rect.y == self.player1.rect.y:
				return 1
			if self.player2.rect.x == self.rect.x and self.rect.y - tile_size <= self.player2.rect.y <= self.rect.y + tile_size:
				return 2
			if self.rect.x - tile_size <= self.player2.rect.x <= self.rect.x + tile_size and self.rect.y == self.player2.rect.y:
				return 2

		if timedelta(seconds=3.5) < datetime.now()-self.time_created:
			self.image = pygame.transform.scale(bomb_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.rect.x = 1000 
			self.rect.y = 1000
			self.explotion= 0
class Bomb2():
	def __init__(self, world, player1 , player2):
		self.image = pygame.transform.scale(bomb_img,[40,40])
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.x = 1000
		self.rect.y = 1000
		self.case_x = 255
		self.case_y = 255
		self.world = world
		self.player1 = player1
		self.player2 = player2
		self.time_created = datetime.now()
		self.bomb2 = self.image
		self.explotion = 0 
	
	def update(self,x,y,bomb2):
		if bomb2 == "MOVE":
			self.rect.x = x
			self.rect.y = y
			self.image = pygame.transform.scale(bomb_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.time_created = datetime.now()

		screen.blit(self.image,self.rect)

	def meledak(self):
		if timedelta(seconds=3) < datetime.now() -self.time_created:
			self.image = pygame.transform.scale(exp_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.explotion = 1

			for tile in world.tile_list:
				if self.rect.y - tile_size :
					if tile == 3:
						tile == 1
				if self.rect.y + tile_size :
					if tile  == 3:
						tile == 1

			if self.player1.rect.x == self.rect.x and self.rect.y - tile_size <= self.player1.rect.y <= self.rect.y + tile_size:
				return 1
			if self.rect.x - tile_size <= self.player1.rect.x <= self.rect.x + tile_size and self.rect.y == self.player1.rect.y:
				return 1
			if self.player2.rect.x == self.rect.x and self.rect.y - tile_size <= self.player2.rect.y <= self.rect.y + tile_size:
				return 2
			if self.rect.x - tile_size <= self.player2.rect.x <= self.rect.x + tile_size and self.rect.y == self.player2.rect.y:
				return 2

		if timedelta(seconds=3.5) < datetime.now()-self.time_created:
			self.image = pygame.transform.scale(bomb_img,[40,40])
			self.image.set_colorkey((255, 255, 255))
			self.rect.x = 1000 
			self.rect.y = 1000
			self.explotion= 0
class Flame():
	def __init__(self, flame_d, flame_u, flame_l, flame_r):
		self.flame_d = pygame.transform.scale(explod_img,[40,40])
		self.flame_d.set_colorkey((255, 255, 255))
		self.flame_u = pygame.transform.scale(explou_img,[40,40])
		self.flame_u.set_colorkey((255, 255, 255))
		self.flame_l = pygame.transform.scale(explol_img,[40,40])
		self.flame_l.set_colorkey((255, 255, 255))
		self.flame_r = pygame.transform.scale(explor_img,[40,40])
		self.flame_r.set_colorkey((255, 255, 255))


world = World(world_data)
player = Player(world)
player2 = Player2(world)
bomb = Bomb(world,player,player2)
flame = Flame(explod_img,explou_img,explol_img,explor_img)
bomb2 = Bomb2(world,player,player2)

run = True
while run:

	screen.fill((240,248,255))
	player.update("KARAKTER")
	world.draw()
	draw_grid()
	player2.update("KARAKTER")

	bomb.update(1000,1000,bomb_img)
	bomb.meledak()
	bomb2.update(1000,1000,bomb_img)
	bomb2.meledak()

	#gameSound.play(-1)

	if bomb.explotion == 1:
		screen.blit(flame.flame_d, (bomb.rect.x, bomb.rect.y + tile_size))
		screen.blit(flame.flame_u, (bomb.rect.x, bomb.rect.y - tile_size))
		screen.blit(flame.flame_l, (bomb.rect.x - tile_size, bomb.rect.y))
		screen.blit(flame.flame_r, (bomb.rect.x + tile_size, bomb.rect.y))

	if bomb2.explotion == 1:
		screen.blit(flame.flame_d, (bomb2.rect.x, bomb2.rect.y + tile_size))
		screen.blit(flame.flame_u, (bomb2.rect.x, bomb2.rect.y - tile_size))
		screen.blit(flame.flame_l, (bomb2.rect.x - tile_size, bomb2.rect.y))
		screen.blit(flame.flame_r, (bomb2.rect.x + tile_size, bomb2.rect.y))
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				player.update("RIGHT")
			if event.key == K_LEFT:
				player.update("LEFT")
			if event.key == K_UP:
				player.update("UP")
			if event.key == K_DOWN:
				player.update("DOWN")
			if event.key == K_SPACE:
				bomb.update(player.rect.x,player.rect.y,"MOVE")


			if event.key == K_d:
				player2.update("RIGHT")
			if event.key == K_a:
				player2.update("LEFT")
			if event.key == K_w:
				player2.update("UP")
			if event.key == K_s:
				player2.update("DOWN")
			if event.key == K_LCTRL:
				bomb2.update(player2.rect.x,player2.rect.y,"MOVE")

	pygame.display.update()
	game_over = bomb.meledak()
	game_over2 = bomb2.meledak()

	if game_over == 1:
		print("Black Player Win")
		run = False
	if game_over == 2:
		print("White Player Win")
		run = False
	if game_over2 == 1:
		print("Black Player Win")
		run = False
	if game_over2 == 2:
		print("White Player Win")
		run = False
pygame.quit()