from Kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan_max, jumlah_kursi, jenis_bahan_bakar):
        super().__init__(nama, kecepatan_max)
        self.jumlah_kursi = jumlah_kursi
        self.jenis_bahan_bakar = jenis_bahan_bakar

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"impian saya yaitu ada {self.jumlah_kursi} kursi dan bahan bakarnya yaitu {self.jenis_bahan_bakar}.")