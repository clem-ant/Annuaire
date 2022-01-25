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
    assert ligne[-1] == loginRandom+";"+charrandom, "La dernière ligne du fichier login.txt n'est pas celle qui a été demandé" #Assert : bloquant si ça passe pas
    
    
    #On regarde dans l'arborescence si il y a bien l'annuaire de ESTIENNE Clément qui est crée.
    dir = os.listdir()
    assert loginRandom+"_LDAP.csv" in dir, "Il n'y a pas eu création de l'annuaire dans l'arboressence"
    
    
    #On regarde dans le fichier authorisation.txt si il y a bien écrit la ligne qui dit que la personne a comme droit 2 dans ce même fichier
    fichierAuth = open("authorisation.txt", "r")
    fLigneAuth = fichierAuth.read().splitlines()
    assert fLigneAuth[-1] == loginRandom+";2;"+loginRandom+"_LDAP.csv"
    
    
    
    print("Test ajouter utilisateur : OK")
    
def test_ajouter_contact():
    testAddC = user.Utilisateur()
    #TODO
    assert testAddC.ajouter_contact()
    #TODO
    
def test_get_authorisation():
    testGetAuth = user.Utilisateur()
    #TODO
    assert testGetAuth.get_autorisation("TESTMAH2ZO246D", "TESTMAH2ZO246D_LDAP.csv") == 2, "Lors de la création du compte de l'utilisateur, il n'y a pas automatiquement la création de son autorisation dans le fichier authorisation.txt"
    assert testGetAuth.get_autorisation("test", "test_LDAP.csv") == 0
    #TODO
      
def appeler_tests():
    test_ajouter_utilisateur()
    # test_ajouter_contact()
    test_get_authorisation()
    
appeler_tests()