class Person:
    #class attributes
    address = "No information"

    #constructor (yapıcı metod)
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.birthyear = year
    
    #methods
    def intro():
        print("Hello There")
        
#object (instance)
p1 = Person(name="Ali", year=2003)
p2 = Person("Yağmur", 1975)

#updating
p1.name = "Umut"
p1.address = "Ankara"

#accessing object attributes
print(f"name: {p1.name} year: {p1.birthyear} address: {p1.address}")
print(f"name: {p2.name} year: {p2.birthyear} address: {p2.address}")


print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)




