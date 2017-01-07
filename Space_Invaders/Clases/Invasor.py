import pygame
from random import randint
import Proyectil

class Invasor(pygame.sprite.Sprite):
	def __init__(self,posx,posy,distancia,ImagenUno,ImagenDos):
		pygame.sprite.Sprite.__init__(self)

		self.imagenA = pygame.image.load(ImagenUno)
		self.imagenB = pygame.image.load(ImagenDos)
		self.listaImagenes = [self.imagenA,self.imagenB]
		self.posImagen = 0
		self.imagenInvasor = self.listaImagenes[self.posImagen]
		self.rect = self.imagenInvasor.get_rect()
		self.listaDisparo = []
		self.rect.top = posy
		self.rect.left = posx
		self.velocidad = 5
		self.rangoDisparo = 5
		self.conquista = False
		self.tiempoCambio = 1
		self.derecha = True
		self.contador = 0
		self.Maxdescenso = self.rect.top + 40

		self.limiteDerecha = posx + distancia
		self.limiteIzquierda = posx - distancia

	def comportamiento(self,tiempo):
		if self.conquista == False:

			self.movimientos()
			self.ataque()
			if self.tiempoCambio == tiempo:
				self.posImagen += 1
				self.tiempoCambio += 1

				if self.posImagen > len(self.listaImagenes) - 1:
					self.posImagen = 0



	def dibujar(self,superficie):
		self.imagenInvasor = self.listaImagenes[self.posImagen]
		superficie.blit(self.imagenInvasor, self.rect)

	def ataque(self):
		if (randint(0,100) < self.rangoDisparo):
			self.__disparo()

	def __disparo(self):
		x,y = self.rect.center
		miProyectil = Proyectil.Proyectil(x,y,"Imagenes/disparob.jpg",False)
		self.listaDisparo.append(miProyectil)

	def movimientos(self):
		if self.contador < 3:
			self.movimientoLateral()
		else:
			self.descenso()

	def descenso(self):
		if self.Maxdescenso == self.rect.top:
			self.contador = 0
			self.Maxdescenso = self.rect.top + 40 
		else:
			self.rect.top += 1

	def movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > self.limiteDerecha:
				self.derecha = False
				self.contador += 1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < self.limiteIzquierda :
				self.derecha = True