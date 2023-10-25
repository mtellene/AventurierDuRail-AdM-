class Arete:

    def __init__(self, couleur, taille, depart, arrivee, type):
        self.couleur = couleur
        self.taille = taille
        self.depart = depart
        self.arrivee = arrivee
        self.type = type

        points = {
            1: 1,
            2: 2,
            3: 4,
            4: 7,
            5: 10,
            6: 15,
            7: 18,
            8: 21
        }
        self.points = points[self.taille]

    def get_couleur(self): return self.couleur

    def get_taille(self): return self.taille

    def get_depart(self): return self.depart

    def get_arrivee(self): return self.arrivee

    def get_points(self): return self.points


class PassageDifficile(Arete):

    def __init__(self, taille, depart, arrivee):
        super().__init__("gris", taille, depart, arrivee, "train")
