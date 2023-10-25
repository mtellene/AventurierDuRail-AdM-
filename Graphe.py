from Villes import Ville
from Aretes import Arete, PassageDifficile

class Graphe:

    def __init__(self):
        self.nodes = {
            "Cambridge Bay": Ville("Cambridge Bay", "port"),
            "Vancouver": Ville("Vancouver", "port"),
            "Winnipeg": Ville("Winnipeg", "gare"),
            "Los Angeles": Ville("Los Angeles", "port"),
            "New York": Ville("New York", "port"),
            "Miami": Ville("Miami", "port"),
            "Mexico": Ville("Mexico", "gare"),
            "Caracas": Ville("Caracas", "port"),
            "Lima": Ville("Lima", "port"),
            "Rio de Janeiro": Ville("Rio de Janeiro", "port"),
            "Valparaiso": Ville("Valparaiso", "port"),
            "Buenos Aires": Ville("Buenos Aires", "port"), 
            "Reykjavik": Ville("Reykjavik", "port"),
            "Edimburgh": Ville("Edimburgh", "port"),
            "Murmansk": Ville("Murmansk", "port"),
            "Hamburg": Ville("Hamburg", "port"),
            "Marseille": Ville("Marseille", "port"), 
            "Athina": Ville("Athina", "port"),
            "Casablanca": Ville("Casablanca", "port"),
            "Al-Qahira": Ville("Al-Qahira", "port"),
            "Djibouti": Ville("Djibouti", "gare"),
            "Lagos": Ville("Lagos", "port"),
            "Dar es Salaam": Ville("Dar es Salaam", "port"),
            "Luanda": Ville("Luanda", "port"),
            "Toamasina": Ville("Toamasina", "port"),
            "Cape Town": Ville("Cape Town", "port"),
            "Moskva": Ville("Moskva", "gare"),
            "Tehran": Ville("Tehran", "gare"),
            "Novosibirsk": Ville("Novosibirsk", "gare"),
            "Tiksi": Ville("Tiksi", "port"),
            "Lahore": Ville("Lahore", "gare"),
            "Mumbai": Ville("Mumbai", "port"),
            "Bangkok": Ville("Bangkok", "port"),
            "Hong Kong": Ville("Hong Kong", "port"),
            "Beijing": Ville("Beijing", "port"),
            "Yakutsk": Ville("Yakutsk", "gare"),
            "Petropavlovsk": Ville("Petropavlovsk", "port"),
            "Tokyo": Ville("Tokyo", "port"),
            "Anchorage": Ville("Anchorage", "port"),
            "Manila": Ville("Manila", "port"),
            "Jakarta": Ville("Jakarta", "port"), 
            "Darwin": Ville("Darwin", "port"),
            "Port Moresby": Ville("Port Moresby", "port"),
            "Perth": Ville("Perth", "port"),
            "Sydney": Ville("Sydney", "port"),
            "Christchurch": Ville("Christchurch", "port"),
            "Honolulu": Ville("Honolulu", "port"),
            "None": Ville("None", "None")
        }

        self.edges = [
            Arete("noir", 6, self.nodes["Anchorage"], self.nodes["Cambridge Bay"], "bateau"),
            PassageDifficile(2, self.nodes["Anchorage"], self.nodes["Vancouver"]),
            Arete("noir", 4, self.nodes["Winnipeg"], self.nodes["Cambridge Bay"], "train"),
            Arete("jaune", 2, self.nodes["Vancouver"], self.nodes["Winnipeg"], "train"),
            Arete("rouge", 1, self.nodes["Vancouver"], self.nodes["Los Angeles"], "train"),
            Arete("vert", 1, self.nodes["Vancouver"], self.nodes["Los Angeles"], "train"),
            Arete("blanc", 6, self.nodes["Vancouver"], self.nodes["Tokyo"], "bateau"),
            Arete("blanc", 6, self.nodes["Reykjavik"], self.nodes["Cambridge Bay"], "bateau"),
            Arete("vert", 2, self.nodes["Winnipeg"], self.nodes["New York"], "train"),
            Arete("gris", 3, self.nodes["Winnipeg"], self.nodes["Los Angeles"], "train"),
            Arete("noir", 7, self.nodes["Los Angeles"], self.nodes["Tokyo"], "bateau"),
            Arete("vert", 7, self.nodes["Los Angeles"], self.nodes["Tokyo"], "bateau"),
            Arete("noir", 4, self.nodes["Los Angeles"], self.nodes["New York"], "train"),
            Arete("violet", 4, self.nodes["Los Angeles"], self.nodes["New York"], "train"),
            Arete("jaune", 3, self.nodes["Los Angeles"], self.nodes["Honolulu"], "bateau"),
            Arete("jaune", 2, self.nodes["Los Angeles"], self.nodes["Mexico"], "train"),
            Arete("blanc", 2, self.nodes["Los Angeles"], self.nodes["Mexico"], "train"),
            Arete("jaune", 6, self.nodes["New York"], self.nodes["Reykjavik"], "bateau"),
            Arete("rouge", 7, self.nodes["New York"], self.nodes["Edimburgh"], "bateau"),
            Arete("violet", 7, self.nodes["New York"], self.nodes["Edimburgh"], "bateau"),
            Arete("blanc", 2, self.nodes["New York"], self.nodes["Miami"], "train"),
            Arete("blanc", 2, self.nodes["Miami"], self.nodes["Caracas"], "bateau"),
            Arete("vert", 7, self.nodes["Miami"], self.nodes["Casablanca"], "bateau"),
            Arete("rouge", 3, self.nodes["Mexico"], self.nodes["Caracas"], "train"),
            Arete("violet", 3, self.nodes["Mexico"], self.nodes["Caracas"], "train"),
            Arete("blanc", 2, self.nodes["Caracas"], self.nodes["Lima"], "train"),
            Arete("jaune", 2, self.nodes["Caracas"], self.nodes["Lima"], "train"),
            Arete("gris", 6, self.nodes["Lima"], self.nodes["Honolulu"], "bateau"),
            Arete("rouge", 7, self.nodes["Caracas"], self.nodes["Lagos"], "bateau"),
            Arete("vert", 4, self.nodes["Caracas"], self.nodes["Rio de Janeiro"], "train"),
            Arete("noir", 4, self.nodes["Caracas"], self.nodes["Rio de Janeiro"], "train"),
            Arete("gris", 2, self.nodes["Lima"], self.nodes["Valparaiso"], "train"),
            Arete("gris", 2, self.nodes["Lima"], self.nodes["Valparaiso"], "train"),
            Arete("violet", 8, self.nodes["Lima"], self.nodes["Sydney"], "bateau"),
            Arete("noir", 8, self.nodes["Lima"], self.nodes["Sydney"], "bateau"),
            Arete("jaune", 7, self.nodes["Valparaiso"], self.nodes["Christchurch"], "bateau"),
            Arete("vert", 3, self.nodes["Valparaiso"], self.nodes["Buenos Aires"], "bateau"),
            Arete("blanc", 1, self.nodes["Rio de Janeiro"], self.nodes["Buenos Aires"], "train"),
            Arete("rouge", 1, self.nodes["Rio de Janeiro"], self.nodes["Buenos Aires"], "train"),
            Arete("gris", 6, self.nodes["Rio de Janeiro"], self.nodes["Luanda"], "bateau"),
            Arete("noir", 6, self.nodes["Rio de Janeiro"], self.nodes["Cape Town"], "bateau"),
            Arete("blanc", 6, self.nodes["Rio de Janeiro"], self.nodes["Cape Town"], "bateau"),
            Arete("jaune", 7, self.nodes["Buenos Aires"], self.nodes["Cape Town"], "bateau"),
            Arete("violet", 7, self.nodes["Buenos Aires"], self.nodes["Cape Town"], "bateau"),
            Arete("vert", 4, self.nodes["Reykjavik"], self.nodes["Murmansk"], "bateau"),
            Arete("gris", 2, self.nodes["Reykjavik"], self.nodes["Edimburgh"], "bateau"),
            Arete("jaune", 1, self.nodes["Edimburgh"], self.nodes["Hamburg"], "train"),
            Arete("noir", 1, self.nodes["Edimburgh"], self.nodes["Hamburg"], "train"),
            Arete("blanc", 1, self.nodes["Edimburgh"], self.nodes["Marseille"], "bateau"),
            Arete("vert", 1, self.nodes["Edimburgh"], self.nodes["Marseille"], "bateau"),
            Arete("rouge", 1, self.nodes["Marseille"], self.nodes["Hamburg"], "train"),
            Arete("violet", 1, self.nodes["Marseille"], self.nodes["Hamburg"], "train"),
            Arete("vert", 2, self.nodes["Athina"], self.nodes["Hamburg"], "train"),
            Arete("rouge", 2, self.nodes["Marseille"], self.nodes["Athina"], "bateau"),
            Arete("blanc", 2, self.nodes["Hamburg"], self.nodes["Moskva"], "train"),
            Arete("noir", 2, self.nodes["Hamburg"], self.nodes["Moskva"], "train"),
            PassageDifficile(1, self.nodes["Marseille"], self.nodes["Casablanca"]),
            Arete("gris", 4, self.nodes["Casablanca"], self.nodes["Lagos"], "train"),
            Arete("gris", 3, self.nodes["Casablanca"], self.nodes["Al-Qahira"], "train"),
            Arete("vert", 1, self.nodes["Athina"], self.nodes["Al-Qahira"], "bateau"),
            Arete("violet", 1, self.nodes["Lagos"], self.nodes["Luanda"], "train"),
            Arete("jaune", 1, self.nodes["Lagos"], self.nodes["Luanda"], "train"),
            Arete("gris", 2, self.nodes["Luanda"], self.nodes["Cape Town"], "train"),
            PassageDifficile(2, self.nodes["Luanda"], self.nodes["Dar es Salaam"]),
            Arete("violet", 3, self.nodes["Cape Town"], self.nodes["Dar es Salaam"], "train"),
            Arete("vert", 3, self.nodes["Cape Town"], self.nodes["Dar es Salaam"], "train"),
            Arete("gris", 3, self.nodes["Cape Town"], self.nodes["Toamasina"], "bateau"),
            Arete("jaune", 1, self.nodes["Dar es Salaam"], self.nodes["Toamasina"], "bateau"),
            Arete("rouge", 5, self.nodes["Cape Town"], self.nodes["None"], "bateau"),
            Arete("vert", 5, self.nodes["Cape Town"], self.nodes["None"], "bateau"),
            Arete("rouge", 1, self.nodes["Dar es Salaam"], self.nodes["Djibouti"], "train"),
            Arete("noir", 1, self.nodes["Dar es Salaam"], self.nodes["Djibouti"], "train"),
            Arete("rouge", 2, self.nodes["Djibouti"], self.nodes["Al-Qahira"], "train"),
            Arete("blanc", 2, self.nodes["Djibouti"], self.nodes["Al-Qahira"], "train"),
            Arete("jaune", 1, self.nodes["Al-Qahira"], self.nodes["Tehran"], "train"),
            Arete("noir", 1, self.nodes["Al-Qahira"], self.nodes["Tehran"], "train"),
            Arete("violet", 2, self.nodes["Moskva"], self.nodes["Murmansk"], "train"),
            Arete("rouge", 3, self.nodes["Moskva"], self.nodes["Tehran"], "train"),
            Arete("blanc", 3, self.nodes["Tehran"], self.nodes["Mumbai"], "train"),
            Arete("violet", 3, self.nodes["Tehran"], self.nodes["Mumbai"], "train"),
            Arete("blanc", 4, self.nodes["Dar es Salaam"], self.nodes["Mumbai"], "bateau"),
            Arete("vert", 7, self.nodes["Dar es Salaam"], self.nodes["Jakarta"], "bateau"),
            Arete("violet", 7, self.nodes["Dar es Salaam"], self.nodes["Jakarta"], "bateau"),
            Arete("blanc", 5, self.nodes["None"], self.nodes["Perth"], "bateau"),
            Arete("violet", 5, self.nodes["None"], self.nodes["Perth"], "bateau"),
            Arete("rouge", 7, self.nodes["Murmansk"], self.nodes["Tiksi"], "bateau"),
            Arete("vert", 4, self.nodes["Moskva"], self.nodes["Novosibirsk"], "train"),
            Arete("jaune", 4, self.nodes["Moskva"], self.nodes["Novosibirsk"], "train"),
            PassageDifficile(2, self.nodes["Tehran"], self.nodes["Lahore"]),
            PassageDifficile(3, self.nodes["Lahore"], self.nodes["Beijing"]),
            Arete("gris", 3, self.nodes["Tiksi"], self.nodes["Novosibirsk"], "train"),
            Arete("violet", 3, self.nodes["Novosibirsk"], self.nodes["Yakutsk"], "train"),
            Arete("blanc", 2, self.nodes["Novosibirsk"], self.nodes["Lahore"], "train"),
            Arete("noir", 1, self.nodes["Lahore"], self.nodes["Mumbai"], "train"),
            Arete("vert", 1, self.nodes["Lahore"], self.nodes["Mumbai"], "train"),
            Arete("jaune", 3, self.nodes["Mumbai"], self.nodes["Bangkok"], "train"),
            Arete("rouge", 3, self.nodes["Mumbai"], self.nodes["Bangkok"], "train"),
            Arete("jaune", 8, self.nodes["Tiksi"], self.nodes["Anchorage"], "bateau"),
            Arete("noir", 7, self.nodes["Tiksi"], self.nodes["Petropavlovsk"], "bateau"),
            Arete("vert", 1, self.nodes["Tiksi"], self.nodes["Yakutsk"], "train"),
            Arete("blanc", 3, self.nodes["Yakutsk"], self.nodes["Petropavlovsk"], "train"),
            Arete("violet", 3, self.nodes["Petropavlovsk"], self.nodes["Anchorage"], "bateau"),
            Arete("rouge", 3, self.nodes["Novosibirsk"], self.nodes["Beijing"], "train"),
            Arete("noir", 3, self.nodes["Novosibirsk"], self.nodes["Beijing"], "train"),
            Arete("jaune", 3, self.nodes["Yakutsk"], self.nodes["Beijing"], "train"),
            Arete("vert", 2, self.nodes["Beijing"], self.nodes["Hong Kong"], "train"),
            Arete("blanc", 2, self.nodes["Beijing"], self.nodes["Hong Kong"], "train"),
            Arete("gris", 2, self.nodes["Petropavlovsk"], self.nodes["Tokyo"], "bateau"),
            Arete("gris", 3, self.nodes["Hong Kong"], self.nodes["Tokyo"], "bateau"),
            Arete("violet", 1, self.nodes["Hong Kong"], self.nodes["Bangkok"], "train"),
            Arete("noir", 1, self.nodes["Hong Kong"], self.nodes["Bangkok"], "train"),
            Arete("violet", 1, self.nodes["Hong Kong"], self.nodes["Manila"], "bateau"),
            Arete("rouge", 2, self.nodes["Bangkok"], self.nodes["Manila"], "bateau"),
            Arete("jaune", 2, self.nodes["Tokyo"], self.nodes["Manila"], "bateau"),
            Arete("rouge", 5, self.nodes["Tokyo"], self.nodes["Honolulu"], "bateau"),
            Arete("blanc", 5, self.nodes["Honolulu"], self.nodes["Manila"], "bateau"),
            Arete("blanc", 2, self.nodes["Bangkok"], self.nodes["Jakarta"], "bateau"),
            Arete("gris", 2, self.nodes["Manila"], self.nodes["Jakarta"], "bateau"),
            Arete("noir", 2, self.nodes["Darwin"], self.nodes["Jakarta"], "bateau"),
            Arete("gris", 3, self.nodes["Perth"], self.nodes["Jakarta"], "bateau"),
            Arete("vert", 3, self.nodes["Honolulu"], self.nodes["Port Moresby"], "bateau"),
            Arete("rouge", 1, self.nodes["Darwin"], self.nodes["Port Moresby"], "bateau"),
            Arete("rouge", 2, self.nodes["Darwin"], self.nodes["Perth"], "train"),
            Arete("vert", 2, self.nodes["Darwin"], self.nodes["Sydney"], "train"),
            Arete("jaune", 2, self.nodes["Perth"], self.nodes["Sydney"], "train"),
            Arete("blanc", 2, self.nodes["Perth"], self.nodes["Sydney"], "train"),
            Arete("jaune", 3, self.nodes["Port Moresby"], self.nodes["Sydney"], "bateau"),
            Arete("rouge", 1, self.nodes["Sydney"], self.nodes["Christchurch"], "bateau"),
            Arete("blanc", 1, self.nodes["Sydney"], self.nodes["Christchurch"], "bateau")
        ]

    
    def voisins(self, ville, chemins_uti_list):
        """
        renvoie la liste des voisins de ville
        ville : str
        """
        voisins = []
        for e in self.edges:
            if e.get_depart().get_nom() == ville and e.get_arrivee().get_nom() not in voisins and e not in chemins_uti_list:
                voisins.append(e.get_arrivee().get_nom())
            if e.get_arrivee().get_nom() == ville and e.get_depart().get_nom() not in voisins and e not in chemins_uti_list:
                voisins.append(e.get_depart().get_nom())
        return voisins
    

    def poids(self, ville1, ville2):
        """
        renvoie le poids de l'arête entre ville1 et ville2
        ville1 : str
        ville2 : str
        """
        for e in self.edges:
            if e.get_depart().get_nom() == ville1 and e.get_arrivee().get_nom() == ville2:
                return e.get_taille()
            if e.get_depart().get_nom() == ville2 and e.get_arrivee().get_nom() == ville1:
                return e.get_taille()

    
    def dijkstra(self, depart, arrivee, chemins_uti_list):
        # mise en place dico distances #
        distances = {}
        for ville in self.nodes.keys(): distances[ville] = float('inf')
        distances[depart] = 0
        
        # mise en place dico predecesseurs #
        pred = {}
        for ville in self.nodes.keys(): pred[ville] = ""
        
        vu = []
        todo = [depart]
        while todo:
            x = todo.pop(0)
            if x not in vu:
                vu.append(x)
                # parcours des voisins de x #
                for succ in self.voisins(x, chemins_uti_list):
                    todo.append(succ)
                    if distances[succ] > distances[x] + self.poids(succ, x):
                        distances[succ] = distances[x] + self.poids(succ, x)
                        pred[succ] = x
        
        # mise en place affichage chemin #
        chemin = [arrivee]
        fin = arrivee
        while pred[fin] != "":
            chemin.append(pred[fin])
            fin = pred[fin]
        chemin_f = []
        for i in range(len(chemin)-1, -1, -1):
            chemin_f.append(chemin[i])
        return chemin_f
    

    def verification_arete(self, depart, arrivee, chemins_uti_list):
        for e in self.edges:
            if e.get_depart().get_nom() == depart and e.get_arrivee().get_nom() == arrivee and e not in chemins_uti_list:
                return e
            if e.get_depart().get_nom() == arrivee and e.get_arrivee().get_nom() == depart and e not in chemins_uti_list:
                return e
        return 1
