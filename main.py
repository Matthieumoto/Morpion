import pygame
import ligne
import choix
from tkinter import *

def main():
    pygame.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion :")

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
                    choix.win(grid)
                    choix.croix(screen, x, y, screen_width, screen_height, grid)
                    choix.rond(screen, screen_width, screen_height, grid)
                    
        
        ligne.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat = choix.win(grid)
        if resultat:
            print("Le gagnant est:", resultat)
            game_over = True
        
        if game_over == True:
            rejouer(resultat)

def ma_fenetre():
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title('Morpion :')

    choix_label = Label(fenetre, text="Jeux du Morpion")
    choix_label.pack()

    bouton_jouer = Button(fenetre, text="Jouer", command=lambda: [fenetre.destroy(), main()])
    bouton_jouer.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: fenetre.destroy())
    bouton_quit.pack()

    fenetre.mainloop()

def rejouer(resultat):
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title('Morpion :')

    if resultat == "Joueur":
        choix_label = Label(fenetre, text="Vous avez gagner !")
        choix_label.pack()
    elif resultat == "Bot":
        choix_label = Label(fenetre, text="Vous avez perdu !")
        choix_label.pack()
    else:
        choix_label = Label(fenetre, text="Vous avez fait match nul !")
        choix_label.pack()

    gagnan_label = Label(fenetre, text=f"le gagnant est : {resultat}")
    gagnan_label.pack()

    bouton_jouer = Button(fenetre, text="Voulez vous rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), ma_fenetre()])
    bouton_jouer.pack()

    fenetre.mainloop()

if __name__ == "__main__":
    ma_fenetre()
