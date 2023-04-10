from unittest import result


x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1
#a = int(input("1.sayı: "))
#b = int(input("2.sayı: "))

#result = (a * b) - (x+y+z)

#print(result)

#2
#y//=x    #y= y // x
#print(y)

#3
#result = (x + y + z) % 3
#print(result)

#4
#result = y ** x
#print(result)

#5
#x, *y, z = numbers
#z**= 3
#print(z)

#6
x, *y, z = numbers
result= y[0] + y[1] + y[2]
print(result)


