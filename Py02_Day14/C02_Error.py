#C02_Error.py

try:
    sayi01 = int(input("a: "))
    sayi02 = int(input("b: "))

    print(sayi01 / sayi02)

except (ZeroDivisionError, ValueError) as hata:
    #print("b icin 0(Sifir) giremezsiniz...")
    print("Hatali giris yaptiniz...")
    print(hata)

#except ValueError:
#    print("Sadece sayi girebilirsiniz...")