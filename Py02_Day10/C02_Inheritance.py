#C02_Inheritance.py

#Inheritance (Kalitim, Miras)
#Insan(isim, soyisim, yas, yemek(), icmek(), nefesAlmak(), yurumek())

#Ogrenci(Insan, okul, bolum, ogrenciNumarasi, sehir)

#Universiteli(Ogrenci, universite, fakulte, bolum)

#MuhendislikOgrencisi (Universiteli, )

#BilgisayarMuhendisi(MuhendislikOgrencisi, )

class Insan():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        print("Insan Class'i calisti")

    def benKimim(self):
        print("Ben bir insanim")

    def yemek(self):
        print("Ben yemek yerim")

class Ogrenci(Insan):
    def __init__(self, isim, soyisim, okul):
        Insan.__init__(self, isim, soyisim)
        self.okul = okul
        print("Ogrenci Class'i calisti")

    ##Override
    def benKimim(self):
        print("Ben bir ogrenciyim")

nazif = Insan("Nazif", "Umut")
akif = Ogrenci("Akif", "Sert","Cankaya Lisesi")

print(f"{nazif.isim} {nazif.soyisim}")
print(f"{akif.isim} {akif.soyisim}, {akif.okul}")

nazif.benKimim()
akif.benKimim()

nazif.yemek()