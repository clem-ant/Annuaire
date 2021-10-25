class Utilisateur:
    #TODO se connecter au serveur

    def __init__(self, nom, prenom, email, num_port = "", adresse_postale =""):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.num_port = num_port
        self.adresse_postale = adresse_postale
        self.contact = "contact_"+nom+"_"+prenom+".csv"
        

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom
        
    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_num_port(self):
        return self.num_port

    def set_num_port(self, num_port):
        self.num_port = num_port

    def get_adresse_postale(self):
        return self.adresse_postale

    def set_adresse_postale(self, adresse_postale):
        self.adresse_postale = adresse_postale
    
    def verifier_si_unique(self, nom, prenom, email):
        fichierContact = open(self.contact, "r")
        contact = fichierContact.read().splitlines()
        for cont in contact:
            splited = cont.split(",")
            if(splited[0] == nom and splited[1] == prenom and splited[2] == email):
                return False
        return True
    
    def ajouter_contact(self, nom, prenom, email, num_port = "", adresse_postale = ""):
        fichierContact = open(self.contact, "r")
        contact = fichierContact.read().splitlines()
        for cont in contact:
            splited = cont.split(",")
            if(splited[0] == nom and splited[1] == prenom and splited[2] == email):
                print("L'utilisateur est déjà dans votre Annuaire")
                return
        fichierContact = open(self.contact, "a")
        fichierContact.write(nom+","+prenom +","+ email +","+ num_port + "," + adresse_postale + "\n")
        fichierContact.close()

    def retirer_contact(self, nom, prenom, num_port= ""):
        fichierContact = open(self.contact, "r")
        infos = fichierContact.read().splitlines()
        new_file = open(self.contact, "w")
        if(len(infos) == 0):
            print("Il n'y a personne dans votre Annuaire, vous ne pouvez donc pas en supprimer")
            return
        if num_port != "":
            for info in infos:
                splited = info.split(",")
                if splited[0] != nom and splited[1] != prenom:
                    new_file.write(info + "\n")
        else:
            for info in infos:
                splited = info.split(",")
                if splited[0] != nom and splited[1] != prenom:
                    new_file.write(info + "\n")