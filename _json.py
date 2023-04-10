import json

person_stirng = '{"name":"Ali", "languages":["Python","C#"]}'

#result = json.loads(person_stirng)
#result = result["name"]
#result = result["languages"]

person_dict = {
    "name":"Ali", 
    "languages":["Python","C#","C++"]
}

result = json.dumps(person_dict)
print(result)