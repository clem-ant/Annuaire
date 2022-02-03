class Administrateur:


    def ajouter_utilisateur(self, login, mdp):
        fichierLogin = open("login.txt", "r")
        contacts = fichierLogin.read().splitlines()        
        for i in range(len(contacts)):
            if(login == contacts[i].split(";")[0]):
                print("Le login est déjà utilisé : " + login)
                return 20
        fichierLogin.close()
        fichierLogin = open("login.txt", "a")
        fichierLogin.write(login+";"+mdp+"\n")
        fichierLogin.close()
        # Utilisateur(nom, prenom, email, num_port, adresse_postale) #Création de l'utilisateur directement dans le constructeur
        fichierAutho = open("authorisation.txt", "a")
        fichierAutho.write(login+";2;"+login+"_LDAP.csv"+"\n")
        fichierAutho.close()
        
        fichierLDAP = open(login+"_LDAP.csv", "w+")
        fichierLDAP.close()
        return 3
        