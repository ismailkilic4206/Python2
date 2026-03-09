#Soru 5- kullanıcıdan notunu alın 50 veya daha yüksek ise Sınıfı geçtin
# 50den kucuk ise maalese kalsın yazın

notSinav= int(input("Lutfen notunuzu giriniz:..."))

if 0<= notSinav < 50:
    print("Maalese kaldiniz.")

elif 50 <= notSinav <= 100:
    print("Sinifi gectiniz.")

else:
    print("Lutfen uygun bir not giriniz.")