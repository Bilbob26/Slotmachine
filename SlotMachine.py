import pygame
import random

pygame.init()

height_screen = 500
width_screen = 750

win = pygame.display.set_mode((width_screen, height_screen))#make the GUI
pygame.display.set_caption('Slot Machine')#GUI caption
font = pygame.font.SysFont(None, 100)#caption font

banana = pygame.image.load('banana.jpg')#all the fruits
cherry = pygame.image.load('cherry.jpg')
bar = pygame.image.load('bar.jpg')
bigwin = pygame.image.load('bigwin.jpg')
grape = pygame.image.load('grape.jpg')
lemon = pygame.image.load('lemon.jpg')
melon = pygame.image.load('melon.jpg')
orange = pygame.image.load('orange.jpg')
seven = pygame.image.load('seven.jpg')

all_fruits = [banana, bar, cherry, bigwin, grape, lemon, melon, orange, seven]#fruits in an array

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

		self.textSurf, self.textRect = text_objects(self.text, smallText)#text
		self.win = win

	def render(self):
		pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def render_hover(self):
		pygame.draw.rect(win, (200, 0, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def render_click(self):
		pygame.draw.rect(win, (150, 0, 0), (self.x, self.y, self.w, self.h))
		self.render_text()

	def unRender(self):#makes the button dissappear
		pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))

	def render_text(self):#renders the text
		self.textSurf, self.textRect = text_objects(self.text, smallText)
		self.textRect.center = (self.x + self.w/2, self.y + self.h/2)
		self.win.blit(self.textSurf, self.textRect)

	def mouse_actions(self):
		self.mouse = pygame.mouse.get_pos()#gets mouse position
		self.pressed = pygame.mouse.get_pressed()#sees if mouse is pressed

	def click(self):
		self.render()#renders the button
		self.mouse_actions()
		if (self.x < self.mouse[0] < self.x + self.w) and (self.y < self.mouse[1] < self.y + self.h):#checks if the mouse is with the button
			self.render_hover()#hover colour
			if self.pressed[0] == 1:

				if self.y < 300 and self.y > 150:#sees if button is clicked
				
					self.y = self.mouse[1] - self.w/2
					self.render_click()#click colour
				elif self.y <= 150:
					self.y = 151
				elif self.y >= 300:
					self.y = 299




def main():
	startButton.click()#renders the button
	slot1 = random.randint(0, 8)#random number 1
	slot2 = random.randint(0, 8)#2
	slot3 = random.randint(0, 8)#3

	win.blit(all_fruits[0], (100, 150))

startButton = UI(550, 200, 25, 25, '', win)#button to randomise the fruits


run = True
while run:
	win.fill((0, 0, 0))
	#pygame.time.delay(10)

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	main()

	pygame.display.update()

pygame.quit()
