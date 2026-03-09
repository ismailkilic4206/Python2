#Kullanici 'c' degeri girmedigi surece alinan her girdinin sayisal ifade oldugundan emin olalim
#degilse hata mesaji yazdiralim

while True:
    sayi = input("Lutfen sayiyi giriniz: ")
    if sayi == "c":
        break

    try:
        sonuc = int(sayi)
        print(f"Girilen sayi {sonuc}")
    except ValueError:
        print("Lutfen gecerli bir deger giriniz..")
        continue