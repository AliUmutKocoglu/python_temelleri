import random

sayi = random.randint(1,50)
hak = 5
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))
    if sayi == tahmin:
            print(f"Tebrikler {sayac}. Denemede Bildiniz.")
            break
    if sayi > tahmin:
        print("Yukarı.")
    if tahmin > sayi:
        print("Aşşağı.")

    if hak == 0:
        print(f"Malesef Bilemediniz. Tutulan Sayı: {sayi}")