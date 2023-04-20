import sys, os, pygame, time, random
from pygame.locals import *
pygame.init()

#Recursos
FistImage = os.path.join(os.path.dirname(__file__), 'Images\\fist2.png')
ChimpImage = os.path.join(os.path.dirname(__file__), 'Images\\chimp.png')
Sonido_Fallaste_Path = os.path.join(os.path.dirname(__file__), 'Sounds\\whiff.wav')
Sonido_Exito_Path = os.path.join(os.path.dirname(__file__), 'Sounds\\whiff.wav')

#Iniciamos Colores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Pantalla
Pantalla = pygame.display.set_mode((860,300))
pygame.display.set_caption('Chimp Game (by Dario)')
pygame.mouse.set_visible(0)
Fondo = pygame.Surface(Pantalla.get_size())
Fondo = Fondo.convert()
Fondo.fill(white)

#Aqui irian las clases

Fist = pygame.image.load(FistImage).convert_alpha()
Chimp = pygame.image.load(ChimpImage).convert_alpha()
Sonido_Fallaste = pygame.mixer.Sound(Sonido_Fallaste_Path)
Sonido_Exito = pygame.mixer.Sound(Sonido_Exito_Path)

Reloj = pygame.time.Clock()
SpritesTodos = pygame.sprite.RenderPlain((Fist, Chimp))

#Texto
Fuente_Texto = pygame.font.Font(None, 36)
Texto = Fuente_Texto.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
Posicion_Texto = Texto.get_rect(centerx=Pantalla.get_width()/2)

#Convert Alpha Allows transparency
Cursor_Chimp = pygame.image.load(chimp_image).convert_alpha()

while True:
	Reloj.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == MOUSEBUTTONDOWN:
			if fist.punch(chimp):
				Sonido_Exito.play()
				chimp.punched()
			else:
				Sonido_Fallaste.play()
		elif event.type is MOUSEBUTTONUP:
			fist.unpunch()
		allsprites.update()

	Pantalla.blit (Fondo, (0,0))
	Pantalla.blit(Texto, Posicion_Texto)
	x,y = pygame.mouse.get_pos()
	x -= Cursor_Chimp.get_width()/2
	y -= Cursor_Chimp.get_height()/2
	Pantalla.blit (Cursor_Chimp, (x,y))
	allsprites.draw(Pantalla)
	pygame.display.update()
	

