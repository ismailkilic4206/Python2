#Verilen 3 siparsin toplamini degişkenler oluşturarak hesaplayıp yazdırınız

# Siparis 1 = 510 tl + vergi
# Siparis 2 = 2070.82 tl + vergi
# Siparis 3 = 730 tl + vergi
# Vergi oranlri %8 hesaplanacatir

siparis01 = 510
siparis02 = 2070.82
siparis03 = 730
vergi = 0.08

vergiDahilsiparis01 = siparis01 * vergi + siparis01
vergiDahilsiparis02 = siparis02 * vergi + siparis02
vergiDahilsiparis03 = siparis03 * vergi + siparis03
toplam = vergiDahilsiparis01 + vergiDahilsiparis02 + vergiDahilsiparis03

print("verilen 3 siparisin toplamı: " + str(toplam))