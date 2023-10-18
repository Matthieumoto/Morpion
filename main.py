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
    pygame.display.set_caption("Morpion Joueur VS Bot :")

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

def main2():
    pygame.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion Joueur VS Joueur :")

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
                    choix.croix(screen, x, y, screen_width, screen_height, grid)
                if event.button == 3: # Clic gauche
                    x, y = event.pos
                    choix.croix2(screen, x, y, screen_width, screen_height, grid)
                    
        
        ligne.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat1 = choix.win2(grid)
        if resultat1:
            print("Le gagnant est:", resultat1)
            game_over = True
        
        if game_over == True:
            rejouer2(resultat1)

def ma_fenetre():
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title('Morpion :')

    choix_label = Label(fenetre, text="Jeux du Morpion")
    choix_label.pack()

    bouton_bot = Button(fenetre, text="Joueur VS Bot", command=lambda: [fenetre.destroy(), main()])
    bouton_bot.pack()

    bouton_jouer = Button(fenetre, text="Joueur VS Joueur", command=lambda: [fenetre.destroy(), main2()])
    bouton_jouer.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: fenetre.destroy())
    bouton_quit.pack()

    fenetre.mainloop()

def rejouer(resultat):
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title(f"le gagnant est : {resultat}")

    if resultat == "Joueur":
        choix_label = Label(fenetre, text="Vous avez gagner !")
        choix_label.pack()
    elif resultat == "Bot":
        choix_label = Label(fenetre, text="Vous avez perdu !")
        choix_label.pack()
    else:
        choix_label = Label(fenetre, text="Vous avez fait match nul !")
        choix_label.pack()

    bouton_jouer = Button(fenetre, text="Voulez vous rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), ma_fenetre()])
    bouton_jouer.pack()

    fenetre.mainloop()

def rejouer2(resultat1):
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title(f"le gagnant est : {resultat1}")

    if resultat1 == "Joueur 1 (Croix)":
        choix_label = Label(fenetre, text="Le joueur 1 (Croix) a Gagner !")
        choix_label.pack()
    elif resultat1 == "Joueur 2 (Cercle)":
        choix_label = Label(fenetre, text="Le joueur 2 (Cercle) a Gagner !")
        choix_label.pack()
    else:
        choix_label = Label(fenetre, text="Vous avez fait match nul !")
        choix_label.pack()

    bouton_jouer = Button(fenetre, text="Voulez vous rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), ma_fenetre()])
    bouton_jouer.pack()

    fenetre.mainloop()

if __name__ == "__main__":
    ma_fenetre()
