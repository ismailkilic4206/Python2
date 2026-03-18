def girisDenetleme (sayfa):

    def icFonksiyon (rol):
        if rol == "Admin":
            return "Rolu {0} olan calisan {1}'ya ulasabilir..".format(rol, sayfa)
        else:
            return "Rolu {0} olan calisan {1}'ya ulasamaz..".format(rol, sayfa)
    return icFonksiyon


calisan1 = girisDenetleme("Ana Sayfa")
print(calisan1("Admin"))

calisan2 = girisDenetleme("Urun Sayfasi")
print(calisan2("Kullanici"))