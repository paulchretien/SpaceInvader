## Page pour gérer les classes et toutes les variables de mes fonctions du programme Principale.py
# Réalisé le 17/01/2021
# Auteurs : Da Rold Tom et Chretien Paul
# ToDo : Modifier les classes pour qu'elles soient plus complètes et efficaces

import math

class jeu_Spaceinvaders:
    def __init__(self, ma_fenetre):
        # Stock des données du jeu SpaceInvaders
        self.ma_fenetre = ma_fenetre
        self.Vie = 3
        self.Score = 0

class class_alien:
    def __init__(self,X):
        # Stock des infos sur l'allien
        self.Xa = X
        self.Ya = 100
        self.vitesse_a = 7
        self.n = 0
        self.DX_a = self.vitesse_a
        self.RAYON_a = 20
        self.alive = True
        
class class_vaisseau:
    def __init__(self):
        # Stock des infos sur le vaisseau
        self.Xv = 500
        self.Yv = 580

class class_missile:
    def __init__(self,X,Y):
        # Stock des infos sur le missile
        self.Xm = X
        self.Ym = Y
        self.vitesse_m = 10
        self.DY_m = self.vitesse_m
        self.RAYON_m = 10

class class_bloc:
    def __init__(self,X,Y):
        # Stock des infos sur le bloc
        self.Xb = X
        self.Yb = Y 
        