eDevlet = "https://www.turkiye.gov.tr"
text = "Turkiye'nin en guzel sehri Istanbul'dur"

#edevlet icinden www karakterlerini yazdirin
print(eDevlet[8:11])
#eDevlet icinden tukiye karakterlerini yazdirin
print(eDevlet[12:19])
#text karakter dizisinde kac tane karakter bulunur
print(len(text))
#text icinde ilk 7 e son 12 karakteri yazdirin Turkiye------Istanbul'dur
print(text[:7], text[len(text)-12:])
print(text[:7], text[-12:])
#text degiskenindeki karakterleri testen yazdirin
print(text[::-1])