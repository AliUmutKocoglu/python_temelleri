import random
from secrets import choice

meterials = ("Taş", "Kağıt", "Makas")
rules1 = "Taş">"Makas", "Kağıt">"Taş", "Kağıt"<"Makas"
#numbers = [0,1,2]

#for numbers in meterials:

real = choice(meterials)
print(real)

answer = input("Taş,Kağıt,Makas?: ")

while meterials==answer or not answer<real or not answer>real:

    if (answer != "Taş" or "Kağıt" or "Makas"):
        print("Taş,Kağıt,Makas'dan biriniz yazmanız gerekiyor.")
        break

    elif answer == real:
        print("Tekrar Deneyiniz İkinizde Aynı Yaptınız.")
        real = choice(meterials)
        answer = input("Taş,Kağıt,Makas?: ")

    elif answer<real:
        print(f"Malesef Kaybettiniz Rakibiniz {real} Yapmıştı ve Siz {answer} Yaptınız.")
        break

    elif answer>real:
        print(f"Tebrikler Kazandınız Rakibiniz {real} Yapmıştı ve Siz {answer} Yaptınız.")
        break
    
    else:
        print("Taş,Kağıt,Makas'dan biriniz yazmanız gerekiyor.")
    
        

