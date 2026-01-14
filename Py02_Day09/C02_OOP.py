#Class
class Insan:
    pass
    #Class Atributes
    adres = "Null"

    #Constructor(Yapici Method)
    def __init__(self, kimlikNo, isim, soyisim, dogumYili, kanGrubu):
        pass
        #Object Atributes
        self.kimlikNo = kimlikNo
        self.isim = isim
        self.soyisim = soyisim
        self.dogumYili = dogumYili
        self.kanGrubu = kanGrubu
        print("init Methodu Calisti")


    #Methods
    def selam(self):
        print("Merhaba ben " + self.isim)

    #Methods
    def yasHesaplama(self):
        return  2026 - self.dogumYili

#Object (Instance)
hakan = Insan(123456, "Hakan", "Coskun", 2012, "0 (-)")
akif  = Insan(123456, "Akif", "Sert", 2012, "0 (+)")
#berra = Insan()
#nazif = Insan()

#Guncelleme
hakan.kanGrubu = "0 (+)"
hakan.adres = "Ankara"

#print(nazif)
#print(akif)

print(f"Kimlik Numarasi: {hakan.kimlikNo}"
      f"\nIsim: {hakan.isim}"
      f"\nSoyisim: {hakan.soyisim}"
      f"\nAdres: {hakan.adres}"
      f"\nKan Grubu: {hakan.kanGrubu}")

hakan.selam()
akif.selam()

print(f"adim: {hakan.isim}, yasim: {hakan.yasHesaplama()}")
print(f"adim: {akif.isim}, yasim: {akif.yasHesaplama()}")