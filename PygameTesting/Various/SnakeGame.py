# Snake game collision test
# USE KEYBOARD ARROWS TO MOVE AND EAT THE APPLES

import sys, os, pygame, random, math
from pygame import *
pygame.init()

#Variables Color
Blanco = (255,255,255)
Negro = (0,0,0)
Verde = (0,155,0)
Rojo = (255,0,0)

#Variables Pantalla
Ancho_Pantalla = 800
Largo_Pantalla = 600
Mensaje_Pantalla = 'Game Title'

#Variables Objetos
Tamano_Jugador = 10
Tamano_Manzana = 30

#FuncionTexto
Tamano_Fuente = 20
Fuente = pygame.font.SysFont("monospace", Tamano_Fuente)
def Poner_Mensaje(Mensaje, Color):
	Texto = Fuente.render(Mensaje,True,Color)
	Pantalla.blit(Texto,[10,30])

#Funcion Objetos
def Serpiente(Tamano_Jugador, Lista_Serpiente):
    for XnY in Lista_Serpiente:
        pygame.draw.rect(Pantalla, Verde, [XnY[0], XnY[1], Tamano_Jugador, Tamano_Jugador])

#Iniciar Pantalla
Pantalla = pygame.display.set_mode((Ancho_Pantalla, Largo_Pantalla))
pygame.display.set_caption(Mensaje_Pantalla)
Reloj = pygame.time.Clock()
FPS = 30

def main():
	Salir_Programa = False
	Salir_Juego = False
	Frente_X = Ancho_Pantalla/2
	Frente_Y = Largo_Pantalla/2
	Cambio_X = 0
	Cambio_Y = 0
	Lista_Serpiente = []
	Tamano_Serpiente = 1
	Manzana_X = round(random.randrange(0, (Ancho_Pantalla-Tamano_Jugador))) #/10.0)*10.0
	Manzana_Y = round(random.randrange(0, (Largo_Pantalla-Tamano_Jugador))) #/10.0)*10.0
	while not Salir_Programa:
		while Salir_Juego == True:
			Pantalla.fill(Blanco)
			Poner_Mensaje("Perdiste. ¿Jugar de nuevo (C) o salir (Q)?",Rojo)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Salir_Juego = False
					Salir_Programa = True
				if event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_q:
						Salir_Juego = False
						Salir_Programa = True
					if event.key == pygame.K_c:
						main()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Salir_Programa = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					Cambio_X = -Tamano_Jugador
					Cambio_Y = 0
				elif event.key == pygame.K_RIGHT:
					Cambio_X = Tamano_Jugador
					Cambio_Y = 0
				elif event.key == pygame.K_UP:
					Cambio_Y = -Tamano_Jugador
					Cambio_X = 0
				elif event.key == pygame.K_DOWN:
					Cambio_Y = Tamano_Jugador
					Cambio_X = 0
		if Frente_X >= Ancho_Pantalla or Frente_X < 0 or Frente_Y >= Largo_Pantalla or Frente_Y < 0: Salir_Juego = True
		Frente_X += Cambio_X
		Frente_Y += Cambio_Y
		Pantalla.fill(Blanco)
		pygame.draw.rect(Pantalla, Rojo, [Manzana_X,Manzana_Y,Tamano_Manzana,Tamano_Manzana])
		if Frente_X >= Manzana_X and Frente_X <= (Manzana_X+Tamano_Manzana):
			if Frente_Y >= Manzana_Y and Frente_Y <= (Manzana_Y+Tamano_Manzana):
				Manzana_X = round(random.randrange(0, (Ancho_Pantalla)-(Tamano_Jugador))) #/10.0)*10.0
				Manzana_Y = round(random.randrange(0, (Largo_Pantalla)-(Tamano_Jugador))) #/10.0)*10.0
				Tamano_Serpiente += 1
		Serpiente_Cabeza = []
		Serpiente_Cabeza.append(Frente_X)
		Serpiente_Cabeza.append(Frente_Y)
		Lista_Serpiente.append(Serpiente_Cabeza)
		Serpiente(Tamano_Jugador,Lista_Serpiente)
		if len(Lista_Serpiente) > Tamano_Serpiente: del Lista_Serpiente[0]
		for Segmento in Lista_Serpiente[:-1]:
			if Segmento == Serpiente_Cabeza: 
				Salir_Juego = True
		Serpiente(Tamano_Jugador,Lista_Serpiente)
		pygame.display.update()
		Reloj.tick(FPS)
	pygame.quit()
	quit()
	raise SystemExit

main()

