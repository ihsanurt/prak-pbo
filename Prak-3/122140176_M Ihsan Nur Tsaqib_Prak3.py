class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for index, barang in enumerate(cls.list_barang, start=1):
            nama, stok, harga = barang
            print(f"{index}. {nama} seharga Rp {harga} (stok: {stok})")

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for barang in Dagangan.list_barang:
            if barang[0] == self.__nama:
                print(f"{self.__nama} dihapus dari toko!")
                Dagangan.list_barang.remove(barang)
                break
        else:
            print(f"{self.__nama} tidak ditemukan di toko.")


Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()