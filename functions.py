def sayHello(name = "user"):
    return "Hello " + name

msg = sayHello("Ali")
msg = sayHello("Umut")

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10, 20)
print(result)



def yasHesapla(dogumYili):
    return 2022 - dogumYili

ageAli = yasHesapla(2003)
ageUmut = yasHesapla(2017)
ageMehmet = yasHesapla(1997)

print(ageMehmet, ageAli, ageUmut)

def emekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRİNG: Doğum yılnıza göre emekliliğinize kaç yıl kadlı
    INPUT: Doğum Yılı
    OUTPUT: Hesaplanan Yıl Bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz")

emekliligeKacYilKaldi(1953, "Ali")
emekliligeKacYilKaldi(1968, "Müslüm")

print(help(emekliligeKacYilKaldi))

list = [1,2,3]
print(help(list.append))


