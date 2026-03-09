liste = ['2', '7', 'asd', '12g', '49', 'oi45', '79']

#Liste icerisinde bulunan sayisal degerleri bulalim
for eleman in liste:
    try:
        son = int(eleman)
        print(son)
    except ValueError:
        continue