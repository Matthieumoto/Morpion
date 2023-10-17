from main import *

def rectangle(screen):
    longeur = 0
    largeur = 0

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, (250, 250, 250), (longeur, largeur, 100, 100))
            longeur += 100
        largeur += 100
        longeur = 0
    