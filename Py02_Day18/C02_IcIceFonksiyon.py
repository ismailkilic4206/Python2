
#encapsulation
def disFonksiyon(sayi1):
    print("Dis Fonksiyon Calisti..")

    def icFonksiyon(sayi1):
        print("Ic Fonksiyon Calisti..")
        return sayi1 + 1
    sayi2 = icFonksiyon(sayi1)
    print(f"1. Sayi: {sayi1}\n2. Sayi: {sayi2}")

disFonksiyon(9)

