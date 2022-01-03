class Segitiga:
    alas = 0
    tinggi = 0
    sisi1 = 0
    sisi2 = 0

    def __init__(self, alas, tinggi, sisi1, sisi2):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2

    def hasil(self):
        l = 0.5 * self.alas * self.tinggi
        k = self.alas + self.sisi1 + self.sisi2

        print("===== Segitiga ======"
              "\nPanjang: ", self.alas,
              "\nLebar: ", self.tinggi,
              "\nLuas: ", l,
              "\nKeliling: ", k,
              "\n==========================="
              "\n")
