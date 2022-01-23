import Administrateur as admin
import Utilisateur as user


administrateur = admin.Administrateur()
clement = user.Utilisateur()
administrateur.ajouter_utilisateur("niahniah", "azerty","ESTIENNE", "Clément", "niah-niah@hotmail.fr")
administrateur.ajouter_utilisateur("nicoco", "qwerty","DUGUAIT", "Nicolas", "nicolas.duguait@hotmail.fr", "0624522323", "2 rue de la gare, Toulouse, 31400")
clement.ajouter_contact("niahniah","DUGUAIT_Nicolas;nicolas.duguait@hotmail.fr;0624522323;2 rue de la gare, Toulouse, 31400")
# administrateur.supprimer_utilisateur("DUGUAIT", "Nicolas")
# #administrateur.modifier_utilisateur("ESTIENNE", "Clément")
# #administrateur.modifier_utilisateur("NonDansLaListe", "TEST")

# administrateur.afficher_utilisateur_list() #Liste a envoyer sur le serveur

# clement = user.Utilisateur("PAYET", "Clément", "clemant@test.fr", "0769959222", "4 rue elvire")
# clement.ajouter_contact("Estienne", "Clement", "niah-niah@hotmail.fr", "0123456789", "test rue 3")
# clement.ajouter_contact("Cuvelier", "Mathias", "matoumatou@gmail.com", "1234567489")
# clement.ajouter_contact("Lacombe", "Sebastien", "homme@sportif.fr", "118218", "Loin")
# clement.ajouter_contact("Deconinck", "Lucas", "Lucas.deconinck@univ-tlse3.fr", "", "Proche")

# #clement.retirer_contact("Cuvelier", "Mathias")
# clement.retirer_contact("Deconinck", "Lucas")
# #clement.modifier_contact("Lacombe", "Sebastien", "homme@sportif.fr")
# clement.afficher_contact_list()
