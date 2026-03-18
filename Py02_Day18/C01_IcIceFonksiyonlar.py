def selamDe(isim):
    print("Selam", isim)

#print(selamDe("Ahmet"))
#print(selamDe)

selam = selamDe

#print(selam)
#print(selamDe)

#print(selam("Ahmet"))
#print(selamDe("Ahmet"))

del selam
print(selamDe)
#print(selam) #NameError: name 'selam' is not defined. Did you mean: 'selamDe'?