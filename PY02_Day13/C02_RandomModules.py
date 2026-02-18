#C02_RandomModules.py

import  random
#sonuc = dir(random)

sonuc = random.random() # 0 - 1 arasi bir sayi tutar
sonuc = random.random() * 10
sonuc = int(random.uniform(1,9))
sonuc = random.randint(1,100)

isim = "Akif Sert"
meyveler = ['Elma', 'Armut', 'Kivi', 'Seftali', 'Nektarin', 'Erik', 'Karpuz']
#sonuc = meyveler[random.randint(0,len(meyveler) - 1)]
sonuc = random.choice(meyveler)
sonuc = random.choice(isim)

liste = list(range(8))
random.shuffle(liste)
sonuc = liste

liste = range(25)
sonuc = random.sample(liste, 8)
sonuc = random.sample(isim, 3)

print(sonuc)