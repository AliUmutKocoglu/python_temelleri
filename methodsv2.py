#class Person:
    #class attributes
#    address = "No information"
#
    #constructor (yapıcı metod)
#    def __init__(self, name, year):
#        #object attributes
#        self.name = name
#        self.birthyear = year
    
    #instance methods
#    def intro(self):
#        print("Hello There. I am "+ self.name)
#
    #instance methods
#    def calculateAge(self):
#        return 2022 - self.birthyear
        
#object (instance)
#p1 = Person(name="Ali", year=2003)
#p2 = Person("Yağmur", 1975)

#p1.intro()
#p2.intro()

#print(f"Adım: {p1.name} ve Yaşım: {p1.calculateAge()}")
#print(f"Adım: {p2.name} ve Yaşım: {p2.calculateAge()}")


class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    #Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1= Circle()
c2= Circle(5) 

print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")




