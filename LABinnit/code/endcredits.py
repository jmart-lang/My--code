import pygame
import subprocess
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'background_2.png')

# zazene pygame
pygame.init()

# s tem sem dolocil barve, ki jih hocem, oziroma jih bom rabil za naprej, dolocil sem jih kot spremenljivke, da mi jih ne bi bilo treba vedno znova dolocati
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ta del kode naredi ekrancek, z WINDOE_SIZE dolocim dimenzije okvircka
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game Options")

# s tem ustvarim enega izmed gummbov, tistega, ki bo kasneje dal moznost, da gre igralec se enkrat igrati
play_again_button_rect = pygame.Rect(90, 250, 150, 50)
play_again_button_color = WHITE

# s tem gumbom bo igralec ixsel iz igrice
quit_button_rect = pygame.Rect(260, 250, 150, 50)
quit_button_color = WHITE

# tukaj dolocim font pisave (v resnici sem dolocil samo velikost)
font = pygame.font.Font(None, 36)

# tukaj si lahko izberem, kaj bom prikazal na gumbu, ta del kode pa bo to prikazal na povrsini od gumba
play_again_text = font.render("Še enkrat", True, BLACK)
quit_text = font.render("Konec", True, BLACK)

# s tem delom kode dodam sliko za ozadje, ki se bo prikazovala
background_image = pygame.image.load(image_path).convert_alpha()

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
            # napisano je, da naj zazene drugo datoteko (main.py, ki je glavna datoteka te igrice in tudi tista, ki vse zacne), nato pa zapre okvircek
            if play_again_button_rect.collidepoint(event.pos):
                p = subprocess.Popen('C:\\Users\\jurij\\OneDrive\\Desktop\\LABinnit\\code\\main.py', shell=True)
                pygame.quit()
                p.wait() # cakam, da se proces konca
                p.kill() # hotel sem, da se, ko igralec nekaj pritisne, zapre tudi terminal --> ni mi uspelo
                exit()
            # preveri, ce je bil pritisnjen gumb za izhod:
            # ce je bil ugasne igrico
            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
                
                
    # narise sliko za ozadje v okvircek
    screen.blit(background_image, (0, 0))

    # prikaze gumbe
    pygame.draw.rect(screen, play_again_button_color, play_again_button_rect)
    pygame.draw.rect(screen, quit_button_color, quit_button_rect)

    # napise besedilo na povrsino gumbov
    screen.blit(play_again_text, (play_again_button_rect.centerx - play_again_text.get_width() // 2,
                                    258))
    screen.blit(quit_text, (quit_button_rect.centerx - quit_text.get_width() // 2,
                            258))

    # posodablja display - vidimo kam premikamo misko
    pygame.display.update()

# konca program
pygame.quit()