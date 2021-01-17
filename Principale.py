# Notre objectif est de coder le jeu space invador
# Réalisé le 17/01/2021
# Auteurs : Da Rold Tom et Chretien Paul
# ToDo : Faire disparaitres les blocs de protection, faire marcher le score, faire apparaître un boss, finitions diverses


# Importation des bibliothèques souhaitées
import math
from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas, messagebox
from Class import jeu_Spaceinvaders, class_alien, class_missile, class_vaisseau, class_bloc


#Fonction permettant à l'utilisateur de lancer sa partie
# Entrées : aucune entrée
# Sorties : fenêtre de jeu qui s'ouvre
def jeu():

    # Création de notre interface graphique
    ma_fenetre = Tk()
    ma_fenetre.title('Space Invader')
    ma_fenetre.geometry('1300x800')
    donnee_jeu = jeu_Spaceinvaders(ma_fenetre)
    alien1 = class_alien(200)
    alien2 = class_alien(420)
    alien3 = class_alien(640)
    Aliens = [alien1,alien2,alien3]
    vaisseau = class_vaisseau()
    Gagne = False # Variable Gagne nécessaire pour ma fonction qui détermine la victoire du joueur 
    Perdu = False # Variable Perdu nécessaire pour ma fonction qui détermine la victoire du joueur
    

    # Création de la zone de jeu
    hauteur = 600
    largeur = 1000
    my_canvas = Canvas(ma_fenetre)
    photo=PhotoImage(file = 'c.png')
    item = my_canvas.create_image(0,0,image = photo)
    my_canvas.pack()


    # Informations pour les aliens 
    alien1_jeu = my_canvas.create_oval(alien1.Xa-alien1.RAYON_a, alien1.Ya-alien1.RAYON_a, alien1.Xa+alien1.RAYON_a, alien1.Ya+alien1.RAYON_a, width = 1, outline='black', fill = 'blue')
    alien2_jeu = my_canvas.create_oval(alien2.Xa-alien2.RAYON_a, alien2.Ya-alien2.RAYON_a, alien2.Xa+alien2.RAYON_a, alien2.Ya+alien2.RAYON_a, width = 1, outline='black', fill = 'blue')
    alien3_jeu = my_canvas.create_oval(alien3.Xa-alien3.RAYON_a, alien3.Ya-alien3.RAYON_a, alien3.Xa+alien3.RAYON_a, alien3.Ya+alien3.RAYON_a, width = 1, outline='black', fill = 'blue')
    Aliens_jeu = [alien1_jeu,alien2_jeu,alien3_jeu]
    

    # Informations pour le vaisseau
    vaisseau_jeu = my_canvas.create_rectangle(vaisseau.Xv-15, vaisseau.Yv-15, vaisseau.Xv+15, vaisseau.Yv+15, width = 1, outline = 'black', fill = 'red')
    my_canvas.focus_set()
    my_canvas.bind('<Key>',lambda event : Clavier(event))
    my_canvas.place(x = 0, y = 100, width = largeur, height = hauteur)


    # Informations pour les blocs
    bloc1 = class_bloc(200,350)
    bloc2 = class_bloc(500,350)
    bloc3 = class_bloc(800,350)

    my_canvas.create_rectangle(bloc1.Xb-30, bloc1.Yb-20, bloc1.Xb+30, bloc1.Yb+20, width = 1, outline = 'black', fill = 'purple')
    my_canvas.create_rectangle(bloc2.Xb-30, bloc2.Yb-20, bloc2.Xb+30, bloc2.Yb+20, width = 1, outline = 'black', fill = 'purple')
    my_canvas.create_rectangle(bloc3.Xb-30, bloc3.Yb-20, bloc3.Xb+30, bloc3.Yb+20, width = 1, outline = 'black', fill = 'purple')


    # Fonction qui permet les mouvements de l'alien
    # Entrées : alien1 de type ccomplexe (classe) et représentant les données liées a l'alien
    # Sorties : alien 1, alien2 et alien3 de type complexe (classe) avec une nouvelle position selon des conditions précises
    def mouvements_aliens(alien1):
        # Lorsque l'alien touche le côté droit
        if alien3.Xa + alien3.RAYON_a + alien3.DX_a > largeur:
            alien3.DX_a = -alien3.DX_a
            alien2.DX_a = -alien2.DX_a
            alien1.DX_a = -alien1.DX_a
            alien3.n += 1
        # Lorsque l'alien touche le côté gauche
        if alien1.Xa - alien1.RAYON_a + alien1.DX_a < 0:
            alien1.DX_a = -alien1.DX_a
            alien3.DX_a = -alien3.DX_a
            alien2.DX_a = -alien2.DX_a
            alien3.n += 1
        # L'alien descend de la moitié de son rayon lorsqu'il a effectué un demi-tour
        if alien3.n == 2:
            alien1.Ya += alien1.RAYON_a
            alien2.Ya += alien1.RAYON_a
            alien3.Ya += alien1.RAYON_a
            alien3.n = 0
        if alien1.Ya > 500:
            fin_de_partie()
        alien1.Xa = alien1.Xa + alien1.DX_a
        alien2.Xa = alien2.Xa + alien2.DX_a
        alien3.Xa = alien3.Xa + alien3.DX_a
        my_canvas.coords(alien1_jeu,alien1.Xa-alien1.RAYON_a, alien1.Ya-alien1.RAYON_a, alien1.Xa+alien1.RAYON_a, alien1.Ya+alien1.RAYON_a)
        my_canvas.coords(alien2_jeu,alien2.Xa-alien2.RAYON_a, alien2.Ya-alien2.RAYON_a, alien2.Xa+alien2.RAYON_a, alien2.Ya+alien2.RAYON_a)
        my_canvas.coords(alien3_jeu,alien3.Xa-alien3.RAYON_a, alien3.Ya-alien3.RAYON_a, alien3.Xa+alien3.RAYON_a, alien3.Ya+alien3.RAYON_a)
        ma_fenetre.after(20,lambda x = alien1 : mouvements_aliens(x))
    ma_fenetre.after(0,lambda x = alien1 : mouvements_aliens(x))


    # Fonction qui permet de relier les touches du clavier à une commande précise 
    # Entrées : event de type complexe qui est une action sur le clavier
    # Sorties : changement de l'abscisse du vaisseau, départ d'un missile
    def Clavier(event):
        touche = event.keysym
        # Le vaisseau se déplace sur la droite si l'on appuie sur la flèche de droite
        if touche == 'Right' and vaisseau.Xv < largeur-20 :
            vaisseau.Xv += 30
        # Le vaisseau se déplace sur la gauche si l'on appuie sur la flèche de gauche
        if touche == 'Left' and vaisseau.Xv > 20:
            vaisseau.Xv -= 30
        # Un missile se lance si l'on appuie sur touche espace
        if touche == 'space' :
            creation_missile()
        # Le vaisseau est recréé à sa nouvelle position
        my_canvas.coords(vaisseau_jeu,vaisseau.Xv-15,vaisseau.Yv-15,vaisseau.Xv+15,vaisseau.Yv+15)


    # Fonction qui crée un missile et qui lance le missile vers le haut
    # Entrées : aucune entrée
    # Sorties : fonction deplacement_missile
    def creation_missile():
        missile = class_missile(vaisseau.Xv,vaisseau.Yv)
        tir_missile = my_canvas.create_oval(vaisseau.Xv-missile.RAYON_m, vaisseau.Yv-missile.RAYON_m, vaisseau.Xv+missile.RAYON_m, vaisseau.Yv+missile.RAYON_m, width=1, outline='black', fill='white')
        def deplacement_missile():
            # Fonction qui assure le déplacement du missile
            if missile.Ym - missile.RAYON_m + missile.DY_m < 0:
                my_canvas.delete(missile)
            else :
                missile.Ym = missile.Ym - missile.DY_m
                my_canvas.coords(tir_missile,missile.Xm-missile.RAYON_m, missile.Ym-missile.RAYON_m, missile.Xm+missile.RAYON_m, missile.Ym+missile.RAYON_m)
                if not mort_aliens(alien1,tir_missile,missile):
                    ma_fenetre.after(20,deplacement_missile)
        deplacement_missile()


    # Fonction qui fait disparaitre le missile tiré par un alien
    # Entrées : vaisseau, tir_missile_aliens, missile_aliens, donnee_jeu
    # Sorties : booleen
    def disparition_missile_aliens(vaisseau,tir_missile_aliens,missile_aliens):
        """ Fonction qui s'occupe de la disparition du missile de l'alien """
        if  missile_aliens.Ym >= vaisseau.Yv - 15 and missile_aliens.Ym <= vaisseau.Yv + 15 and missile_aliens.Xm >= vaisseau.Xv - 15 and missile_aliens.Xm <= vaisseau.Xv + 15 :
            my_canvas.delete(tir_missile_aliens)
            # On perd une vie
            donnee_jeu.Vie = donnee_jeu.Vie - 1
            nombre_vie(donnee_jeu)
            return True
        if missile_aliens.Ym >= bloc1.Yb-50 and missile_aliens.Ym <= bloc1.Yb+50 and missile_aliens.Xm >= bloc1.Xb-50 and missile_aliens.Xm <= bloc1.Xb+50 :
            my_canvas.delete(tir_missile_aliens)
            return True
        if missile_aliens.Ym >= bloc2.Yb-50 and missile_aliens.Ym <= bloc2.Yb+50 and missile_aliens.Xm >= bloc2.Xb-50 and missile_aliens.Xm <= bloc2.Xb+50 :
            my_canvas.delete(tir_missile_aliens)
            return True
        if missile_aliens.Ym >= bloc3.Yb-50 and missile_aliens.Ym <= bloc3.Yb+50 and missile_aliens.Xm >= bloc3.Xb-50 and missile_aliens.Xm <= bloc3.Xb+50 :
            my_canvas.delete(tir_missile_aliens)
            return True
        return False


    # Fonction qui permet de créer et envoyer un missile de la part des aliens
    # Entrées : aucune entrée
    # Sorties : nouvelle abscisse pour le missile de l'alien
    def creation_missile_aliens():
        missile_aliens1 = class_missile(alien1.Xa,alien1.Ya)
        tir_missile_aliens1 = my_canvas.create_oval(alien1.Xa-missile_aliens1.RAYON_m, alien1.Ya-missile_aliens1.RAYON_m, alien1.Xa+missile_aliens1.RAYON_m, alien1.Ya+missile_aliens1.RAYON_m, width=1, outline='black', fill='pink')
        missile_aliens2 = class_missile(alien2.Xa,alien2.Ya)
        tir_missile_aliens2 = my_canvas.create_oval(alien2.Xa-missile_aliens2.RAYON_m, alien2.Ya-missile_aliens2.RAYON_m, alien2.Xa+missile_aliens2.RAYON_m, alien2.Ya+missile_aliens2.RAYON_m, width=1, outline='black', fill='green')
        missile_aliens3 = class_missile(alien3.Xa,alien3.Ya)
        tir_missile_aliens3 = my_canvas.create_oval(alien3.Xa-missile_aliens3.RAYON_m, alien3.Ya-missile_aliens3.RAYON_m, alien3.Xa+missile_aliens3.RAYON_m, alien3.Ya+missile_aliens3.RAYON_m, width=1, outline='black', fill='yellow')
        def deplacement_missile_aliens(missile_aliens,tir_missile_aliens):
            # Dispararition du missile si il sort de la fenêtre de jeu
            if missile_aliens.Ym + missile_aliens.RAYON_m - missile_aliens.DY_m > 600 :
                my_canvas.delete(missile_aliens)
            else :
                missile_aliens.Ym = missile_aliens.Ym + missile_aliens.DY_m
                my_canvas.move(tir_missile_aliens,0,missile_aliens.DY_m)
                if not disparition_missile_aliens(vaisseau,tir_missile_aliens,missile_aliens):
                    ma_fenetre.after(20,lambda:deplacement_missile_aliens(missile_aliens,tir_missile_aliens))
        deplacement_missile_aliens(missile_aliens1,tir_missile_aliens1)
        deplacement_missile_aliens(missile_aliens2,tir_missile_aliens2)
        deplacement_missile_aliens(missile_aliens3,tir_missile_aliens3)
        ma_fenetre.after(900,creation_missile_aliens)
    creation_missile_aliens()


    # Fonction qui fait mourir l'alien et fait disparaitre le missile quand ce dernier atteint l'alien
    # Entrées : donnee_alien, tir_missile, missile
    # Sorties : booléen, renvoie true si une condition a été remplie et l'action correspondante a été appliquée
    def mort_aliens(donnee_alien, tir_missile, missile):
        global tir_missile_aliens1, tir_missile_aliens2, tir_missile_aliens3
        if  missile.Ym >= alien1.Ya - alien1.RAYON_a and missile.Ym <= alien1.Ya + alien1.RAYON_a and missile.Xm >= alien1.Xa - alien1.RAYON_a and missile.Xm <= alien1.Xa + alien1.RAYON_a  : 
            my_canvas.delete(tir_missile)
            my_canvas.delete(alien1_jeu)
            my_canvas.delete(tir_missile_aliens1)

            return True
        if  missile.Ym >= alien2.Ya - alien2.RAYON_a and missile.Ym <= alien2.Ya + alien2.RAYON_a and missile.Xm >= alien2.Xa - alien2.RAYON_a and missile.Xm <= alien2.Xa + alien2.RAYON_a  : 
            my_canvas.delete(tir_missile)
            my_canvas.delete(alien2_jeu)
            my_canvas.delete(tir_missile_aliens2)
            return True
        if  missile.Ym >= alien3.Ya - alien3.RAYON_a and missile.Ym <= alien3.Ya + alien3.RAYON_a and missile.Xm >= alien3.Xa - alien3.RAYON_a and missile.Xm <= alien3.Xa + alien3.RAYON_a  : 
            my_canvas.delete(tir_missile)
            my_canvas.delete(alien3_jeu)
            my_canvas.delete(tir_missile_aliens3)
            return True
        if missile.Ym >= bloc1.Yb-50 and missile.Ym <= bloc1.Yb+50 and missile.Xm >= bloc1.Xb-75 and missile.Xm <= bloc1.Xb+75 :
            my_canvas.delete(tir_missile)
            return True
        if missile.Ym >= bloc2.Yb-50 and missile.Ym <= bloc2.Yb+50 and missile.Xm >= bloc2.Xb-75 and missile.Xm <= bloc2.Xb+75 :
            my_canvas.delete(tir_missile)
            return True
        if missile.Ym >= bloc3.Yb-50 and missile.Ym <= bloc3.Yb+50 and missile.Xm >= bloc3.Xb-75 and missile.Xm <= bloc3.Xb+75 :
            my_canvas.delete(tir_missile)
            return True
        return False


    # Fonction qui affiche le nombre de vies restantes
    # Entrées : donnee_jeu de type complexe
    # Sorties : fenêtre affichant le nombre de vies calculées automatiquement  
    def nombre_vie(donnee_jeu):
        nombre_vie = Label(donnee_jeu.ma_fenetre, text = 'Vies restantes : ' + str(donnee_jeu.Vie), bg = 'white',fg = 'black', font = 100)
        nombre_vie.place(x = 700, y = 5, width = 300, height = 30)
  
    # Fonction qui permet de redemarrer une partie
    # Entrées : aucune entrée
    # Sorties : fonction jeu()
    def rejouer():
        ma_fenetre.destroy()
        jeu()
    

    # Fonction qui indique au joueur qu'il a perdu
    # Entrées : aucune entrée
    # Sorties : fenetre qui affiche un message
    def perdu():

        Perdu = False
        if alien1.Ya + alien1.RAYON_a >= vaisseau.Xv or alien2.Ya + alien2.RAYON_a >= vaisseau.Xv or alien3.Ya + alien3.RAYON_a >= vaisseau.Xv  :
            Perdu = True
            my_canvas.delete(vaisseau_jeu)
            my_canvas.delete(alien1_jeu)
        if donnee_jeu.Vie <= 0:
            Perdu = True
        if Perdu == True:
            buttonRecommencer = Button (ma_fenetre, text = "RECOMMENCER", fg = 'black', bg = 'white',relief = 'groove', command = rejouer)
            buttonRecommencer.place(x = 200, y = 400, width = 300, height = 100)
            buttonQuitt = Button (ma_fenetre, text = "QUITTER", fg = 'black', bg = 'white',relief = 'groove', command = ma_fenetre.destroy)
            buttonQuitt.place(x = 500, y = 400, width = 300, height = 100)
            partie_perdu = Label(ma_fenetre, text = 'Game Over', bg = 'white',fg = 'black', font = 100)
            partie_perdu.place(x = 200, y = 300, width = 600, height = 50)
        else :
            ma_fenetre.after(1000,perdu)
    perdu()


    # Création d'un widget Menu
    menubar = Menu(ma_fenetre)
    menuoption = Menu(menubar,tearoff = 0)
    menuoption.add_command(label = "Recommencer une partie", command = ma_fenetre.destroy) # Boutton pour recommencer une partie
    menuoption.add_command(label = "Quitter le jeu", command = ma_fenetre.destroy) # Boutton pour quitter 
    menubar.add_cascade(label = "Option", menu = menuoption)

    # Affichage du menu
    ma_fenetre.config(menu = menubar)

    # Création d'un widget Button pour recommencer une partie
    buttonRecommencer = Button (ma_fenetre, text="RECOMMENCER", fg = 'white', bg='black',relief = 'groove', command = rejouer)
    buttonRecommencer.place(x = 1050, y = 250, width = 100, height = 50)

    

    

    # Création d'un widget Label pour afficher le nombre de vies restantes
    nombre_vies = Label(ma_fenetre, text='Vie :' , bg='white',fg='black', font=100)
    nombre_vies.place(x=700, y=5, width=300, height=30)


    # Création d'un widget Label (Pour afficher le nombre de vie du joueur)
    nombre_vie(donnee_jeu)       
    # Création d'un widget Button (boutton_quitter)
    bouton_quitter = Button (ma_fenetre, text = "QUITTER", fg = 'white', bg = 'black',relief = 'groove', command = ma_fenetre.destroy)
    bouton_quitter.place(x = 1050, y = 450, width = 100, height = 50)


    ma_fenetre.mainloop()
    
