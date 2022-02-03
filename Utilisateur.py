class Utilisateur:

    def ajouter_contact(self, login, donnees):
        nom_annuaire = login+"_LDAP.csv"
        droit =  self.get_autorisation(login, nom_annuaire)
        annuaire = open(login+"_LDAP.csv")
        LAnnuaire = annuaire.read().splitlines()
        if(droit == 2 and donnees not in LAnnuaire):
            fichierContact = open(nom_annuaire, "a")
            fichierContact.write(donnees + "\n")
            fichierContact.close()
            return 8
        else:
            print("Vous avez déjà ce contact dans votre Annuaire")
            return 9
        
    def get_autorisation(self, login, nom_annuaire):
        f = open('authorisation.txt', 'r')
        fi= f.read().splitlines()
        # print("test")
        droit = 0
        for ligne in fi :
            ligne1 = ligne.split(";")
            if (login == ligne1[0] and nom_annuaire == ligne1[2]) :
                login, droit, nom_annuaire = ligne.split(";")
                # print(droit)
                break
        f.close()    
        return int(droit) #Int car de base les choses lu dans un fichier sont en string mais la on sait que ce sera forcément des int
        #TODO il manque soit un return soit il manque de fermer le fichier AVANT de return le droit sur la ligne juste au dessus
        
    def search_contact(self,login, mdp, donnees):
        tab = [2]
        tab = donnees.split(";")
    
        nom_annuaire = tab[0] + "_LDAP.csv"
        print(nom_annuaire)
        droit = self.get_autorisation(login, nom_annuaire)
        boolean = False
        if(droit >= 1):
            fichier = open(nom_annuaire, "r")
            for ligne in fichier:
                if (tab[1] in ligne):
                    code_erreur = 00
                    resultat = []
                    resultat = ligne.split(";")
                    resultat = ' '.join(resultat)
                    print(f"Résultat : {resultat}")
                    boolean = True
    
            if(boolean == False):
                print("Contact non trouvé")
                code_erreur= 12
                return code_erreur  
            fichier.close()
        else:
            print("Vous n'avez pas les droit de rechercher un contact")
        
