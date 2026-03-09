#Girilen sifre icinde TR karakter hatasi veren uygulama
karakterTR = "çğİıöşüÇĞÜŞÖ"

sifre = input("Lutfen sifre giriniz: ")
for i in sifre:
    if i in karakterTR:
        raise TypeError("Sifreniz, TR karakter icermemelidir..")
    else:
        pass
print("Sifreniz Gecerlidir..")