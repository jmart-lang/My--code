import pygame
import subprocess
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'background_2.png')

script_dir2 = os.path.dirname(os.path.abspath(__file__))
image_path2 = os.path.join(script_dir2, '..', 'graphics', 'test',
'button.png')

script_dir3 = os.path.dirname(os.path.abspath(__file__))
image_path3 = os.path.join(script_dir3, '..', 'graphics', 'test',
'button2.png')

script_dir4 = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir4, '..', 'code', 'main.py',)

script_dir5 = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(script_dir5, '..', 'music', 'konec.wav',)

# zazene pygame
pygame.init()

#za glasbo hocem da se predvaja ves cas
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

# s tem sem dolocil barve, ki jih hocem, oziroma jih bom rabil za naprej, dolocil sem jih kot spremenljivke
# da mi jih ne bi bilo treba vedno znova dolocati
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ta del kode naredi ekrancek, z WINDOE_SIZE dolocim dimenzije okvircka
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("LABinnit")

# s tem ustvarim enega izmed gummbov, tistega, ki bo kasneje dal moznost, da gre igralec se enkrat igrati
replay_button_surface = pygame.Surface((200, 50))
replay_button_surface.set_alpha(0)
replay_button_surface.fill((0,0,0))
replay_button_rect = replay_button_surface.get_rect(center=(25, 250))


# s tem gumbom bo igralec ixsel iz igrice
quit_button_surface = pygame.Surface((200, 200))
quit_button_surface.set_alpha(0)
quit_button_surface.fill((0,0,0))
quit_button_rect = quit_button_surface.get_rect(center=(275, 250))


# tukaj dolocim font pisave (v resnici sem dolocil samo velikost)
font = pygame.font.Font(None, 36)

# tukaj si lahko izberem, kaj bom prikazal na gumbu, ta del kode pa bo to prikazal na povrsini od gumba
play_again_text = font.render("Še enkrat", True, WHITE)
quit_text = font.render("Konec", True, WHITE)

# s tem delom kode dodam sliko za ozadje, ki se bo prikazovala
background_image = pygame.image.load(image_path).convert_alpha()
button_image = pygame.image.load(image_path2).convert_alpha()
button_image2 = pygame.image.load(image_path3).convert_alpha()

# tukaj je loop, to tece dokler igralec ne izbere ene izmed opcij
running = True
while running:
    # z eventi, ki ji to preverjaa mislimo v tem primeru klik na gumb z uporabo miske
    for event in pygame.event.get():
        # ce zapremo okvircek, se bo koda ustavila
        if event.type == pygame.QUIT:
            pygame.quit()
        # to doloca, kaj se bo zgodilo, ce igralec pritisne na gumb z misko
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ce je igralec pritisnil na gumb za ponovno igro, se bo zgodilo kar je napisano spodaj:
            # napisano je, da naj zazene drugo datoteko (main.py, ki je tista, ki vse zacne), nato pa zapre okvircek
            if replay_button_rect.collidepoint(event.pos):
                p = subprocess.Popen(file_path, shell=True)
                pygame.quit()
                p.wait() # cakam, da se proces konca
                p.kill() # hotel sem, da se, ko igralec nekaj pritisne, zapre tudi terminal --> ni mi uspelo
                exit()
            # preveri, ce je bil pritisnjen gumb za izhod:
            # ce je bil ugasne igrico
            elif quit_button_rect.collidepoint(event.pos):
                running = False
                
                
    # narise sliko za ozadje v okvircek
    screen.blit(background_image, (0, 0))
    screen.blit(button_image, (275, 250))
    screen.blit(button_image2, (25, 250))

    # prikaze gumbe
    screen.blit(replay_button_surface, replay_button_rect)
    screen.blit(quit_button_surface, quit_button_rect)

    # napise besedilo na povrsino gumbov
    screen.blit(play_again_text, (replay_button_rect.centerx - play_again_text.get_width() // 2 + 100,
                                    258))
    screen.blit(quit_text, (quit_button_rect.centerx - quit_text.get_width() // 2 + 100,
                            258))

    # posodablja display - vidimo kam premikamo misko
    pygame.display.update()

# konca program
pygame.quit()