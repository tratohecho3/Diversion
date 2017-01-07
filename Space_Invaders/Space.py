import pygame,sys
from pygame.locals import *
from random import randint
from Clases import Nave
from Clases import Invasor as Enemigo 

ancho = 900
alto = 480
listaEnemigo = []

def detenerTodo():
	for enemigo in listaEnemigo:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)

		enemigo.conquista = True

def cargarEnemigos():
	enemigo = Enemigo(100,100,50,"Imagenes/marciano.jpg","Imagenes/MarcianoB.jpg")
	listaEnemigo.append(enemigo)

	enemigo2 = Enemigo(300,100,50,"Imagenes/marciano.jpg","Imagenes/MarcianoB.jpg")
	listaEnemigo.append(enemigo2)

	enemigo3 = Enemigo(500,100,50,"Imagenes/marciano.jpg","Imagenes/MarcianoB.jpg")
	listaEnemigo.append(enemigo3)

	enemigo4 = Enemigo(700,100,50,"Imagenes/marciano.jpg","Imagenes/MarcianoB.jpg")
	listaEnemigo.append(enemigo4)

def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invaders")
	ImagenFondo = pygame.image.load("Imagenes/Fondo.jpg")
	enJuego = True
	jugador = Nave.naveEspacial(ancho,alto)
	reloj = pygame.time.Clock()
	cargarEnemigos()

	pygame.mixer.music.load('Imagenes/fondo.mp3')
	pygame.mixer.music.play(3)

	fuente = pygame.font.SysFont("Arial", 30)
	Texto = fuente.render("Game Over",0,(120,100,40))
	Texto2 = fuente.render("Has Ganado",0,(120,100,40))
	enJuego = True

	while True:
		#jugador.movimiento()
		reloj.tick(60)
		tiempo = pygame.time.get_ticks()/1000
		for evento in pygame.event.get():
			if evento.type == QUIT:
					pygame.quit()
					sys.exit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT:
						jugador.movimientoIzquierda()
					elif evento.key == K_RIGHT:
						jugador.movimientoDerecha()

					elif evento.key == K_SPACE:
						x = jugador.rect.centerx -5
						y = jugador.rect.centery -20
						jugador.disparar(x,y)
							 
		ventana.blit(ImagenFondo, (0,0))
		
		
		jugador.dibujar(ventana)
	

		if len(jugador.listaDisparo) > 0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()

				if x.rect.top < 10:
					jugador.listaDisparo.remove(x)

				else:
					for enemigo in listaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigo.remove(enemigo)
							jugador.listaDisparo.remove(x)


		if len(listaEnemigo) > 0:
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(ventana)
				if enemigo.rect.colliderect(jugador.rect):
					jugador.destruccion()
					enJuego = False
					detenerTodo()
				if len(enemigo.listaDisparo) > 0:
					for x in enemigo.listaDisparo:
						x.dibujar(ventana)
						x.trayectoria()
						if x.rect.colliderect(jugador.rect):
							jugador.destruccion()
							enJuego = False
							detenerTodo()
						if x.rect.top > 900:
						
							enemigo.listaDisparo.remove(x)
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
									enemigo.listaDisparo.remove(x)
		if len(listaEnemigo) == 0:
			ventana.blit(Texto2,(300,300))
			detenerTodo()
			pygame.mixer.fadeout(3000)
			jugador.velocidad = 0
			jugador.listaDisparo= []
		

		if enJuego == False:
			pygame.mixer.fadeout(3000)
			ventana.blit(Texto,(300,300))
									
		pygame.display.update()


SpaceInvader()