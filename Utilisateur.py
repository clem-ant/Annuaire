class Utilisateur:

    def __init__(self, nom, prenom, email, num_port = "", adresse_postale =""):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.num_port = num_port
        self.adresse_postale = adresse_postale

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_email(self):
        return self.email

    def get_num_port(self):
        return self.num_port

    def get_adresse_postale(self):
        return self.adresse_postale