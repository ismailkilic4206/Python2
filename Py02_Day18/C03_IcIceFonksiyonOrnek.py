def faktoriyel(sayi01):

    if not  isinstance(sayi01, int):
        raise TypeError("Girilen deger bir tamsayi olmalidir..")

    if not sayi01 >= 0:
        raise ValueError("Girilen deger p+ tamsayi olmalidir..")

    def icFaktoriyel(sayi01):
        if sayi01 <= 1:
            return  1
        return  sayi01 * icFaktoriyel(sayi01 - 1)

    return icFaktoriyel(sayi01)

print(faktoriyel(5))