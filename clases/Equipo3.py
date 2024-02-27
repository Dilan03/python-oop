class Equipo3:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Leonardo Alberto Gonzáles Carmona"
        self.integrante_2 = "Norma Graciela Mendoza Ruiz"
        self.integrante_3 = "Jonathan Durán Mendoza"
        self.eslogan = "Respiración de Programación, Pose de HTML, Codificar"

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)