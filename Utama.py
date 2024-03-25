from Kendaraan import Kendaraan
from Sepeda import Sepeda
from Motor import Motor
from Mobil import Mobil

kendaraan_umum = Kendaraan('Kendaraan Umum', 100)

sepeda_lipat = Sepeda('Sepeda Lipat', 20, 21)

motor_honda_vario = Motor('Motor Honda Vario', 150, 250)

mobil_pajero_sport_2024 = Mobil('Mobil Pajero Sport 2024', 180, 7, 'Diesel')

print(f"{kendaraan_umum.nama} kecepatannya hingga {kendaraan_umum.kecepatan_max} km/jam.")
print(f"{sepeda_lipat.nama} punya sabila memiliki {sepeda_lipat.jumlah_gir} gir.")
print(f"{motor_honda_vario.nama} yang saya beli kapasitas mesinnya {motor_honda_vario.kapasitas_mesin} cc.")
print(f"{mobil_pajero_sport_2024.nama} impian saya yaitu ada {mobil_pajero_sport_2024.jumlah_kursi} kursi dan bahan bakarnya yaitu {mobil_pajero_sport_2024.jenis_bahan_bakar}.")