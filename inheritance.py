# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

import numbers


class Person():
    def __init__(self, fname, lname):
        self.firstName=fname
        self.lastName=lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")
    
    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created") 
        

    #override
    def who_am_i(self):
        print("I am a student")

    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch=branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")
        


p1=Person("Ali Umut", "Koçoğlu")
s2=Student("Selin", "Koçoğlu", 1234)
t1=Teacher("Mustafa Kemal", "Atatürk", "CENG")

print(p1.firstName + " " + p1.lastName)
print(s2.firstName + " " + s2.lastName+ " " + str(s2.studentNumber))

p1.who_am_i()
s2.who_am_i()
p1.eat()
s2.eat()
s2.sayHello()
t1.who_am_i()


