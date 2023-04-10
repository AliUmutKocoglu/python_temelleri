import random
sayi = random.randint(1,100)

hak = 3
while hak>0:
    hak-=1
    tahmin = int(input("Tahmin Giriniz: "))
    if sayi==tahmin:
        print("Tebrikler Kazandınız")
        break
    if sayi<tahmin:
        print("Lütfen Tekrar Deneyiniz ve Daha Küçük Bir Sayı Giriniz")
    if sayi>tahmin:
        print("Lütfen Tekrar Deneyiniz ve Daha Büyük Bir Sayı Giriniz")
    if hak == 0:
        print("Üzgünüz Hakkınız Kalmadı")


