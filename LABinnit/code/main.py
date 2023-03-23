import pygame, sys
from settings import *
#vpeljemo class Level iz level.py to pomeni da ga lahko uporabljamo tukaj
from level import Level
#vpeljem subprocess, da lahko odpiram druge datoteke, med tem ko ena ze tece
import subprocess 

colour = (209, 142, 12)

class Game:
	def __init__(self):
		
		# general setup
		#zacne pygame
		pygame.init()
		#ustvari povrsino na kateri se bo prikazovala igrica
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		#poimenuje okence LABinnit
		pygame.display.set_caption('LABinnit')
		#ustvarim uro
		self.clock = pygame.time.Clock()
		
		self.level = Level()
	
	def run(self):
		#zazenem inp datoteko, to mi omogoci, da izberem tezavnost igrice
		subprocess.run(['inp'], shell=True)

		#event loop: preverja, ce se je igra zaprla
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			#zaslon nastavim na izbrano barvo
			self.screen.fill(colour)

			#zazenem class level v tem loopu
			self.level.run()
			#posodablja zaslon
			pygame.display.update()
			#nadzorujem FPS
			self.clock.tick(FPS)

#preveri, ce je to glavna datoteka
if __name__ == '__main__':
	#ustvarimo novo igro
	game = Game()
	#zazenemo igro
	game.run()