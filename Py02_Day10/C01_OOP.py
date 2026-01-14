#C01_OOP.py

class Daire:
    #Class Atributes
    pi = 3.14

    #Constructor(Yapici Method, init methodu)
    def __init__(self, yariCap = 1):
        self.yariCap = yariCap

    #Methods
    def daireninAlani(self):
        return self.pi * self.yariCap ** 2

    def daireninCevresi(self):
        return 2 * self.pi * self.yariCap

hakan = Daire()
akif = Daire(3)

print(f"Hakan Dairesinin Alani: {hakan.daireninAlani()}, Hakan Dairesinin Cevresi: {hakan.daireninCevresi()}")
print(f"Akif Dairesinin Alani: {akif.daireninAlani()}, Akif Dairesinin Cevresi: {akif.daireninCevresi()}")