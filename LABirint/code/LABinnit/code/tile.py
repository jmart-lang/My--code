import pygame
from settings import *
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'stena.png')

# ustvarimo nov class
class Tile(pygame.sprite.Sprite):
    # pos = rabimo pozicijo vseh spritov
    # groups = del katere skupine je sprite
    def __init__(self,pos,groups,):
        # zastartamo clas v vrstici 5 
        super().__init__(groups)
        # zato ker imamo tukaj zgoraj znotraj oklepaja groups, lahko uporabimo spodnja izraza, saj sta nujna za vsak sprite
        # tukaj hocem naloziti sliko, zato moram uporabiti pygame.image.load, ter dodati kje se nahaja in jo pretvoriti v obliko, 
        ## ki jo zaslon lahko prikaze
        self.image = pygame.image.load(image_path).convert_alpha()
        # topleft = position
        self.rect = self.image.get_rect(topleft = pos)
        # dolocil bom hitbox, z inflate bom spremenil originalen hitbox, isto stvar bom naredil se za lik igralca
        self.hitbox = self.rect.inflate(0,-22)

        # dobil sem program, ki mi bo na zaslonu prikazoval stene labirinta, ta program se da kopirati