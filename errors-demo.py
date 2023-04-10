liste = ["1", "2","5a", "10b", "abc", "10", "50"]

#1
#for x in liste:
#    try:
#        result = int(x)
#        print(result)
#    except ValueError:
#        continue

#2
#while True:
#    sayi=input("sayı: ")
#    if sayi == "q":
#        break
#
#    try:
#        result = float(sayi)
#    except:
#        print("geçersiz sayı")
#        continue
#    else:
#        print("girdiniz")

#3
#parola = input("Parola: ")
#def checkPassword(parola):
#    turkceKarakterler = "şçğüöıİÖĞŞÇ"
#    for i in parola:
#        if i in turkceKarakterler:
#            raise TypeError("Parola türkçe karakter içeremez.")
#        else:
#            pass
#    print("Geçerli Parola")

#try:
#    checkPassword(parola)
#except TypeError as error:
#    print(error)

#4
def faktoriyel(x):
    x = int(x)
    if x<0:
        raise ValueError("Negatif Değer")
    
    result = 1
    
    for i in range(1, x+1):
        result *= i
        
    return result

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)

