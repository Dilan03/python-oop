class PingGalact:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Yahir Antonio Monje Ochoa"
        self.integrante_2 = "Yesica Cristina Rodriguez Renteria"
        self.integrante_3 = "Integrante 3"
        self.eslogan = "SIC•PARVIS•MAGNA"

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)