#C03_Error.py

# try:
#     sayi01 = int(input("a: "))
#     sayi02 = int(input("b: "))
#
#     print(sayi01 / sayi02)
#
# except :
#     print("Hatali giris yaptiniz...")

while True:
    try:
        sayi01 = int(input("a: "))
        sayi02 = int(input("b: "))

        print(sayi01 / sayi02)

    except :
        print("Hatali giris yaptiniz...")

    else:
        break