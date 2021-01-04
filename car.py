import pygame
import sys

#colores
white = (255,255,255)

#deriva de la clase sprite
class car(pygame.sprite.Sprite):
    #constructor, cuando creas un objeto a partir de esta clase, 
    #nos construye el rectangulo y lo imprime
    #esta función se ejecuta
    #self y el fichero donde se encuntra la img, un color, 
    #una anchura, una altura y una velocidad
	def __init__(self, file, color, width, height, speed):
        #inicializa el sprite
		super().__init__()

        #imagen y superficie
        #surface es el espacio k ocupa
		self.image = pygame.Surface([width, height])
        #fondo blanco
		self.image.fill(white)
		self.image.set_colorkey(white)

        #atributos
		self.width = width
		self.height = height
		self.color = color
		self.speed = speed



        #definimos rectangulo con superficie, color, anchura, altura, width y height
		pygame.draw.rect(self.image, self.color, [0,0,self.width, self.height])

        #si se carga imagen
		self.image = pygame.image.load(file)
		self.image = pygame.transform.scale(self.image ,(width, height))

        #definir superficie como rectangulo
		self.rect = self.image.get_rect()

	def moveRight(self,pixels):
		self.rect.x +=pixels
	def moveLeft(self,pixels):
		self.rect.x -=pixels
	def moveUp(self,pixels):
		self.rect.y -=pixels
	def moveDown(self,pixels):
		self.rect.y +=pixels
    
    #mover coche hacia delante y hacia atras
	def moveForward(self,speed):
		self.rect.y += self.speed*speed/20
	def moveBackward(self,speed):
		self.rect.y -= self.speed*speed/20

    #definimos cambio de velocidad, es como un SET en PHP
	def changeSpeed(self, speed):
		self.speed = speed
