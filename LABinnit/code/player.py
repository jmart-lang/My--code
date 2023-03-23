import pygame
from settings import *
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'Theseus_right.png')
image_path2 = os.path.join(script_dir, '..', 'graphics', 'test',
'Theseus_left.png')
image_path3 = os.path.join(script_dir, '..', 'graphics', 'test',
'Theseus_up.png')
image_path4 = os.path.join(script_dir, '..', 'graphics', 'test',
'Theseus_down.png')
script_dir2 = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir2, '..', 'code', 'endcredits.py')

# ustvarim nov class
# ta program sem skopiral iz tile.py, vse kar rabim narediti je samo spremeniti ime classa in pa popraviti nekaj manjsih zadev

# spremenil sem ime classa v Player
class Player(pygame.sprite.Sprite):
    # pos = rabim pozicijo vseh spritov
    # groups = del katere skupine je sprite
    # obstacle_sprites = vedeti je treba pozicije ovir, ce hocem, da collisons delujejo
    def __init__(self,pos,groups,obstacle_sprites,portal_sprites): #  <--
        # zastartamo clas v vrstici 5 
        super().__init__(groups)
        # zato ker je tukaj zgoraj znotraj oklepaja groups, lahko uporabim spodnja izraza, saj sta nujna za vsak sprite
        # tukaj hocem naloziti sliko, zato moram uporabiti pygame.image.load, ter dodati kje se nahaja in jo pretvoriti v obliko, 
        ## ki jo zaslon lahko prikaze
        # tukaj sem moral spremeniti pot do datoteke
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)

        # dobil sem program, ki nam bo na zaslonu prikazoval igralca oz. njegov lik

        # da mi 2 vektorja, ki sta navadno 0,0
        # z pritiskom na tipkovnico se bo ta vrednost spreminjala
        # rabim vnos tipkovnice
        self.direction = pygame.math.Vector2()
        # dam mu se hitrost, s katero lahko pomnozimo premik in tako dobimo stalno giabnje
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.portal_sprites = portal_sprites #  <--
    
    def input(self):
        # vse tipke, ki so pritisnjene na tipkovnici
        keys = pygame.key.get_pressed()
        # ce pritisnem puscico ki kaze gor/dol, se bo lik premaknil gor/dol
        # dodal sem moznost, da se spreminja slika igralcevega lika, glede na to, katero tipko pritisne
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.image = pygame.image.load(image_path3).convert_alpha()
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.image = pygame.image.load(image_path4).convert_alpha()
        # ce ne dodam tega else, bi se lik premikal naprej
        else:
            self.direction.y = 0

        # ce pritisnem puscico ki kaze desno/levo, se bo lik premaknil desno/levo
        # treba je spremeniti direction iz y v x in dodati vrednosti
        # dodal sem moznost, da se spreminja slika igralcevega lika, glede na to, katero tipko pritisne
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = pygame.image.load(image_path).convert_alpha()
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.image.load(image_path2).convert_alpha()
        # ce ne dodam tega else, bi se lik premikal naprej
        else:
            self.direction.x = 0

    # ustvarim nacin premikanja
    def move(self,speed):
        # to dodam, da, ce se lik premika diagonalno, da se hitrosti ne sestevajo ampak vedno ostanejo enake
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # tukaj moram dolociti horizontalno in vertikalno gibanje
        self.hitbox.x += self.direction.x * speed
        # ko premaknem lik igralca hocem preveriti horizontalne trke
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        # ko premaknem igralca hocem preveriti vertikalne trke
        self.collision('vertical')
        #  prejsnja metoda --> self.rect.center += self.direction * speed
        self.rect.center = self.hitbox.center
    
    # ustvarim novo funkcijo, ki bo obravnavala 'trke' med spriti
    # dam smer, ki je lahko vertikalna ali horizontalna

    def collision(self,direction):
        # ce je smer horizontalna:
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                # preverim, ce sprite igralca trci ob sprite ovire
                if sprite.hitbox.colliderect(self.hitbox):
                    # ne vem ali trci na desni ali na levi strani
                    # predvidevam, da lahko trci z oviro samo v smeri, v katero se premika
                    if self.direction.x > 0: #  <-- tukaj se premikam v desno (vektor gibanja je vecji od nic)
                        self.hitbox.right = sprite.hitbox.left # vem da se premikam v desno kar pomeni da trcim z levo stranjo ovire 
                        # hocem premakniti desno stran igralca zraven leve strani ovire
                    if self.direction.x < 0: #  <-- tekaj se premikam v levo (vektor gibanja je manjsi od nic)
                        self.hitbox.left = sprite.hitbox.right #  vem da se premikam v levo kar pomeni da trcim z desno stranjo ovire
                        # igralca premaknem na desno stran ovire
            # tuki naprej
            for sprite in self.portal_sprites:
                        if sprite.hitbox.colliderect(self.hitbox):
                            pygame.display.quit() # zaprem pygame display window
                            os.system(file_path) # zazenem datoteko endcredits.py
                            quit() 

        # ce je smer vertikalna
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                # preverim, ce sprite igralca trci ob sprite ovire
                if sprite.hitbox.colliderect(self.hitbox):
                    # ne vem ali trci na zgornji ali na spodnji strani
                    # predvidevam, da lahko trci z oviro samo v smeri, v katero se premika
                    if self.direction.y > 0: #  <-- tekaj se premikam dol (vektor gibanja je manjsi od nic)
                        self.hitbox.bottom = sprite.hitbox.top #  vem da se premikam dol kar pomeni da trcim z zgornjo stranjo ovire
                        # igralca premaknem na zgornjo stran ovire
                    if self.direction.y < 0: #  <-- tukaj se premikam gor (vektor gibanja je vecji od nic)
                        self.hitbox.top = sprite.hitbox.bottom #  vem da se premikam gor kar pomeni da trcim s spodnjo stranjo ovire 
                        # hocem premakniti zgornjo stran igralca zraven spodnje strani ovire
            # tuki naprej
            for sprite in self.portal_sprites:
                        if sprite.hitbox.colliderect(self.hitbox):
                            pygame.display.quit() # zaprem pygame display window
                            os.system(file_path) # zazenem datoteko endcredits.py
                            quit()
                            

    # igra samo sebe posodablja
    def update(self):
        self.input()
        self.move(self.speed)