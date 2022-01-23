import Administrateur as admin
import Utilisateur as user



def test_ajouter_utilisateur():
    test1 = admin.Administrateur()
    test1.ajouter_utilisateur("niahniah", "azerty", "ESTIENNE", "Clément", "niah-niah@hotmail.fr")
    #On ouvre le fichier login afin de vérifier qu'il y a bien le login & le mdp
    fichierLogin = open("login.txt", "r")
    ligne = fichierLogin.read().splitlines()
    assert ligne[-1] == "niahniah;azerty" #Assert : bloquant si ça passe pas.
    print("Test ajouter utilisateur : OK")
    #On regarde dans l'arborescence si il y a bien l'annuaire de ESTIENNE Clément qui est crée.
    
def appeler_tests():
    test_ajouter_utilisateur() #Ajouter paramètre afin de vérifier pour n'importe quel nom ? 
    
appeler_tests()