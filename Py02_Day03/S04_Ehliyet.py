#Soru 3- Kullanicidan yasini isteyin, 18 yas üzeeri ise "ehliyet alabilirsin" yazdırın,
# yoksa ehliyet alması için gereken yil sayısını yazdırın.

yas = int(input("Lutfen yasınızı giriiniz: "))

if yas >=18:
    print("Ehliyet alabilirsiniz.")
else:
    print(f"Ehiyet almanıza {18-yas} yıl kaldi.")
