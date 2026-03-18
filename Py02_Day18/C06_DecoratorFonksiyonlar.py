def decorator (func):

    def wrapper(ad):
        print("onceki islem...")
        func(ad)
        print("sonraki islem...")

    return wrapper
@decorator
def merhabaDe(isim):
    print(f"Merhaba {isim}...")

merhabaDe("Hakan")