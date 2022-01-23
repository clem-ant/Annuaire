class Utilisateur:
    # #TODO se connecter au serveur

    # def __init__(self, nom, prenom, email, num_port = "", adresse_postale =""):
    #     self.nom = nom
    #     self.prenom = prenom
    #     self.email = email
    #     self.num_port = num_port
    #     self.adresse_postale = adresse_postale
    #     self.contact = nom+"_"+prenom+"_LDAP"+".csv"
    #     tmp = open(self.contact, "a")
    #     tmp.close()
        
    # def get_nom(self):
    #     return self.nom

    # def set_nom(self, nom):
    #     self.nom = nom
        
    # def get_prenom(self):
    #     return self.prenom

    # def set_prenom(self, prenom):
    #     self.prenom = prenom

    # def get_email(self):
    #     return self.email

    # def set_email(self, email):
    #     self.email = email

    # def get_num_port(self):
    #     return self.num_port

    # def set_num_port(self, num_port):
    #     self.num_port = num_port

    # def get_adresse_postale(self):
    #     return self.adresse_postale

    # def set_adresse_postale(self, adresse_postale):
    #     self.adresse_postale = adresse_postale
    
    # def afficher_contact_list(self):
    #     print("~~~~~ Affichage des contacts de " + self.nom + " " + self.prenom + " ~~~~~")
    #     fichierContact = open(self.contact, "r")
    #     contacts = fichierContact.read().splitlines()
    #     for contact in range(len(contacts)):
    #         print(contacts[contact])
    #     fichierContact.close()

    # def verifier_si_unique(self, nom, prenom, email):
    #     fichierContact = open(self.contact, "r")
    #     contact = fichierContact.read().splitlines()
    #     for cont in contact:
    #         splited = cont.split(",")
    #         if(splited[0] == nom and splited[1] == prenom and splited[2] == email):
    #             return False
    #     return True
    
    # def verifier_si_existant(self, nom, prenom, email): #Retourne True si il existe
    #     fichierContact = open(self.contact, "r")
    #     contact = fichierContact.read().splitlines()
    #     fichierContact.close()
    #     for cont in contact:
    #         splited = cont.split(",")
    #         if(splited[0] == nom and splited[1] == prenom and splited[2] == email):
    #             return True
    #     return False

    def ajouter_contact(self, login, donnees):
        # if(self.verifier_si_existant(nom, prenom, email) == False): #Donc si il existe pas
        nom_annuaire = donnees.split(";")[0]+"_LDAP.csv"
        # droit = get_authorisation(login, nom_annuaire)
        droit = 2
        if(droit == 2):
            print(nom_annuaire)
            fichierContact = open(nom_annuaire, "a")
            fichierContact.write(donnees + "\n")
            fichierContact.close()
            return 8
        else:
            print("Vous avez déjà ce contact dans votre Annuaire")
            return 9

    # def trouver_indice_contact(self, nom, prenom, email):
    #     fichierContact = open(self.contact, "r")
    #     infos = fichierContact.read().splitlines()
    #     fichierContact.close()
    #     compteur = 0 
    #     for inf in infos:
    #         splited = inf.split(",")
    #         print(splited[0])
    #         if(splited[0] == nom and splited[1] == prenom and splited[2] == email):
    #             return compteur
    #         compteur += 1
    #     return compteur

    # def modifier_contact(self, nom, prenom, email): #On peut check si c'est un mail
    #     if(self.verifier_si_existant(nom, prenom, email)):
    #         pass
    #     else:
    #         print("Vous essayez de modifier un contact non existant")
    #         return
    #     fichierContact = open(self.contact, "r")
    #     contacts = fichierContact.read().splitlines()
    #     fichierContact.close()
    #     indice_contact = self.trouver_indice_contact(nom, prenom, email)
    #     while True:
    #         print("Quel élément voulez vous changer : ")
    #         index_changement = int(input("[1] Nom\n[2] Prenom\n[3] Email\n[4] Numéro de Portable\n[5] Adresse Postale\n"))
    #         if(index_changement > 0 or index_changement <= 5):
    #             break
    #     valeur_a_mettre = input("Par quoi voulez vous le remplacer ?\n")
    #     tmp = contacts[int(indice_contact)]
    #     new_contact = tmp.split(",")
    #     self.retirer_contact(nom, prenom) #Grâce à la condition du début on sait que c'est vrai.
    #     new_contact[index_changement-1] = valeur_a_mettre
    #     self.ajouter_contact(new_contact[0], new_contact[1], new_contact[2], new_contact[3], new_contact[4])


    # def retirer_contact(self, nom, prenom, num_port= ""): #Prendre l'email ? Au cas ou doublons ?
    #     fichierContact = open(self.contact, "r")
    #     infos = fichierContact.read().splitlines()
    #     new_file = open(self.contact, "w")

    #     if(len(infos) == 0):
    #         print("Il n'y a personne dans votre Annuaire, vous ne pouvez donc pas en supprimer")
    #         return
    #     if num_port != "":
    #         for info in infos:
    #             splited = info.split(",")
    #             if splited[0] != nom and splited[1] != prenom:
    #                 new_file.write(info + "\n")
    #     else:
    #         for info in infos:
    #             splited = info.split(",")
    #             if splited[0] != nom and splited[1] != prenom:
    #                 new_file.write(info + "\n")
    #     fichierContact.close()
    #     new_file.close()