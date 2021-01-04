import pygame
import sys
#para hacer k las speed de los coches sea random
import random
#sublibreria para que cargue las funciones y no todo el código
from pygame.locals import *

pygame.init()

def main():

	#esto es que creamos una clase llamada car
	from car import car
	#para poder usarla funcion timepara el sleep
	import time

	#tamaño de la pantalla
	screenwidth=800
	screenheight=600
	#colores
	green = (0,205,0)
	black = (20,20,20)
	grey=(135,135,135)
	grey2 = (145,145,145)
	white = (255,255,255)
	red = (255,0,0)
	#velocidad inical del playerCar
	speed=1
	score=0



	#definimos tupla, son constantes de dos coordenadas
	size=(screenwidth, screenheight)
	#creamos la agrupación de los sprites
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Cars racing")

	#te da todas las fuentes
	fonts = pygame.font.get_fonts()
	#print(fonts)
	fonts = pygame.font.SysFont('Arial',30)
	font_score = pygame.font.SysFont('Arial',20)


	#music
	pygame.mixer.music.load('audio/soundtrack.mp3')
	pygame.mixer.music.play (-1)

	#Jugadores = color, anchura, altura, speed
	playerCar=car('images/alonso.png',red, 170,150, 70)
	#obtenemos la coordenada x del rectangulo
	playerCar.rect.x=150-playerCar.image.get_width()/2
	playerCar.rect.y=screenheight-100

	all_sprites_list=pygame.sprite.Group()

	car1=car('images/español.png',black, 170,150,70)
	car1.rect.x=250-playerCar.image.get_width()/2
	car1.rect.y=screenheight-100

	car2=car('images/amarillo.png',red, 170,150,random.randint(50,100))
	car2.rect.x=350-playerCar.image.get_width()/2
	car2.rect.y=screenheight-600

	car3=car('images/japo.png',red, 170,150,random.randint(50,100))
	car3.rect.x=150-playerCar.image.get_width()/2
	car3.rect.y=screenheight-1020

	car4=car('images/andorra.png',red, 170,150,random.randint(50,100))
	car4.rect.x=450-playerCar.image.get_width()/2
	car4.rect.y=screenheight-900

	car5=car('images/schumacher.png',red, 170,150,random.randint(50,100))
	car5.rect.x=550-playerCar.image.get_width()/2
	car5.rect.y=screenheight-600

	#cargamos el coche roto
	breakcar = car('images/cocheestrellado.png', red, 170,150,random.randint(50,100))
	breakcar.rect.x=600
	breakcar.rect.y=-600

	#creamos lista con todos los sprites
	all_sprites_list.add(playerCar)
	all_sprites_list.add(car1)
	all_sprites_list.add(car2)
	all_sprites_list.add(car3)
	all_sprites_list.add(car4)
	all_sprites_list.add(car5)
	all_sprites_list.add(breakcar)



	#declaramos la variable game over y finished
	gameover=False
	finished = False

	#agrupamineot de coahes que llegan
	all_coming_cars=pygame.sprite.Group()
	all_coming_cars.add(car1,car2,car3,car4,car5)

	#definir reloj
	clock=pygame.time.Clock()
	
	while not finished:
		while not gameover:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					finished=True

		    #velocidad de juego con las flechas
			keys=pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				if playerCar.rect.x > 60:
					playerCar.moveLeft(5)
			if keys[pygame.K_RIGHT]:
				if playerCar.rect.x < 500:
					playerCar.moveRight(5)   
			if keys[pygame.K_UP]:
				if playerCar.rect.y > 0:
					#speed +=0.05
					playerCar.moveUp(5)    
			if keys[pygame.K_DOWN]:
				if playerCar.rect.y < 500:
					#speed -=0.05 
					playerCar.moveDown(5)  

		    #movimiento de coche


		    #logica del juego
			for car in all_coming_cars:
				car.moveForward(speed)
				if car.rect.y>screenheight:
					car.changeSpeed(random.randint(50,100))
					car.rect.y=-200
					# car.repaint(random.choice(lista_colores))
		    #lista de colisiones 
			car_collision_list= pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
			for car in car_collision_list:
				#breakcar = pygame.image.load('images/cocheestrellado.png')
				'''breakcar.rect.x=playerCar.rect.x
				breakcar.rect.y=playerCar.rect.y
				#textos
				text=fonts.render("GAME OVER / FIN DEL JUEGO", True, red)
				screen.blit(text, (250, 250))
				pygame.display.flip()'''
			#audio explosion
			#añadimos el sonido para el choque con algun coche
				effect = pygame.mixer.Sound('audio/crash.wav')
				effect.play(1)
				breakcar.rect.x=playerCar.rect.x
				breakcar.rect.y=playerCar.rect.y
				time.sleep(3)
				


				all_sprites_list.update()
				
				
				gameover=True
			screen.fill(grey2)
		    #dibujar carretera
			pygame.draw.rect(screen,black,[100,0,500, screenheight])
		    #punto inicial, punto final y grosor
			pygame.draw.line(screen,white,[200,0],[200,screenheight],5)
			pygame.draw.line(screen,white,[300,0],[300,screenheight],5)
			pygame.draw.line(screen,white,[400,0],[400,screenheight],5)
			pygame.draw.line(screen,white,[500,0],[500,screenheight],5)

		    #dibujar sprites
			all_sprites_list.draw(screen)

			text = fonts.render("Cars racing",True,black)
			screen.blit(text, (screenwidth-text.get_width()-10,30))
			text_score=font_score.render("Score: "+str(score),True,black)
			screen.blit(text_score,(screenwidth-text_score.get_width()-10,60))
			score +=1
			pygame.display.flip()
			
			clock.tick(60)


			
 			


		#textos
		#text=fonts.render("GAME OVER / FIN DEL JUEGO", True, red)
		text=fonts.render("Pulsa Y para reintentar o N para cerrar", True, red)
		screen.blit(text, (250, 250))
		pygame.display.flip()
		#print("Parece que tu no eres Fernando Alonso, eres demasiado malo.")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished=True
			keys=pygame.key.get_pressed()
			if keys[pygame.K_y]:

				main()

			elif keys[pygame.K_n]:

					finished=True

	pygame.quit()  

main()