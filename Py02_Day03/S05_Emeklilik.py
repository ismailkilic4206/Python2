#Soru 4- Kullanıcıdan cinsiyetini ve yasını alin,
#Kadın 60 yas ve uzri Erkek 65 yas ve üzeri emekli olabilir
# cinsiyet ve yasini dikkate alarak Emekli olabirisin veya emekli olmak için .... yıl daha çalışmalısın
# yazdırın.

cinsiyet = input("Lutfen cinsiyetiniz giriniz (E/K): ").upper()
yas = int(input("Lutfen yasinizi giriniz: "))

if cinsiyet == "K":
    if yas >= 60:
        print("Emekli olabilirisin")
    else:
        print(f"Emekli olmak icin {60-yas} yil daha çalısman gerekir.")

elif cinsiyet == "E":
    if yas >= 65:
        print("Emekli olabilirisin")
    else:
        print(f"Emekli olmak için {65-yas} yıl calısman gerekir")

else:
    print("Lutfen gecerli bir cinsiyet girin.(K/E)")