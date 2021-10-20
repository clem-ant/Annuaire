from Utilisateur import Utilisateur
#: le nom, le prénom, le numéro de téléphone portable, l’adresse postale, l’adresse
#mail. Les champs nom, prénom et adresse mail sont obligatoires.
class Administrateur:
    utilisateur = []
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.utilisateur = []

    def afficher_utilisateur_list(self):
        for user in self.utilisateur:
            print("Nom : " + user.get_nom())
            print("Prenom : " + user.get_prenom())
            print("Email : " + user.get_email())
            print("Numéro de portable : " + str(user.get_num_port()))
            print("Adresse postale : " + user.get_adresse_postale())
            print("\n")

    def ajouter_utilisateur(self, nom, prenom, email, num_port = "", adresse_postale = ""):
        self.utilisateur.append(Utilisateur(nom, prenom, email, num_port, adresse_postale))
    
    def supprimer_utilisateur(self, nom, prenom, num_port = ""):
        if num_port != "": #On priorise si il existe un numero de telephone c'est plus simple
            for user in range(len(self.utilisateur)):
                if(self.utilisateur[user].get_num_port() != "" and self.utilisateur[user].get_num_port() == num_port):
                    self.utilisateur.pop(user)
        else:
            for user in range(len(self.utilisateur)):
                if(self.utilisateur[user].get_nom() == nom and self.utilisateur[user].get_prenom() == prenom):
                    self.utilisateur.pop(user)
                else:
                    print("On ne trouve pas l'utilisateur")

    def modifier_utilisateur(self, nom, prenom, index_changement, valeur_a_mettre, num_port = ""):
        if num_port != "":
            for user in range(len(self.utilisateur)):
                if(self.utilisateur[user].get_num_port() != "" and self.utilisateur[user].get_num_port() == num_port):
                    self.utilisateur[user][index_changement] = valeur_a_mettre
        else:
            for user in range(len(self.utilisateur)):
                if(self.utilisateur[user].get_nom() == nom and self.utilisateur[user].get_prenom() == prenom):
                    self.utilisateur[user][index_changement] = valeur_a_mettre
                else:
                    print("On ne trouve pas l'utilisateur")

def afficher_list(liste):
    print(liste)
    for user in liste:
        user.afficher_informations()

admin = Administrateur("PAYET", "Clément")
admin.ajouter_utilisateur("ESTIENNE", "Clément", "niah-niah@hotmail.fr")
admin.ajouter_utilisateur("DUGUAIT", "Nicolas", "nicolas.duguait@hotmail.fr", "0624522323", "2 rue de la gare, Toulouse, 31400")
admin.afficher_utilisateur_list()
