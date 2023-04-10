#def greeting(name):
#    print("hello", name)

#print(greeting("ali"))
#print(greeting)

#sayHello = greeting

#print(sayHello)
#print(greeting)

#del sayHello
#print(greeting)

# encapsulation
#def outer(num1):
#    def inner_increment(num1):
#        return num1 + 1
#    num2 = inner_increment(num1)
#    print(num1,num2)

#outer(10)


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an intager")

    if not number >= 0:
        raise ValueError("number must be one or positive")

    def inner_factorial(number):
        if number<=1:
            return 1
        
        return number*inner_factorial(number-1)

    return inner_factorial(number)

print(factorial(3))