import Administrateur as admin
import Utilisateur as user
import random
import string
import os



def test_ajouter_utilisateur():
    test1 = admin.Administrateur()
    charrandom = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    loginRandom = "TEST"+charrandom
    test1.ajouter_utilisateur(loginRandom, charrandom, loginRandom, loginRandom,loginRandom+"@hotmail.fr")
    fichierLogin = open("login.txt", "r")
    ligne = fichierLogin.read().splitlines()
    #On ouvre le fichier login afin de vérifier qu'il y a bien le login & le mdp
    assert ligne[-1] == loginRandom+";"+charrandom #Assert : bloquant si ça passe pas
    #On regarde dans l'arborescence si il y a bien l'annuaire de ESTIENNE Clément qui est crée.
    dir = os.listdir()
    assert loginRandom+"_LDAP.csv" in dir
    #On regarde dans le fichier authorisation.txt si il y a bien écrit la ligne qui dit que la personne a comme droit 2 dans ce même fichier
    print("Test ajouter utilisateur : OK")
    
def test_ajouter_contact():
    testAddC = user.Utilisateur()
    #TODO
    assert testAddC.ajouter_contact()
    #TODO
    
def test_get_authorisation():
    testGetAuth = user.Utilisateur()
    #TODO
    assert testGetAuth.get_autorisation()
    #TODO
      
def appeler_tests():
    test_ajouter_utilisateur()
    test_ajouter_contact()
    test_get_authorisation()
    
appeler_tests()