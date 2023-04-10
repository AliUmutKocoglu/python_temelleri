#1
#name = input("Lütfen İsminizi Giriniz: ").lower()
#age = int(input("Lütfen Yaşınızı Giriniz: "))
#edu = input("Lütfen Eğitim Bilgilerinizi Giriniz(Örneğin: Lise): ").lower()

#if (age >= 18) and (edu == 'lisans' or edu == 'lise'):
#    print(f"{name} Ehliyet alabilirsiniz.")
#elif age < 18:
#    print(f"{name} 18 yaşından küçük olduğunuz için ehliyet alamazsınız!!") 
#elif edu == "lisans" or "lise":
#    print(f"{name} Eğitim düzeyiniz yetmiyor")

#2
#yazili1 = int(input("Lütfen 1. Yazılı Notunu Giriniz: "))
#yazili2 = int(input("Lütfen 2. Yazılı Notunu Giriniz: "))
#sozlu = int(input("Lütfen Sözlü Notunu Giriniz: "))

#ortalama = (yazili1 + yazili2 + sozlu) / 3

#if (ortalama >= 85) and (ortalama <= 100):
#    print(f"Ders notunuz 5")
#elif (ortalama >= 70) and (ortalama <= 84):
#    print(f"Ders notunuz 4")
#elif (ortalama >= 55) and (ortalama <= 69):
#    print(f"Ders notunuz 3")
#elif (ortalama >= 45) and (ortalama <= 54):
#    print(f"Ders notunuz 2")
#elif (ortalama >= 25) and (ortalama <= 44):
#    print(f"Ders notunuz 1")
#elif (ortalama >= 0) and (ortalama <= 24):
#    print(f"Ders notunuz 0")
#else:
#    print("HATALI VEYA EKSİK GİRİŞ!!!!")

#3
import datetime

tarih = (input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): "))
tarih = tarih.split("/")

trafigeCigis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi= datetime.datetime.now()
fark = simdi - trafigeCigis
days = fark.days

if days <= 365:
    print(f"1.servis aralığı ve {days} gündür trafikte.")
elif (days >= 365) and (days <= 365*2):
    print(f"2.servis aralığı ve {days} gündür trafikte.") 
elif (days >= 365*2) and (days <= 365*3):
    print(f"3.servis aralığı ve {days} gündür trafikte.") 
else:
   print(f"Araç çok eski amk bi tamirciye götür ve {days} gündür trafikte.")




