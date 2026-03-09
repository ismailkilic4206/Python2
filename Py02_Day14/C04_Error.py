#C04_Error.py

# rakam = int(input("Bir Rakam giriniz.. "))
#
# if rakam > 9:
#     raise  Exception("Rakam 9'dan buyuk olamaz")

def sifreKontrol(sifre):
    import  re
    if len(sifre) < 6:
        raise Exception("Sifreniz 6 haneden daha az olamaz..")
    elif not  re.search("[a-z]", sifre):
        raise Exception("Sifre kucuk harf icermelidir..")
    elif not  re.search("[A-Z]", sifre):
        raise Exception("Sifre buyuk harf icermelidir..")
    elif not  re.search("[0-9]", sifre):
        raise Exception("Sifre rakam icermelidir..")
    elif not  re.search("[_-]", sifre):
        raise Exception("Sifre '_' veya '-' icermelidir..")
    elif re.search("\s", sifre):
        raise Exception("Sifre bosluk karakteri icermemelidir..")

sfr = "12345678kH_"

try:
    sifreKontrol(sfr)
except Exception as hata:
    print(hata)
else:
    print("Sifreniz Hatasizdir")