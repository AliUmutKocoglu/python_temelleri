# value types => string, number   #sonraki değişken ilk değişkeni etkilemez
x = 5
y = 25

x = y

y = 10

#print(x,y)

# reference types => list      #burada etkiliyor
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)