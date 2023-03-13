import pygame
import os

# to je zadnja stvar, ki jo dodajam, dodal bom kodo, ki bo omogocila, da ta koda tece na kateremkoli racunalniku
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'graphics', 'test',
'background.png')

# zacne pygame
pygame.init()

# velikost okenca in caption
screen_size = (500, 500)
caption = "LABinnit"
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(caption)

# za ozadje sem  sliko naredil sam --> pixilart.com
background_image = pygame.image.load(image_path).convert_alpha()

# oznaci barvo in font pisave (navadna)
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
selected_color = (240, 248, 255)

# tukaj dam na voljo 3 izbire: lahko. srednjo in legendarno kar to naredi v resnici samo spreminja velikost generiranega labirinta 
difficulty_levels={"IZI":(20 ,20) ,"IZZI(V)":(40 ,40) ,"LEGENDA":(100 ,100)}

# ponastavi da ni izbran noben level 
selected_level=None

button_width=200 
button_height=50 

def draw_button(text,x,y):
    button_rect=pygame.draw.rect(screen,(29 ,145 ,158),(x,y ,button_width ,button_height))
    text_surface=font.render(text,True,(255 ,255 ,255))
    text_rect=text_surface.get_rect(center=(x+(button_width//2),y+(button_height//2)))
    screen.blit(text_surface,text_rect)
    return button_rect

# to zanko bo program ponavljal dokler igralec ne izbere tezavnosti 
while not selected_level:
    # to samo projecira sliko ozadja dokler tece zanka 
    screen.blit(background_image,(0 ,0))

    # narise besedilo za vsako izmed tezavnosti in preverja za pritiske gumbov 
    for level,(width,height) in difficulty_levels.items():
        # napise besedilo 
        button_x=(screen_size[0]-button_width)//2 
        button_y=((screen_size[1]//2)+(100*list(difficulty_levels.keys()).index(level)))
        button_rect=draw_button(level ,button_x ,button_y)

        # preverja za pritiske z misko  
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    selected_level=level

    # posodablja zaslon  
    pygame.display.update()

# to je zelo pomembno:  
# to nastevi visino(height) in sirino(width) dve spremenljivki glede na izbrano tezavnost  
# te spremenljivke nato uporabi labyrinth.py ki jih uporabi za nakljucno generiranje labirinta   
width,height=difficulty_levels[selected_level]

# konec programa  
pygame.quit()