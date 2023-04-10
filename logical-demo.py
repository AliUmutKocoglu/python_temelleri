#1
#girilenSayi = float(input("Sayı Giriniz: "))
#result = (0 < girilenSayi < 100)
#print(f"Girmiş Olduğunuz {girilenSayi} sayısı 0 ila 100 arasında mıdır?: {result}")

#2
#girilenSayi = int(input("Sayı Giriniz: "))
#result = (girilenSayi > 0) and (girilenSayi % 2 == 0)
#print(f"Girmiş Olduğunuz {girilenSayi} sayısı pozitif çift sayı mıdır?: {result}")

#3
#email = "kocoglu"
#sifre = "abc123"

#girilenEmail = input("Lütfen e-mailinizi giriniz: ").strip().lower()
#girilenSifre = input("Lütfen şifrenizi giriniz: ").strip().lower()

#result = (email == girilenEmail) and (sifre == girilenSifre)

#print(f"Girmiş olduğunuz e mail veya şifre doğru mu: {result}")

#4
#a = int(input("1.Sayı: "))
#b = int(input("2.Sayı: "))
#c = int(input("3.Sayı: "))
#result = (a > b) and (a > c)
#print(f"a en büyük sayıdır: {result}")
#result = (b > a) and (b > c)
#print(f"b en büyük sayıdır: {result}")
#result = (c > a) and (c > b)
#print(f"c en büyük sayıdır: {result}")



#5
#vize1 = int(input("Lütfen 1. Vizenizi Notunuzu Giriniz: "))
#vize2 = int(input("Lütfen 2. Vizenizi Notunuzu Giriniz: "))
#finall = int(input("Lütfen Final Notunuzu Giriniz: "))

#vizeler = ((vize1 + vize2) /2) * 0.6
#final = finall * 0.4
#ortalama = vizeler + final
#result = (ortalama > 50) and (finall >= 50) or (finall >= 70)
#print(f"Ders ortalamanız {ortalama}'dir. Geçtiniz mi: {result}")

#6
kisiAd = input("Lütfen adınızı giriniz: ")
kisiKilo = float(input("Lütfen kilonuzu giriniz: "))
kisiBoy = float(input("Lütfen boyunuzu giriniz: "))

index = (kisiKilo) / (kisiBoy**2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
kilolu = (index >= 25.0) and (index <= 29.9)
obez = (index >= 30.0) and (index <= 34.9)


print(f"{kisiAd} kilo indeksin {index} ve kilo değerlendirmen zayif: {zayif}")
print(f"{kisiAd} kilo indeksin {index} ve kilo değerlendirmen normal: {normal}")
print(f"{kisiAd} kilo indeksin {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{kisiAd} kilo indeksin {index} ve kilo değerlendirmen obez: {obez}")





