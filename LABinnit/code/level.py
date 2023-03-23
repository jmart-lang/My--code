import pygame
from settings import *
from labyrinth import *
from tile import Tile  
from player import Player
from portal import Portal
#from floor import Floor

class Level: 
    def __init__(self):

        # Dobim povrsino prikaza
        self.display_surface = pygame.display.get_surface()

        # naredim prvo skupino za sprite
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.portal_sprites = pygame.sprite.Group()


        # vzpostavitev sprita
        self.create_map()

    # naredil bom novo funkcijo, s katero bom prikazoval labirint
    def create_map(self):
        # za vsako vrsto 
        for row_index,row in enumerate(WORLD_MAP):
            # zdej imam pozicijo (navpicno) od vsake vrste tilov = dobim y koordinato
            #  s tem for loopom sem sel cez vsako vrstico, s spodnjim pa se cez vsak x ali pa presledek v tej vrstici - grem cez cel list labirinta
            for col_index,col in enumerate(row):
                # tako dobim x in y koordinato
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # zdaj ima cel svet neko doloceno pozicijo
                # zdaj lahko recem, da ce je ena enota sveta dolocena kot x, naj bo to stena labirinta
                if col == 'w':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                # zdaj dodam se igralca
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.portal_sprites)# <--
                # dodati moram se sprite, ki bo, ko se ga igralec dotakne, koncal igro
                if col == 's':
                    Portal((x,y),[self.visible_sprites,self.portal_sprites])
                #if col == ' ':
                    #Floor ((x,y),[self.visible_sprites])

    def run(self):
        # hocem, da se igra obnavlja in prikazuje
        # s tem pokazem sprite 
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        

# dodam se en class, za to da dobim funkcionalno kamero, ki sledi liku igralca
# CameraGroup : pomeni da bo ta class odgovoren za kamero
# YSort : pomeni, da bomo vse sprite sortirali po Y koordinati in tako bomo lahko dodali overlap --> lazno globino
# kako kamera deluje: deluje znotraj funkcije custom_draw, v bistvu namesto da isem sprite znotraj njegovega rectangla, lahko dodam offset in tako omogocim premik
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # navaden setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        # ustvarim vektor za kamero
        # kolikersno pozicijo dam temu vektorju, toliko bo kamera zamaknjena
        # v primeru, da bi mu dal pozicijo (100, 200), bi celotna slika bila zamaknjena za 100 v desno in za 200 dol
        # nisem spremenil pozicije nicesar, samo risem sprite 'z zamikom'
        # ce hocem da s ekmera centrira na igralca moram najprej dobiti dimenzije zaslona
        self.offset = pygame.math.Vector2()
        # s spodnjima dvema vrsticama kode vem, koliko sem oddaljen od obeh robov ekrana
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    # dodam se en argument, player, tako lahko dobim njegovo pozicijo
    def custom_draw(self, player):
        
        # s to kodo dobimo 'offset' (zamik)
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # prejsnja metoda -->  for sprite in self.sprites():
        # ni bila liabilna, ker so se spriti narbe prekrivali z likom igralca
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)