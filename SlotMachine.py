import pygame
import random

pygame.init()

height_screen = 500
width_screen = 750

win = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption('Slot Machine')
font = pygame.font.SysFont(None, 100)

banana = pygame.image.load('banana.jpg')
cherry = pygame.image.load('cherry.jpg')
bar = pygame.image.load('bar.jpg')
bigwin = pygame.image.load('bigwin.jpg')
grape = pygame.image.load('grape.jpg')
lemon = pygame.image.load('lemon.jpg')
melon = pygame.image.load('melon.jpg')
orange = pygame.image.load('orange.jpg')
seven = pygame.image.load('seven.jpg')

all_fruits = [banana, bar, cherry, bigwin, grape, lemon, melon, orange, seven]

smallText = pygame.font.Font('freesansbold.ttf',20)
largeText = pygame.font.Font('freesansbold.ttf',200)
def text_objects(text, font):
	textSurface = font.render(text, True, (255, 255, 255))
	return textSurface, textSurface.get_rect()


class UI:
	def __init__(self, x, y, w, h, text, win):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		self.text = text

		self.mouse = pygame.mouse.get_pos()
		self.pressed = pygame.mouse.get_pressed()

		self.textSurf, self.textRect = text_objects(self.text, smallText)
		self.win = win

	def render(self):
		pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def render_hover(self):
		pygame.draw.rect(win, (0, 200, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def render_click(self):
		pygame.draw.rect(win, (0, 155, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def unRender(self):
		pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))

	def render_text(self):
		self.textSurf, self.textRect = text_objects(self.text, smallText)
		self.textRect.center = (svdself.x + self.w/2, self.y + self.h/2)
		self.win.blit(self.textSurf, self.textRect)

	def mouse_actions(self):
		self.mouse = pygame.mouse.get_pos()
		self.pressed = pygame.mouse.get_pressed()

	def click(self):
		self.render()
		self.mouse_actions()
		if (self.x < self.mouse[0] < self.x + self.w) and (self.y < self.mouse[1] < self.y + self.h):
			self.render_hover()
			if self.pressed[0] == 1:
				self.render_click()



def main():
	startButton.click()
	slot1 = random.randint(0, 8)
	slot2 = random.randint(0, 8)
	slot3 = random.randint(0, 8)

	#win.blit(win.blit(all_fruits[0], (100, 150)))

startButton = UI(400, 200, 75, 50, 'Click!', win)


run = True
while run:
	win.fill((0, 0, 0))
	pygame.time.delay(60)

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	main()

	pygame.display.update()

pygame.quit()
