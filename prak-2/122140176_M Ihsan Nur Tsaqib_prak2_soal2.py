def pastikan_positif(func):
    def pembungkus(instansi, *args, **kwargs):
        if all(arg > 0 for arg in args):
            print("Semua argumen positif. Fungsi sedang dijalankan.")
            return func(instansi, *args, **kwargs)
        else:
            print("Error: Semua argumen harus positif.")
            return None
    return pembungkus

class KonverterJarak:
    def __init__(self):
        print("KonverterJarak diinisialisasi.")

    def __del__(self):
        print("KonverterJarak dihentikan.")

    @pastikan_positif
    def km_ke_mil(self, km):
        return km * 0.621371

# Penggunaan
konverter = KonverterJarak()
km = int (input("Masukkan jarak dalam KM: "))
mil = konverter.km_ke_mil(km)
if mil is not None:
    print(f"{km} kilometer sama dengan {mil} mil.")
