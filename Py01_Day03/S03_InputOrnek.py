#Verilen 3 siparisin toplamini kullanicidan almis oldugunuz fiyatlar
# ile degiskenler olusturarak hesaplayip yazdiriniz

# siparis 1 = kullanicidan girilen deger + vergi
# siparis 2 = kullanicidan girilen deger + vergi
# siparis 3 = kullanicidan girilen deger + vergi

# vergi oranlari % olarak kullanicidan alinicaktir

siparis1 = int(input("1. Siparisin Fiyatini Giriniz: "))
siparis2 = int(input("2. Siparisin Fiyatini Giriniz: "))
siparis3 = int(input("3. Siparisin Fiyatini Giriniz: "))
vergiOrani = int(input("Vergi Oranini Giriniz: %"))
vergiOrani = vergiOrani/100

vergiDahilSiparis1 = siparis1 * vergiOrani + siparis1
vergiDahilSiparis2 = siparis2 * vergiOrani + siparis2
vergiDahilSiparis3 = siparis3 * vergiOrani + siparis3

siparisToplam = vergiDahilSiparis1 + vergiDahilSiparis2 + vergiDahilSiparis3

print("Siparisin Toplami: " + str(siparisToplam))