from Map import Map

map = Map()

test = True

def affichage_choix():
    print("--------------------------")
    print("0 - Quitter")
    print("1 - Voir tout le plateau")
    print("2 - Voir toutes les cartes destinations en rapport avec une ville")
    print("3 - Entrer des destinations")
    print("4 - Trouver le meilleur chemin pour une destination")
    print("5 - Modification de la carte")
    print("--------------------------")

if __name__ == "__main__":
    ### initialisation ###
    print("Initialisation...")
    map = Map()
    destinations_list = []
    chemins_uti_list = []
    print(("Initialisation terminée..."))
    ### fin initialisation ###

    choix = -1

    while choix != 0:

        ### actions possibles ###
        affichage_choix()
        choix = int(input("Choix : "))
        while choix not in [0, 1, 2, 3, 4, 5]:
            affichage_choix()
            choix = int(input("Choix : "))

        ### ferme l'appli ###
        if choix == 0:
            print("Merci, au revoir")

        ### affiche tout le plateau ###
        if choix == 1:
            map.affiche_plateau()


        ### affiche toutes les destinations d'une ville ###
        elif choix == 2:
            print("Liste de toutes les villes :")
            map.affichage_toutes_les_villes()
            ville = input("Ville : ")
            while map.affichage_destination_ville(ville) == 1:
                ville = input("Ville : ")

        ### entrer les destinations ###
        elif choix == 3:
            continuer = "o"
            while continuer == "o":
                print("-- Nouvelle destination --")
                depart = input("Depart : ")
                while map.verification_ville(depart):
                    depart = input("Depart : ")
                arrivee = input("Arrivee : ")
                while map.verification_ville(arrivee):
                    arrivee = input("Arrivee : ")
                
                confirmation = input("Confirmer la destination " + depart + " - " + arrivee + " ?(o/n) : ")
                if confirmation == "o":
                    verif_dest = map.verification_destination(depart, arrivee)
                    if verif_dest != 1:
                        destinations_list.append(verif_dest)
                    else:
                        print("Chemin inconnu, abandon")
                print(destinations_list)
                continuer = input("Entrer une nouvelle destination ? (o/n) : ")

        ### calcul du meilleur chemin ###
        # meilleur chemin : le moins de wagon utilisés (à modifier dans le futur ?)
        elif choix == 4:
            if test and len(destinations_list) == 0:
                destinations_list = [map.verification_destination("Moskva", "Hong Kong")]
                print("Lancement du test")
                print("Destination utilisée : Moskva - Hong Kong")
            if len(destinations_list) == 0:
                print("Aucune destination saisie...")
                print("Vous devez entrer au moins une destination !")
            else:
                print("--------------------------")
                for dest in destinations_list:
                    depart = dest.get_depart().get_nom()
                    arrivee = dest.get_arrivee().get_nom()
                    chemin = map.plus_court_chemin(depart, arrivee, chemins_uti_list)
                    ch = "Chemin à suivre pour " + depart + " - " + arrivee + " : " + "\n"
                    for ville in chemin:
                        ch += ville + " - "
                    print(ch[:-2] + "\n")
                print("--------------------------")
    

        ### modification de la carte ###
        elif choix == 5:
            print("Des chemins ont été pris ? Pas de soucis, écrivez les chemins utilisés")
            print("N'oubliez pas de relancer le calcul de meilleur chemin")
            continuer = "o"
            while continuer == "o":
                print("-- Chemin pris --")
                depart = input("Depart : ")
                while map.verification_ville(depart):
                    depart = input("Depart : ")
                arrivee = input("Arrivee : ")
                while map.verification_ville(arrivee):
                    arrivee = input("Arrivee : ")
                
                confirmation = input("Confirmer le chemin " + depart + " - " + arrivee + " ?(o/n) : ")
                if confirmation == "o":
                    verif_chemin = map.verification_chemin(depart, arrivee, chemins_uti_list)
                    if verif_chemin != 1:
                        chemins_uti_list.append(verif_chemin)
                    else:
                        print("Chemin inconnu, abandon")
                print(chemins_uti_list)
                continuer = input("Entrer une nouvelle destination ? (o/n) : ")
