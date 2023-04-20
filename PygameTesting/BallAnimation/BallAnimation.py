#Programa con distintas animaciones (4) de una pelota.

import sys, os, pygame
from pygame.locals import *
pygame.init()

#Clases
class ObjetoJuegoAnimacionDV:
	def __init__(self, image, height, speed):
		self.speed = speed
		self.image = image
		self.pos = image.get_rect().move(0, height)
	def move(self):
		self.pos = self.pos.move(self.speed, 0)
		if self.pos.right > 640: #Cuando llegue el final reiniciar su posicion
			self.pos.left = 0

#Recursos
FondoImagen = os.path.join(os.path.dirname(__file__), 'Images\\bg.jpg')
PelotaImagen = os.path.join(os.path.dirname(__file__), 'Images\\green_ball.png')

def AnimacionPelota():
	LargoPantalla = 640
	AnchoPantalla = 360
	Pantalla = pygame.display.set_mode((LargoPantalla,AnchoPantalla))
	Fondo = pygame.image.load(FondoImagen).convert()
	Fondo = pygame.transform.scale(Fondo, (LargoPantalla, AnchoPantalla))
	Pelota = pygame.image.load(PelotaImagen).convert_alpha()
	pygame.mouse.set_visible(0)
	Velocidad = [3,2] #Cambia la direccion
	PelotaRect = Pelota.get_rect()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		PelotaRect = PelotaRect.move(Velocidad)
		if PelotaRect.left < 0 or PelotaRect.right > LargoPantalla:
			Velocidad[0] = -Velocidad[0]
		if PelotaRect.top < 0 or PelotaRect.bottom > AnchoPantalla:
			Velocidad[1] = -Velocidad[1]
		Pantalla.blit(Fondo,(0,0))
		Pantalla.blit(Pelota,PelotaRect)
		pygame.display.update()
		#Cambia la velocidad
		pygame.time.wait(7)
def AnimacionDistintasVelocidades():
	#Original en "C:\Users\dario\AppData\Local\Programs\Python\Python35\Lib\site-packages\pygame\examples\moveit.py"
	LargoPantalla = 640
	AnchoPantalla = 480
	Pantalla = pygame.display.set_mode((LargoPantalla,AnchoPantalla))
	Fondo = pygame.image.load(FondoImagen).convert()
	Fondo = pygame.transform.scale(Fondo, (LargoPantalla, AnchoPantalla))
	Pelota = pygame.image.load(PelotaImagen).convert_alpha()
	Pantalla.blit(Fondo, (0, 0))
	Objetos = []
	for x in range(6): #Range = Cantidad de pelotas
		UnaPelota = ObjetoJuegoAnimacionDV(Pelota, x*70, x) #Segundo argumento separacion entre pelotas
		Objetos.append(UnaPelota)
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		for UnaPelota in Objetos:
			Pantalla.blit(Fondo, UnaPelota.pos, UnaPelota.pos)
		for UnaPelota in Objetos:
			UnaPelota.move()
			Pantalla.blit(UnaPelota.image, UnaPelota.pos)
		pygame.display.update()
def MoverPelotaMouse():
	Pantalla = pygame.display.set_mode((640,360))
	Fondo = pygame.image.load(FondoImagen).convert()
	Pelota = pygame.image.load(PelotaImagen).convert_alpha()
	pygame.mouse.set_visible(0)

	#Main Loop
	while True:
		#Checar evento de salida
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		screen.blit (Fondo, (0,0))
		x,y = pygame.mouse.get_pos()
		x -= Pelota.get_width()/2
		y -= Pelota.get_height()/2
		screen.blit (Pelota, (x,y))
		pygame.display.update()
def MoverPelotaTeclado():
    Pantalla = pygame.display.set_mode((640,360))
    Fondo = pygame.image.load(FondoImagen).convert()
    Pelota = pygame.image.load(PelotaImagen).convert_alpha()
    x,y = 0,0
    movex, movey = 0,0
    while True:
		#Checar evento de salida
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
		#Si se detecta algun evento cambiar coordenadas (x,y)
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
        Pantalla.blit (Fondo, (0,0))
        Pantalla.blit (Pelota, (x,y))
        pygame.display.update()

#UNCOMMENT TO ACTIVATE ONE OF THE ANIMATIONS

AnimacionPelota()
#AnimacionDistintasVelocidades()
#MoverPelotaMouse()
#MoverPelotaTeclado()

