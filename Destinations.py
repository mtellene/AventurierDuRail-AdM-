
class Destination:

    def __init__(self, depart, arrivee, points):
        self.depart = depart
        self.arrivee = arrivee
        self.points = points
        self.type = 0    # 0 if destination, 1 if itinerary

    def get_depart(self): return self.depart
    
    def get_arrivee(self): return self.arrivee
    
    def get_points(self): return self.points
    
    def get_type(self): return self.type



class Itineraire(Destination):

    def __init__(self, depart, arrivee, points, ordre, sous_points, malus):
        super().__init__(depart, arrivee, points)
        self.type = 1
        self.ordre = ordre
        self.sous_points = sous_points
        self.malus = malus

    def get_ordre(self): return self.ordre

    def get_sous_points(self): return self.sous_points

    def get_malus(self): return self.malus