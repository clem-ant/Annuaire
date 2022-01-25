import Administrateur as admin
import Utilisateur as user
import random
import string
import os



def test_ajouter_utilisateur():
    test1 = admin.Administrateur()
    charrandom = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    loginRandom = "TEST"+charrandom
    test1.ajouter_utilisateur(loginRandom, "azerty", loginRandom, loginRandom,loginRandom+"@hotmail.fr")
    #On ouvre le fichier login afin de vérifier qu'il y a bien le login & le mdp
    fichierLogin = open("login.txt", "r")
    ligne = fichierLogin.read().splitlines()
    
    
    
    assert ligne[-1] == loginRandom+";azerty" #Assert : bloquant si ça passe pas.
    
    #On regarde dans l'arborescence si il y a bien l'annuaire de ESTIENNE Clément qui est crée.
    dir = os.listdir()
    assert loginRandom+"_LDAP.csv" in dir
            
    
    print("Test ajouter utilisateur : OK")
    
def appeler_tests():
    test_ajouter_utilisateur() #Ajouter paramètre afin de vérifier pour n'importe quel nom ? 
    
appeler_tests()