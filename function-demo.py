#def yazdir(kelime, adet):
#    print(kelime * adet)
#
#yazdir("Ali\n", 10)


#def listeyeCevir(*params):
#    liste = []
#
#    for param in params:
#        liste.append(param)
#
#    return liste
#
#result = listeyeCevir(10,30,30,"Merhaba")
#print(result)



#def asalSayilariBul(sayi1, sayi2):
#    for sayi in range(sayi1, sayi2+1):
#        if sayi > 1:
#            for i in range(2, sayi):
#                if (sayi % i == 0):
#                    break
#            else:
#                print(sayi)
#
#sayi1 = input("sayı 1:")
#sayi2 = input("sayi 2:")


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))