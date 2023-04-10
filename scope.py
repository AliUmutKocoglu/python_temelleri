# global scope
x = "global x"

def function():
    #locak scope
    #x = "local x"
    print(x)

function()
print(x)

#######################

name = "Ali"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Umut")
print(name)

#######################

name = "global string"

def greeting():
    #name = "Ali"

    def hello():
        #name = "Umut"
        print("hello " + name)
    
    hello()

greeting()

#######################

x = 50
def test():
    global x
    print(f"x {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)

