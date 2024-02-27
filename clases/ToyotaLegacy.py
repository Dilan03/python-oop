class ToyotaLegacy:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Israel Chacon Rojo"
        self.integrante_2 = "Dilan Mauricio Garcia Hernandez"
        self.integrante_3 = "Jesus Elias Sierra Ruiz"
        self.eslogan = "Transformamos líneas de código en experiencias excepcionales."

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)