##Soru 2- kullanicidan bir harf alin, harf ile baslayan bir sayı varsa yazdırın
#not: buyuk ve kucuk harf hassasiyeti olmasın
#kullanıcı o veya O yazdığında output Ocat olsun

aylar = {
    "o" : "Ocak" ,
    "s" : "Subat",
    "m" : "Mart" ,
    "n" : "Nisan" ,
    "h" : "Haziran",
    "t" : "Temmuz"
}

harf = input("Lutfen bir harf giriniz...").lower()

if harf in aylar:
    print(aylar[harf])
else:
    print("Girdirğiniz harf ile baslayan ay adi yoktur.")