#my_list = [1,2,3]
#my_list = ["bir", 2, True, 5.6]
#print(my_list)

#list1 = ["one", "two", "three"]
#list2 = ["four", "five", "six"]

#numbers = list1 + list2
#print(numbers)
#print(len(numbers))

#list = ["Bmw", "Mercedes", "Opel", "Mazda"]
#result = len(list)
#result = list[0]

#print(result)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

result = studentA[0], studentB[2], studentC[3][2]

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)