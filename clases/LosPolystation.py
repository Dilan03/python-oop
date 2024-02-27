class LosPolystation:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Erick Fernando Siqueiros Zúñiga"
        self.integrante_2 = "Paulina Ixchel Arreguin Ruiz"
        self.integrante_3 = "Integrante 3"
        self.eslogan = "Conectando el futuro, hoy"

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)