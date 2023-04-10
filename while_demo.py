#sayilar = [1,3,5,7,9,12,19,21]

#1
#i = 0
#while (i < len(sayilar)):
#    print(sayilar[i])
#    i += 1

#2
#baslangic = int(input("ilk sayı: "))
#bitis = int(input("bitiş: "))

#i = baslangic
#while i < bitis:
#    i += 1
#    if (i % 2 == 1):
#        print(i)

#3
#i = 100
#while i > 0:
#    print(i)
#    i -= 1

#4
#numbers = []

#i = 0
#while i < 5:
#    sayi = int(input("sayı: "))
#    numbers.append(sayi)
#    i += 1

#numbers.sort()
#print(numbers)

#5
urunler = []

urunsayisi = int(input("Kaç Ürün Ekleyeceksiniz: "))
i = 0

while (i < urunsayisi):
    name = input("Üürn Adı: ")
    price = input("Ürün Fiyatı: ")
    urunler.append({
        "name": name ,
        "price": price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')

