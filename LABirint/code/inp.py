import pygame
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'background.png')

script_dir2 = os.path.dirname(os.path.abspath(__file__))
image_path2 = os.path.join(script_dir2, '..', 'graphics', 'test',
'gumb.png')

script_dir3 = os.path.dirname(os.path.abspath(__file__))
image_path3 = os.path.join(script_dir3, '..', 'graphics', 'test',
'gumb2.png')

script_dir4 = os.path.dirname(os.path.abspath(__file__))
image_path4 = os.path.join(script_dir4, '..', 'graphics', 'test',
'gumb3.png')

script_dir5 = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(script_dir5, '..', 'music', 'zacetek.wav',)

# zacne pygame
pygame.init()

# velikost okenca in caption
screen_size = (500, 500)
caption = "Choose a difficulty level"
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(caption)

# za ozadje sem  sliko naredil sam --> pixilart.com
background_image = pygame.image.load(image_path).convert_alpha()
button1_image = pygame.image.load(image_path2).convert_alpha()
button2_image = pygame.image.load(image_path3).convert_alpha()
button3_image = pygame.image.load(image_path4).convert_alpha()

# oznaci barvo in font pisave (navadna)
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
selected_color = (240, 248, 255)

# tukaj dam na voljo 3 izbire: lahko. srednjo in legendarno 
# v resnici to samo spreminja velikost generiranega labirinta
difficulty_levels = {"EASY": (20, 20), "MEDIUM": (40, 40), "LEGENDARY": (100, 100)}

# ponastavi, da ni izbran noben level
selected_level = None

#hocem glasbo, zato sem se odlocil dodati se en scrpt
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

# to zanko bo program ponavljal, dokler igralec ne izbere tezavnosti
while not selected_level:
    # to samo projecira sliko ozadja, dokler tece zanka
    screen.blit(background_image, (0, 0))
    screen.blit(button1_image, (150, 225))
    screen.blit(button2_image, (150, 325))
    screen.blit(button3_image, (150, 425))

    # narise besedilo za vsako izmed tezavnosti in preverja za pritiske gumbov
    for level, (width, height) in difficulty_levels.items():
        # napise besedilo
        text = font.render(level, True, text_color)
        text_rect = text.get_rect(center=(screen_size[0] // 2, (screen_size[1] // 2) + (100 * list(difficulty_levels.keys()).index(level))))
        if selected_level == level:
            text_color = selected_color
        else:
            text_color = (255, 255, 255)
        screen.blit(text, text_rect)

        # preverja za pritiske z misko
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect.collidepoint(event.pos):
                    selected_level = level

    # posodablja zaslom
    pygame.display.update()



# to je zelo pomembno:
# to nastevi visino(height) in sirino(width), dve spremenljivki, glede na izbrano tezavnost
# te spremenljivke nato uporabi labyrinth.py, ki jih uporabi za nakljucno generiranje labirinta 
width, height = difficulty_levels[selected_level]

# konec programa  
pygame.quit()