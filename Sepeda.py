from Kendaraan import Kendaraan

class Sepeda(Kendaraan):
    def __init__(self, nama, kecepatan_max, jumlah_gir):
        super().__init__(nama, kecepatan_max)
        self.jumlah_gir = jumlah_gir