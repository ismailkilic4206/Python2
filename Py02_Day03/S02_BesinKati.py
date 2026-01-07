#Soru 1- kullanıcadan bir sayi isteyin, sayiyi kontrol edip 5 ile bolunebiliyorsa
#sayi %'in kati yazırın

sayi =int(input("Lutfen bir sayi giriniz:..."))

if sayi % 5 == 0:
    print(f"{sayi}, 5'in katidir.")