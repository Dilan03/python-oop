from .Equipo3 import Equipo3
from .ToyotaLegacy import ToyotaLegacy
from .PingGalact import PingGalact
from .LosPolystation import LosPolystation
from .TresMosqueteros import TresMosqueteros
from .WebHeros import WebHeros

class FS3:

    def __init__(self):
        self.Equipo_1 = ToyotaLegacy()
        self.Equipo_2 = WebHeros()
        self.Equipo_3 = Equipo3()
        self.Equipo_4 = TresMosqueteros()
        self.Equipo_5 = LosPolystation()
        self.Equipo_6 = PingGalact()

    def __str__(self):
        return "\n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.Equipo_1, self.Equipo_2, self.Equipo_3, self.Equipo_4, self.Equipo_5, self.Equipo_6)