class Persegi_Panjang:
    panjang = 0
    lebar = 0

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hasil(self):
        l = self.panjang * self.lebar
        k = 2 * (self.panjang + self.lebar)

        print("===== Persegi Panjang ======"
              "\nPanjang: ", self.panjang,
              "\nLebar: ", self.lebar,
              "\nLuas: ", l,
              "\nKeliling: ", k,
              "\n==========================="
              "\n")
