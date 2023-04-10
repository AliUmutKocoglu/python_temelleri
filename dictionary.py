#key - value

#41 => kocaeli 

#sehirler = ["kocaeli", "istanbul"]
#plakalar = [41, 34]

#print(plakalar[sehirler.index("kocaeli")])
#print(plakalar[sehirler.index("istanbul")])

# print(plakalar["kocaeli"]) => 41

#plakalar = { "istanbul" : 34, "izmir" : 35 }
#print(plakalar["istanbul"])

#plakalar["ankara"] = 6

#print(plakalar)

users = {
    "selin" : {
        "age" : 25,
        "roles" : ["user"],
        "email" : "selin@gmail.com",
        "adress": "istanbul",
        "phone" : "05123456789"
    },
    "alibaba" : {
        "age" : 18,
        "roles" : ["admin", "user"],
        "email" : "kocoglualiumut@gmail.com",
        "adress": "ankara yenimahalle",
        "phone" : "05123456789"
    }
}

print(users["alibaba"]["age"])
print(users["alibaba"]["roles"][0])
print(users["alibaba"]["email"])
print(users["alibaba"]["adress"])
print(users["alibaba"]["phone"])