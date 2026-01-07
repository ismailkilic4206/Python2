# Dairenin Alani
# Dairenin Cevresi
# Dairenin yari capi kullanicidan alinan bir dairenin alan ve cevresini hesaplayiniz
# Dairenin Alani: pi * (r**2)
# Dairenin Cevresi: pi * r *2

pi = int(input("Pi Sayisini Giriniz: "))
r = int(input("Dairenin Yari Capini Giriniz: "))

daireninAlani = pi * (r**2)
daireninCevresi = pi * r *2

print("Yari Capi Verilen Dairenin Cevresi: " + str(daireninCevresi) +
      "\nYari Capi Verilen Dairenin Alani: " + str(daireninAlani))
