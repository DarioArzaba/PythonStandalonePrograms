import sys, os, random, math, getopt, pygame
from pygame.locals import *

def Cargar_Imagen(NombreImagen):
	Direccion_Imagen = os.path.join(os.path.dirname(__file__), 'Images\\' + NombreImagen)
	Imagen = pygame.image.load(Direccion_Imagen)
	if Imagen.get_alpha() is None:
		Imagen = Imagen.convert()
	else:
		Imagen = Imagen.convert_alpha()
	return Imagen, Imagen.get_rect()

class Pelota(pygame.sprite.Sprite):
	def __init__(self, x_y, vector):
		x,y= x_y
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Cargar_Imagen('ball.png')
		Pantalla = pygame.display.get_surface()
		self.area = Pantalla.get_rect()
		self.vector = vector
		self.hit = 0
	def update(self):
		Nueva_Posicion = self.Calcular_Nueva_Posicion(self.rect, self.vector)
		self.rect = Nueva_Posicion
		(angle,z) = self.vector
		if not self.area.contains(Nueva_Posicion):
			tl = not self.area.collidepoint(Nueva_Posicion.topleft)
			tr = not self.area.collidepoint(Nueva_Posicion.topright)
			bl = not self.area.collidepoint(Nueva_Posicion.bottomleft)
			br = not self.area.collidepoint(Nueva_Posicion.bottomright)
			if tr and tl or (br and bl):
				angle = -angle
			if tl and bl:
				#self.offcourt()
				angle = math.pi - angle
			if tr and br:
				angle = math.pi - angle
				#self.offcourt()
		else:
			player1.rect.inflate(-3, -3)
			player2.rect.inflate(-3, -3)
			if self.rect.colliderect(player1.rect) == 1 and not self.hit:
				angle = math.pi - angle
				self.hit = not self.hit
			elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
				angle = math.pi - angle
				self.hit = not self.hit
			elif self.hit:
				self.hit = not self.hit
		self.vector = (angle,z)
	def Calcular_Nueva_Posicion(self, rect, vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)
class Bat(pygame.sprite.Sprite):
	def __init__(self, side):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = Cargar_Imagen('bat.png')
		Pantalla = pygame.display.get_surface()
		self.area = Pantalla.get_rect()
		self.side = side
		self.speed = 10
		self.state = "still"
		self.reinit()
	def reinit(self):
		self.state = "still"
		self.movepos = [0,0]
		if self.side == "left":
			self.rect.midleft = self.area.midleft
		elif self.side == "right":
			self.rect.midright = self.area.midright
	def update(self):
		newpos = self.rect.move(self.movepos)
		if self.area.contains(newpos):
			self.rect = newpos
		pygame.event.pump()
	def moveup(self):
		self.movepos[1] = self.movepos[1] - (self.speed)
		self.state = "moveup"
	def movedown(self):
		self.movepos[1] = self.movepos[1] + (self.speed)
		self.state = "movedown"

def main():
	pygame.init()
	Pantalla = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Basic Pong')
	Fondo = pygame.Surface(Pantalla.get_size())
	Fondo = Fondo.convert()
	Fondo.fill((0, 0, 0))
	global player1
	global player2
	player1 = Bat("left")
	player2 = Bat("right")
	speed = 13
	rand = ((0.1 * (random.randint(5,8))))
	ball = Pelota((0,0),(0.47, speed))
	playersprites = pygame.sprite.RenderPlain((player1, player2))
	ballsprite = pygame.sprite.RenderPlain(ball)
	Pantalla.blit(Fondo, (0, 0))
	pygame.display.flip()
	clock = pygame.time.Clock()

	while 1:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_a:
					player1.moveup()
				if event.key == K_z:
					player1.movedown()
				if event.key == K_UP:
					player2.moveup()
				if event.key == K_DOWN:
					player2.movedown()
			elif event.type == KEYUP:
				if event.key == K_a or event.key == K_z:
					player1.movepos = [0,0]
					player1.state = "still"
				if event.key == K_UP or event.key == K_DOWN:
					player2.movepos = [0,0]
					player2.state = "still"
		Pantalla.blit(Fondo, ball.rect, ball.rect)
		Pantalla.blit(Fondo, player1.rect, player1.rect)
		Pantalla.blit(Fondo, player2.rect, player2.rect)
		ballsprite.update()
		playersprites.update()
		ballsprite.draw(Pantalla)
		playersprites.draw(Pantalla)
		pygame.display.flip()

if __name__ == '__main__': main()