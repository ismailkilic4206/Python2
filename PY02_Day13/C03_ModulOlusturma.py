#C03_ModulOlusturma.py
from symtable import Class

"""
Modul hakkinda bilgilendirme yapildi
"""

print("Modul eklendi")

numara = 7

numaralar = [7, 8, 9]

ogrenci ={
    "isim" : "Nazif",
    "yas" : "19",
    "sehir" : "Ankara"
}

def fonksiyon(x):

    """
    Fonksiyon hakkinda  bilgilendirme yapildi
    """
    print(f"X degeri: {x}")


class Insan:
    def yeme(self):
        print("Ben yemek yerim")