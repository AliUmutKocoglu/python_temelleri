#1
#a = int(input("a: "))
#b = int(input("b: "))

#result = a > b

#print(f"a: {a} b: {b} den büyüktür: {result}")

#2
#v1 = float(input("vize1: "))
#v2 = float(input("vize2: "))
#f = float(input("final: "))

#Vizeler = ((v1 + v2) / 2) *0.6
#Final = f * 0.4
#result = Vizeler + Final

#print(f"not ortalamanız: {result} ve dersten geçme durmunuz: {result>50}")

#3
#sayi = int(input("Bir Sayı Giriniz: "))
#tekcift = sayi % 2 == 0
#print (f"girilen sayı çift olma durumu: {tekcift}")

#4
#sayi = int(input("Bir Sayı Giriniz: "))
#pozitifmi = (sayi > 0)
#print(f"girilen sayı pozitif olma durumu: {pozitifmi}")

#5
email = "kocoglu"
password = "abc123"

gemail = input("Lütfen e-mailinizi giriniz: ")
gpassword = input("Lütfen Şifrenizi Giriniz: ")

isEmail = gemail.lower().strip() == email
isPassword = gpassword.lower().strip() == password
print(f"Girmiş olduğunuz e-mail {isEmail} ve girmiş olduğunuz şifre {isPassword}")