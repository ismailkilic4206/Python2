#C04_DosyaYonetimi.py

#open() fonksiyonu ile dosya acar veya olustururuz
#Kullanimi: open(dosyaAdi, dosyaErismeModu)
#"w" (write): yazma modudur..
#dosya = open("dosyaAdi", "w")
#dosya.close()

#dosya = open("C:/Users/saidn/OneDrive/Desktop/dosyaAdi.pdf", "w")
#print(dosya)
#dosya.close()

#dosya = open("dosyaAdi", "w", encoding = "UTF-8")
#dosya.write("İsmail Kılıç")
#dosya.close()
#
#
#
##   "a" (append): ekleme..
#dosya = open("dosyaAdi", "a", encoding = "UTF-8")
#dosya.write("\nHakan C")
#dosya.close()



#   "x" (create): olusturma
dosya = open("dosyaAdi23", "x", encoding = "UTF-8")
dosya.close()
#   "r" (read): okuma
