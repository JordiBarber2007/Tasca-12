def pex4():

    class Esportista:
        def __init__(self, nom, nacionalitat, edat):
            self.nom = nom
            self.nacionalitat = nacionalitat
            self.edat = edat
            
        def esport(self):
            pass
        
        def mostrar_nacionalitat(self):
            print(f"{self.nom} és de {self.nacionalitat}")
            
        def mostrar_anys(self):
            print(f"{self.nom} té {self.edat} anys\n")

    class Futbolista(Esportista):
        def esport(self):
            print(f"{self.nom} és un futbolista")

    class Tenista(Esportista):
        def esport(self):
            print(f"{self.nom} és un tenista")

    class Basquetbolista(Esportista):
        def esport(self):
            print(f"{self.nom} és un basquetbolista")

    class Culturista(Esportista):
        def esport(self):
            print(f"{self.nom} és un culturista")

    class F1(Esportista):
        def esport(self):
            print(f"{self.nom} és un pilot de F1")

    def pex4():
        llistagent = [
            Futbolista("Leo Messi", "Argentina", 32),
            Tenista("Rafa Nadal", "Espanya", 31),
            Basquetbolista("Lebron James", "USA", 30),
            Culturista("Kevin Levrone", "Brasil", 29),
            F1("Fernando Alonso", "Espanya", 33)
                    ]

        for e in llistagent: 
            e.esport()
            e.mostrar_nacionalitat()
            e.mostrar_anys()
