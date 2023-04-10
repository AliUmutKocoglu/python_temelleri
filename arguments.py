#def changeName(n):
#    n = "ada"

#name = "yiğit"

#changeName(name)
#print(name)

#def change(n):
#    n[0] = "istanbul"

#sehirler = ["ankara","izmir"]

#change(sehirler[:])

#print(sehirler)

#def add(*params):
#    sum = 0
#    for n in params:
#        sum += n

#    return sum

#print(add(10, 20))
#print(add(10, 20, 30, 50, 60, 10))


def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name = "Ali", age = 18, city = "Ankara", phone = "123321")
displayUser(name = "Çınar", age = 2, city = "İstanbul")
displayUser(name = "Yiğit", age = 14, city = "İzmir", phone = "313131", email = "yiğit@gmail.com")

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50,key1="value 1", key2="value 2")
