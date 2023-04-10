maasAli = 5000
maasUmut = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasUmut - (maasUmut * vergi))

# Değişken Tanımlama Kuralları

# rakam ile başlayamaz

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30 
print(number1)

# Büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanmayalım

x = 1              # int
y = 2.3            #float
name = "Ali Baba"  #string
isStudent = True   #bool

x, y, name, isStudent = (1, 2.3, "Ali Baba", True) 

a = "10"
b = "20"
print(a+b)   #30 => 1020

firstName = "Mustafa Kemal"
lastName = " ATATÜRK"

print(firstName+lastName)   # Mustafa Kemal Atatürk


