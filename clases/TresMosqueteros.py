class TresMosqueteros:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Dania Denisse Benavides Figueroa"
        self.integrante_2 = "Erick Lozano Duarte"
        self.integrante_3 = "Ana Cristina Valenzuela Ruiz"
        self.eslogan = "Todos para uno, uno para todos"

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)