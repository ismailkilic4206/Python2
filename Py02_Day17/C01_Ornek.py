def ortalamaHesapla(kisiBilgisi):
    sinavNotu = kisiBilgisi[:-1]
    liste = kisiBilgisi.split(":")

    isimSoyisim = liste[0]
    notlar = liste[1].split(",")


    vizeNotu = int(notlar[0])
    finalNotu = int(notlar[1])

    ortalama = (vizeNotu + finalNotu) / 2

    if ortalama >= 85 and ortalama <= 100:
        harfNotu = "AA"
    elif ortalama >= 50 and ortalama < 85:
        harfNotu = "BB"
    elif ortalama >= 35 and ortalama < 50:
        harfNotu = "CC"
    else:
        harfNotu = "DD"

    return isimSoyisim + ": " + harfNotu + "\n"

def notOkuma():
    with open("sinavNotlari.txt", "r", encoding = "UTF-8") as file:
        for kisiBilgisi in file:
            print(ortalamaHesapla(kisiBilgisi))

def notGirme():
    isim = input("Ogrenci Adi: ")
    soyisim = input("Ogrenci Soyisim: ")
    vize = input("Vize Notu: ")
    final = input("Final Notu: ")

    with open("sinavNotlari.txt", "a", encoding = "UTF-8") as file:
        file.write(isim + " " + soyisim +  ":" + vize + "," + final + "\n")

def notKayit():
    with open("sinavNotlari.txt", "r", encoding = "UTF-8") as file:
        liste = []
        for i in file:
            liste.append(ortalamaHesapla(i))
        with open("sonuc.txt","w", encoding = "UTF-8") as file02:
            for i in liste:
                file02.write(i)


while True:
    yapilacakIslem = input("1 --> Not Okuma\n2 --> Not Gir\n3 --> Not Kayit\n4 --> Cikis")

    if yapilacakIslem == "1":
        notOkuma()

    elif yapilacakIslem == "2":
        notGirme()

    elif yapilacakIslem == "3":
        notKayit()

    else:
        break