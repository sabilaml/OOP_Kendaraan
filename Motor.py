from Kendaraan import Kendaraan

class Motor(Kendaraan):
    def __init__(self, nama, kecepatan_max, kapasitas_mesin):
        super().__init__(nama, kecepatan_max)
        self.kapasitas_mesin = kapasitas_mesin