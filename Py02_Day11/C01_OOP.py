#C01_OOP.py
#Sinav Uygulamasi

class Soru:
    def __init__(self, soru, secenekler, cevap):
        self.soru = soru
        self.secenekler = secenekler
        self.cevap = cevap
    def cevapKontrol(self, cevap):
        return self.cevap == cevap


class Sinav:
    def __init__(self, sorular):
        self.sorular = sorular
        self.puan = 0
        self.soruIndex = 0

    def soruGetir(self):
        return self.sorular[self.soruIndex]

    def gosterSoru(self):
        sorux = self.soruGetir()
        print(f"SORU {self.soruIndex + 1}: {sorux.soru}")

        for i in sorux.secenekler:
            print(f"* {i}")

        cevap = int(input("Cevap: "))
        self.tahmin(cevap)
        self.soruYukle()


    def tahmin (self, cevap):
        sorux = self.soruGetir()

        if sorux.cevapKontrol(cevap):
            self.puan += 20
        self.soruIndex += 1



    def soruYukle (self):
        if len(self.sorular) == self.soruIndex:
            self.gosterPuan()
        else:
            self.gosterSurec()
            self.gosterSoru()


    def gosterPuan (self):
        print(f"Puaniniz: {self.puan}")

    def gosterSurec (self):
        toplamSoru = len(self.sorular)
        soruNumarasi =self.soruIndex +1

        if soruNumarasi > toplamSoru:
            print("Sinav Bitti")
        else:
            print(f" SORU {soruNumarasi} / {toplamSoru} ".center(50,"*"))

s1 = Soru("2'nin kupu kactir", [2, 6, 8, 4], 8)
s2 = Soru("2'nin karesi kactir", [2, 6, 8, 4], 4)
s3 = Soru("3'nin kupu kactir", [12, 9, 27, 3], 27)
s4 = Soru("3'nin karesi kactir", [12, 9, 27, 3], 9)
s5 = Soru("2'nin 3 kati kactir", [2, 6, 8, 4], 6)
sorular = [s1, s2, s3, s4, s5]

sonuc = Sinav(sorular)
sorux = sonuc.soruGetir()
sonuc.soruYukle()



