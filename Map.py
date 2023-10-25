from Graphe import Graphe
from Destinations import Destination, Itineraire


class Map:

    def __init__(self):
        self.map = Graphe()
        self.destination_pull = [
        Destination(self.map.nodes["Vancouver"], self.map.nodes["Edimburgh"], 13),
        Destination(self.map.nodes["Rio de Janeiro"], self.map.nodes["Hamburg"], 18),
        Destination(self.map.nodes["Casablanca"], self.map.nodes["Honolulu"], 16),
        Destination(self.map.nodes["Edimburgh"], self.map.nodes["Hong Kong"], 17),
        Destination(self.map.nodes["Hong Kong"], self.map.nodes["Jakarta"], 5),
        Destination(self.map.nodes["Bangkok"], self.map.nodes["Tokyo"], 6),
        Destination(self.map.nodes["Tokyo"], self.map.nodes["Sydney"], 11),
        Destination(self.map.nodes["Marseille"], self.map.nodes["Christchurch"], 23),
        Destination(self.map.nodes["Buenos Aires"], self.map.nodes["Marseille"], 18),
        Destination(self.map.nodes["Marseille"], self.map.nodes["Jakarta"], 18),
        Destination(self.map.nodes["Rio de Janeiro"], self.map.nodes["Tokyo"], 20),
        Destination(self.map.nodes["Los Angeles"], self.map.nodes["Hamburg"], 14),
        Destination(self.map.nodes["Athina"], self.map.nodes["Manila"], 14),
        Destination(self.map.nodes["Lagos"], self.map.nodes["Tehran"], 10),
        Destination(self.map.nodes["Al-Qahira"], self.map.nodes["Sydney"], 19),
        Destination(self.map.nodes["Winnipeg"], self.map.nodes["Perth"], 14),
        Itineraire(self.map.nodes["Casablanca"], self.map.nodes["Tehran"], 9, [self.map.nodes["Casablanca"], self.map.nodes["Al-Qahira"], self.map.nodes["Tehran"]], 6, 15),
        Destination(self.map.nodes["Lagos"], self.map.nodes["Lahore"], 7),
        Destination(self.map.nodes["Edimburgh"], self.map.nodes["Luanda"], 10),
        Destination(self.map.nodes["Lagos"], self.map.nodes["Hong Kong"], 14),
        Itineraire(
            self.map.nodes["Lagos"], self.map.nodes["Djibouti"], 9,
            [self.map.nodes["Lagos"], self.map.nodes["Luanda"], self.map.nodes["Dar es Salaam"], self.map.nodes["Djibouti"]], 6, 15
        ),
        Destination(self.map.nodes["Caracas"], self.map.nodes["Al-Qahira"], 13),
        Destination(self.map.nodes["Valparaiso"], self.map.nodes["Rio de Janeiro"], 6),
        Destination(self.map.nodes["Buenos Aires"], self.map.nodes["Manila"], 17),
        Destination(self.map.nodes["Buenos Aires"], self.map.nodes["Sydney"], 13),
        Itineraire(
            self.map.nodes["Manila"], self.map.nodes["Darwin"], 13,
            [self.map.nodes["Manila"], self.map.nodes["Honolulu"], self.map.nodes["Port Moresby"], self.map.nodes["Darwin"]], 9, 19
        ),
        Destination(self.map.nodes["Moskva"], self.map.nodes["Petropavlovsk"], 15),
        Destination(self.map.nodes["New York"], self.map.nodes["Cape Town"], 19),
        Destination(self.map.nodes["Casablanca"], self.map.nodes["Yakutsk"], 16),
        Destination(self.map.nodes["Dar es Salaam"], self.map.nodes["Tokyo"], 15),
        Destination(self.map.nodes["Los Angeles"], self.map.nodes["Dar es Salaam"], 17),
        Destination(self.map.nodes["Hamburg"], self.map.nodes["Beijing"], 13),
        Destination(self.map.nodes["Edimburgh"], self.map.nodes["Tokyo"], 22),
        Destination(self.map.nodes["Novosibirsk"], self.map.nodes["Darwin"], 23),
        Itineraire(
            self.map.nodes["Anchorage"], self.map.nodes["Tiksi"], 34,
            [self.map.nodes["Anchorage"], self.map.nodes["Cambridge Bay"], self.map.nodes["Reykjavik"], self.map.nodes["Murmansk"], self.map.nodes["Tiksi"]], 23, 40
        ),
        Destination(self.map.nodes["Cape Town"], self.map.nodes["Jakarta"], 13),
        Destination(self.map.nodes["Reykjavik"], self.map.nodes["Mumbai"], 13),
        Destination(self.map.nodes["Mexico"], self.map.nodes["Beijing"], 13),
        Destination(self.map.nodes["Mumbai"], self.map.nodes["Beijing"], 6),
        Destination(self.map.nodes["Moskva"], self.map.nodes["Hong Kong"], 13),
        Destination(self.map.nodes["Moskva"], self.map.nodes["Toamasina"], 11),
        Destination(self.map.nodes["New York"], self.map.nodes["Tokyo"], 15),
        Destination(self.map.nodes["Los Angeles"], self.map.nodes["Jakarta"], 11),
        Destination(self.map.nodes["Hamburg"], self.map.nodes["Dar es Salaam"], 8),
        Destination(self.map.nodes["Rio de Janeiro"], self.map.nodes["Perth"], 17),
        Destination(self.map.nodes["Caracas"], self.map.nodes["Athina"], 12),
        Itineraire(
            self.map.nodes["Murmansk"], self.map.nodes["Petropavlovsk"], 30,
            [self.map.nodes["Murmansk"], self.map.nodes["Tiksi"], self.map.nodes["Novosibirsk"], self.map.nodes["Yakutsk"], self.map.nodes["Petropavlovsk"]], 20, 36
        ),
        Destination(self.map.nodes["Miami"], self.map.nodes["Moskva"], 13),
        Destination(self.map.nodes["Rio de Janeiro"], self.map.nodes["Dar es Salaam"], 11),
        Destination(self.map.nodes["New York"], self.map.nodes["Marseille"], 10),
        Itineraire(
            self.map.nodes["Tehran"], self.map.nodes["Bangkok"], 13,
            [self.map.nodes["Tehran"], self.map.nodes["Lahore"], self.map.nodes["Mumbai"], self.map.nodes["Bangkok"]], 9, 19
        ),
        Destination(self.map.nodes["New York"], self.map.nodes["Mumbai"], 19),
        Destination(self.map.nodes["Mexico"], self.map.nodes["Mumbai"], 15),
        Destination(self.map.nodes["New York"], self.map.nodes["Sydney"], 17),
        Destination(self.map.nodes["Lima"], self.map.nodes["Jakarta"], 14),
        Destination(self.map.nodes["Los Angeles"], self.map.nodes["Rio de Janeiro"], 15),
        Destination(self.map.nodes["Marseille"], self.map.nodes["Beijing"], 14),
        Itineraire(
            self.map.nodes["Mexico"], self.map.nodes["Valparaiso"], 15,
            [self.map.nodes["Mexico"], self.map.nodes["Caracas"], self.map.nodes["Lima"], self.map.nodes["Valparaiso"]], 10, 21
        ),
        Destination(self.map.nodes["Marseille"], self.map.nodes["Al-Qahira"], 5),
        Destination(self.map.nodes["Miami"], self.map.nodes["Buenos Aires"], 9),
        Destination(self.map.nodes["Mexico"], self.map.nodes["New York"], 13),
        Destination(self.map.nodes["Vancouver"], self.map.nodes["Miami"], 9),
        Destination(self.map.nodes["Jakarta"], self.map.nodes["Sydney"], 7),
        Itineraire(
            self.map.nodes["Anchorage"], self.map.nodes["Cambridge Bay"], 18,
            [self.map.nodes["Anchorage"], self.map.nodes["Vancouver"], self.map.nodes["Winnipeg"], self.map.nodes["Cambridge Bay"]], 12, 24
        ),
        Destination(self.map.nodes["Edimburgh"], self.map.nodes["Sydney"], 25)
    ]
        

    def affiche_plateau(self):
        for el in self.destination_pull:
            ch = ""
            if el.get_type() == 0:  #0 if destination
                ch += "Trajet de " + el.get_depart().get_nom() + " à " + el.get_arrivee().get_nom() + "\n"
                ch += "Si le trajet est réussi il vaudra " + str(el.get_points()) + " sinon les points seront retirés" + "\n"
            else:   #if itinerary
                ch += "L'ordre doit être : "
                for el2 in el.get_ordre():
                    ch += el2.get_nom() + " "
                ch += "\n"
                ch += "Si les villes sont reliées sans l'ordre, l'itinéraire vaudra " + str(el.get_sous_points()) + "\n"
                ch += "Si l'ordre est respecté, l'itinéraire vaudra " + str(el.get_points()) + "\n"
                ch += "Sinon, " + str(el.get_malus()) + " seront enlevés"
            print(ch)


    def affichage_toutes_les_villes(self):
        for ville in self.map.nodes:
            print("- " + self.map.nodes[ville].get_nom() + " ("+ self.map.nodes[ville].get_type()+")")

    def affichage_destination_ville(self, ville):
        if self.verification_ville(ville) == 1: return 1

        for destination in self.destination_pull:
            ch = ""
            if destination.get_depart().get_nom() == ville or destination.get_arrivee().get_nom() == ville:
                if destination.get_type() == 0:  #0 if destination
                    ch += "Trajet de " + destination.get_depart().get_nom() + " à " + destination.get_arrivee().get_nom() + "\n"
                    ch += "Si le trajet est réussi il vaudra " + str(destination.get_points()) + " sinon les points seront retirés" + "\n"
                else:   #if itinerary
                    ch += "L'ordre doit être : "
                    for el2 in destination.get_ordre():
                        ch += el2.get_nom() + " "
                    ch += "\n"
                    ch += "Si les villes sont reliées sans l'ordre, l'itinéraire vaudra " + str(destination.get_sous_points()) + "\n"
                    ch += "Si l'ordre est respecté, l'itinéraire vaudra " + str(destination.get_points()) + "\n"
                    ch += "Sinon, " + str(destination.get_malus()) + " seront enlevés\n"
                print(ch)


    def verification_ville(self, ville):
        if ville not in self.map.nodes:
            print("Ville inconnue")
            return 1
        

    def verification_destination(self, ville1, ville2):
        for dest in self.destination_pull:
            if dest.get_depart().get_nom() == ville1 and dest.get_arrivee().get_nom() == ville2 or dest.get_depart().get_nom() == ville2 and dest.get_arrivee().get_nom() == ville1:
                return dest
        print("Destination inexistante")
        print("Annulation de l'opération, entrer une destination")
        return 1
    

    def plus_court_chemin(self, depart, arrivee, chemins_uti_list):
        return self.map.dijkstra(depart, arrivee, chemins_uti_list)
    

    def verification_chemin(self, depart, arrivee, chemins_uti_list):
        return self.map.verification_arete(depart, arrivee, chemins_uti_list)
