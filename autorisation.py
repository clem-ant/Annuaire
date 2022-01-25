from os import lseek


'''Fonction get_autorisation(E : login : chaîne de caractères, E : nom_annuaire): entier
/*chercher les droits d’un utilisateur sur un annuaire*/
Variables
Début
	autorisation=0
	OUVRIR(autorisation.txt)
Tant que LIRE_LIGNES(autorisation.txt) :
Si (LIGNE.contient(login)) ET (LIGNE.contient(nom annuaire)) Alors : /*Vérifie que le login a bien une autorisation sur le nom de l’annuaire*/ 
		autorisation=LIGNE[2]  /* affecte l’autorisation donnée dans le fichier
	Fin tant que
FERMER(autorisation.txt)
retourne autorisation		
Fin
'''

def get_autorisation(login, nom_annuaire):
        f = open('authorisation.txt', 'r')
        fi= f.read().splitlines()
        # print("test")
        # print(fi)

        for ligne in fi :
        #     print(login, fi[0])
        #     print(login in fi)
            if (login in fi[0] and nom_annuaire in fi[0]) :
                login, droit, nom_annuaire = ligne.split(";")
                # print(droit)
                break

        f.close()
        return droit

get_autorisation("cmathias","cmathias_LDAP.csv")

            



