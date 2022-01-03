class Lingkaran:
    # member1 variabel1
    jari2 = 0

    # member2 konstruktor
    def __init__(self, jari2):
        self.jari2 = jari2

    # member3 method

    def hasil(self):
        if(self.jari2 > 0):
            k = 2 * 3.14 * self.jari2
            l = 3.14 * self.jari2 * self.jari2

        print("==== Lingkaran ===="
              "\nJari2: ", self.jari2,
              "\nKeliling: ", k,
              "\nLuas: ", l,
              "\n===================="
              "\n")
