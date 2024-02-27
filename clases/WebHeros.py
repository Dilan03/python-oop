class WebHeros:
    integrante_1 = ""
    integrante_2 = ""
    integrante_3 = ""
    eslogan = ""

    def __init__(self):
        self.integrante_1 = "Jesus Manuel Arellano Merendon"
        self.integrante_2 = "Axel Felipe Reyes Valadez"
        self.integrante_3 = "Luis Daniel Delgado Enriquez"
        self.eslogan = "La verdad solo se puede encontrar en un lugar: el codigo"

    def __str__(self):
        return "{}\n{}\n{}\n{}\n".format(self.integrante_1, self.integrante_2, self.integrante_3, self.eslogan)