from imghdr import tests
import Administrateur as admin
import Utilisateur as user
import os, sys, string, random

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def test_ajouter_utilisateur(loginRandom, charrandom):
    test1 = admin.Administrateur()
    test1.ajouter_utilisateur(loginRandom, charrandom)
    fichierLogin = open("login.txt", "r")
    ligne = fichierLogin.read().splitlines()
    
    #On ouvre le fichier login afin de vérifier qu'il y a bien le login & le mdp
    assert ligne[-1] == loginRandom+";"+charrandom, bcolors.WARNING+ "La dernière ligne du fichier login.txt n'est pas celle qui a été demandé" + bcolors.ENDC #Assert : bloquant si ça passe pas
    
    
    #On regarde dans l'arborescence si il y a bien l'annuaire du loginRandom qui est crée.
    dir = os.listdir()
    assert loginRandom+"_LDAP.csv" in dir,  bcolors.WARNING+"Il n'y a pas eu création de l'annuaire dans l'arboressence"+bcolors.ENDC
    
    
    #On regarde dans le fichier authorisation.txt si il y a bien écrit la ligne qui dit que la personne a comme droit 2 dans ce même fichier
    fichierAuth = open("authorisation.txt", "r")
    fLigneAuth = fichierAuth.read().splitlines()
    assert fLigneAuth[-1] == loginRandom+";2;"+loginRandom+"_LDAP.csv"

    fichierAuth.close()
    fichierLogin.close()
    print(bcolors.OKGREEN + "Test ajouter utilisateur : "+bcolors.BOLD+"OK"+ bcolors.ENDC)
    
    
def test_ajouter_contact(loginRandom):
    testAddC = user.Utilisateur()    
    blockPrint() #Permet de mute les prints de la fonction ajouter contact juste pour ces tests
    assert testAddC.ajouter_contact(loginRandom,"DUGUAIT_Nicolas;nicolas.duguait@hotmail.fr;0624522323;2 rue de la gare, Toulouse, 31400")==8,  bcolors.WARNING+ "Problème lors de l'ajout d'un premier contact" + bcolors.ENDC
    assert testAddC.ajouter_contact(loginRandom,"DUGUAIT_Nicolas;nicolas.duguait@hotmail.fr;0624522323;2 rue de la gare, Toulouse, 31400")==9,  bcolors.WARNING+ "Problème lors de l'ajout d'un contact déjà dans l'annuaire" +bcolors.ENDC
    enablePrint() #Permet de réactiver les prints
    
    #On vérifie que la ligne a été écrite dans l'annuaire de la personne
    fichier = open(loginRandom+"_LDAP.csv", "r") 
    contenu = fichier.read().splitlines()
    assert contenu[0] == "DUGUAIT_Nicolas;nicolas.duguait@hotmail.fr;0624522323;2 rue de la gare, Toulouse, 31400", "Les données n'ont pas été écrites"
    
    print(bcolors.OKGREEN + "Test ajouter contact : "+bcolors.BOLD+"OK"+ bcolors.ENDC)
    
def test_get_authorisation(loginRandom):
    testGetAuth = user.Utilisateur()
    assert testGetAuth.get_autorisation(loginRandom, loginRandom+"_LDAP.csv") == 2,  bcolors.WARNING+ "Lors de la création du compte de l'utilisateur, il n'y a pas automatiquement la création de son autorisation dans le fichier authorisation.txt" + bcolors.ENDC
    assert testGetAuth.get_autorisation("test", "test_LDAP.csv") == 0, "Une personne qui n'est pas dans l'annuaire n'a pas une authorisation != 0"
    assert testGetAuth.get_autorisation("mathias", "nicoco_LDAP.csv") == 1, "Problème lors de l'autorisation == 1"
    assert testGetAuth.get_autorisation("sebb", "niahniah_LDAP.csv") == 0, "Problème lors de l'autorisation == 0"
    assert testGetAuth.get_autorisation("pas_dedans", "niahniah_LDAP.csv") == 0, "Une personne pas dedans ne peut pas avoir d'autorisation"
    print(bcolors.OKGREEN + "Test get authorisation : "+bcolors.BOLD+"OK"+ bcolors.ENDC)
    
def test_search_contact(loginRandom, charrandom):
    testSearchUser = user.Utilisateur()
    
    blockPrint() #Permet de mute les prints de la fonction ajouter contact juste pour ces tests
    assert testSearchUser.search_contact(loginRandom, charrandom, loginRandom+";DUGUAIT") == "DUGUAIT_Nicolas nicolas.duguait@hotmail.fr 0624522323 2 rue de la gare, Toulouse, 31400", "L'utilisateur DUGUAIT est dans l'annuaire"
    assert testSearchUser.search_contact(loginRandom, charrandom, loginRandom+";Inconnu") == 12, "L'utilisateur n'est pas dedans"
    assert testSearchUser.search_contact("sebb", "", "niahniah") == 11, "L'utilisateur sebb n'a pas les droits"
    enablePrint() #Permet de réactiver les prints
    print(bcolors.OKGREEN + "Test search_contact : "+bcolors.BOLD+"OK"+ bcolors.ENDC)
    
def appeler_tests(): #test
    print(bcolors.HEADER + "Début des tests" + bcolors.ENDC)
    charrandom = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    loginRandom = "TEST"+charrandom
    
    test_ajouter_utilisateur(loginRandom, charrandom)
    test_ajouter_contact(loginRandom)
    test_get_authorisation(loginRandom)
    test_search_contact(loginRandom, charrandom)
    os.remove(loginRandom+"_LDAP.csv")
    
    fichierLogin = open("login.txt", "r")
    ligne = fichierLogin.read().splitlines()
    fichierLogin.close()
    fichierLogin = open("login.txt", "w")
    for i in range(len(ligne)-1): #réécrit le fichier sans la dernière ligne déjà crée
        fichierLogin.write(ligne[i]+"\n")
    fichierLogin.close()
    
    fichierAuth = open("authorisation.txt", "r")
    fLigneAuth = fichierAuth.read().splitlines()
    fichierAuth.close()
    fichierAuth = open("authorisation.txt", "w")
    for i in range(len(fLigneAuth)-1): #réécrit le fichier sans la dernière ligne déjà crée
        fichierAuth.write(fLigneAuth[i]+"\n")
    fichierAuth.close()
    print(bcolors.HEADER+"Tous les tests sont passés\nLes lignes dans les fichiers supprimés\nLes annuaires crées pendant les tests supprimé"+bcolors.ENDC)
    
appeler_tests()
