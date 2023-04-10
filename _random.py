import random

#result = dir(random)

result = random.random() * 100
result = random.uniform(1,10)
result = random.randint(1,100)

greeting = "hello there"
names = ["ali", "yağmur", "deniz", "cenk"]
result = names[random.randint(0,3)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))

result = liste
random.shuffle(liste)

liste = range(100)
result = random.sample(liste,3)
result = random.sample(names,2)

print(result)
