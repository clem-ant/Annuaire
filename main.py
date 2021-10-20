import socket as sk
import random as rd
import Administrateur as admin


administrateur = admin.Administrateur("PAYET", "Clément")
administrateur.ajouter_utilisateur("ESTIENNE", "Clément", "niah-niah@hotmail.fr")
administrateur.ajouter_utilisateur("DUGUAIT", "Nicolas", "nicolas.duguait@hotmail.fr", "0624522323", "2 rue de la gare, Toulouse, 31400")
administrateur.supprimer_utilisateur("DUGUAIT", "Nicolas")
administrateur.modifier_utilisateur("ESTIENNE", "Clément")
administrateur.modifier_utilisateur("NonDansLaListe", "TEST")

administrateur.afficher_utilisateur_list() #Liste a envoyer sur le serveur