import sys, os, pygame, time, random
from pygame.locals import *
pygame.init()

#FIX COLISION RACEGAME LOGIC!
#FIX PROGRAMS MENU

#Resources
bif = os.path.join(os.path.dirname(__file__), 'Images\\bg.jpg')
mif = os.path.join(os.path.dirname(__file__), 'Images\\green_ball.png')
fist = os.path.join(os.path.dirname(__file__), 'Images\\fist.bmp')
whiff = os.path.join(os.path.dirname(__file__), 'Sounds\\whiff.wav')
punch = os.path.join(os.path.dirname(__file__), 'Sounds\\punch.ogg')
chimp_img = os.path.join(os.path.dirname(__file__), 'Images\\chimp.bmp')

#Funciones Basicas
def Menu():
	menuDisplay = pygame.display.set_mode((800,600))
	black = (0,0,0)
	white = (255,255,255)
	green = (0,200,0)
	menuDisplay.fill(black)
	TextSurf = pygame.font.Font('freesansbold.ttf',115).render("Menu",True,white)
	TextRect = TextSurf.get_rect()
	TextRect.center = (400,300) #Posicion del texto
	menuDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	clock = pygame.time.Clock()
	clock.tick(15)
	menu_start = True
	while menu_start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

#Programas
def MoveBallMouse():
    screen = pygame.display.set_mode((640,360),0,32)
    background = pygame.image.load(bif).convert()
    mouse_c = pygame.image.load(mif).convert_alpha()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit (background, (0,0))
        x,y = pygame.mouse.get_pos()
        x -= mouse_c.get_width()/2
        y -= mouse_c.get_height()/2
        screen.blit (mouse_c, (x,y))
        #Repetir el Ciclo
        pygame.display.update()
def MoveBallKeyBoard():
    screen = pygame.display.set_mode((640,360),0,32)
    background = pygame.image.load(bif).convert()
    mouse_c = pygame.image.load(mif).convert_alpha()
    x,y = 0,0
    movex, movey = 0,0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    movex=-1
                elif event.key==K_RIGHT:
                    movex=+1
                elif event.key==K_UP:
                    movey=-1
                elif event.key==K_DOWN:
                    movey=+1
            if event.type == KEYUP:
                if event.key==K_LEFT:
                    movex=0
                elif event.key==K_RIGHT:
                    movex=0
                elif event.key==K_UP:
                    movey=0
                elif event.key==K_DOWN:
                    movey=0

        x+=movex
        y+=movey
        screen.blit (background, (0,0))
        screen.blit (mouse_c, (x,y))
        pygame.display.update()
def Dibujo():
	white = (255,255,255)
	black = (0,0,0)
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	gameDisplay = pygame.display.set_mode((800,600))
	gameDisplay.fill(black)
	pixAr = pygame.PixelArray(gameDisplay)
	pixAr[250][220] = green
	pixAr[260][230]= blue
	pixAr[270][240]= white
	pixAr[280][250]= red
	pygame.draw.line(gameDisplay,blue,(100,200),(300,450),3)
	pygame.draw.rect(gameDisplay,red,(400,400,50,30))
	pygame.draw.circle(gameDisplay,white,(370,150),50)
	pygame.draw.polygon(gameDisplay,green,((500,50),(520,50),(540,80),(490,70),(495,60)))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.display.update()
def RaceGame():
	#Display Start
	display_width = 800
	display_height = 600
	gameDisplay = pygame.display.set_mode((display_width,display_height)) 
	pygame.display.set_caption('A bit Racey')
	clock = pygame.time.Clock()

	#Constant Definitions
	black = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	block_color = (53,115,255)
	car_width = 40
	car_height = 79

	#Resource Load
	carImg_dir = os.path.join(os.path.dirname(__file__), 'Images\\Taxi.png')
	carImg = pygame.image.load(carImg_dir)
	carImg = pygame.transform.scale(carImg,(car_width, car_height))

	#Functions
	def things_dodged(count):
		font = pygame.font.SysFont(None,25)
		text = font.render("Points: "+str(count),True,black)
		gameDisplay.blit(text,(0,0))
	def things(thingx, thingy, thingw, thingh, color):
		#Obstaculos
		pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
	def car(x,y):
		#Dibujar el coche
		gameDisplay.blit(carImg,(x,y))
	def text_objects(text,font):
		textSurface = font.render(text,True,black)
		return textSurface, textSurface.get_rect()
	def message_display(text):
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects(text,largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)
		pygame.display.update()
		time.sleep(2)
		game_loop()
	def crash():
		#
		message_display('Game Over!')
	
	def game_loop():
		x = (display_width * 0.45) #Posicion del Sprite
		y = (display_height * 0.8)
		x_change = 0
		thing_startx = random.randrange(0,display_width)
		thing_starty = -500
		thing_speed = 7
		thing_width = 100
		thing_height = 100
		dodged = 0
		gameExit = False
		while not gameExit: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x_change = -5
					elif event.key == pygame.K_RIGHT:
						x_change = 5
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						x_change = 0
					elif event.key == pygame.K_RIGHT:
						x_change = 0

			x += x_change

			gameDisplay.fill(white)
			
			things(thing_startx,thing_starty,thing_width,thing_height,block_color)
			thing_starty += thing_speed
			car(x,y)
			things_dodged(dodged)
			
			if x > (display_width-car_width)  or x < 0:
				crash()
			if thing_starty > (display_height):
				thing_starty = 0 - thing_height
				thing_startx = random.randrange(0,display_width)
				dodged += 1
				thing_speed += .1

			if y <thing_starty+thing_height:
				if x > thing_startx and x < (thing_startx+thing_width) or (x+car_width) > thing_startx and (x+car_width) < (thing_startx+thing_width):
					crash()

			pygame.display.update()
			clock.tick(60)
	game_loop()
	pygame.quit()
	sys.exit()

#MoveBallMouse()
#MoveBallKeyBoard()
Dibujo()
#ChimpGame() TODO!
#RaceGame()
#Menu()