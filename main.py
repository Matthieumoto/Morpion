import pygame
import ligne
import choix


def main():
    pygame.init()

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mon jeu Pygame")

    running = True

    background_color = (255, 255, 255)
    screen.fill(background_color)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    x, y = event.pos  # Obtenez les coordonnées du clic
                    choix.win()
                    choix.croix(screen, x, y, screen_width, screen_height)
                    choix.rond(screen, screen_width, screen_height)
                    
        
        ligne.lig(screen, screen_width, screen_height)
        pygame.display.update()

        resultat = choix.win()
        if resultat:
            print("Le gagnant est:", resultat)
            break
             
if __name__ == "__main__":
    main()