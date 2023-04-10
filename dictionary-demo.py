ogrenciler = {
    "120" : {
        "ad" : "Ali Umut",
        "soyad" : "Koçoğlu",
        "telefon" : "5123456789"
    },
    "125" : {
        "ad" : "Selin",
        "soyad" : "Koçoğlu",
        "telefon" : "5123456789"
    },
    "128" : {
        "ad" : "Umut",
        "soyad" : "Koçoğlu",
        "telefon" : "5123456789"
    },
}

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

#ogrenciler[number] = {
#    "ad" : name,
#    "soyad" : surname,
#    "telefon" : phone,
#}
                           #ikiside aynı alltaki daha işlevli
ogrenciler.update({
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone,
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone,
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone,
    }
})
print("*"*50)

ogrNo = input["öğrenci no: "]
ogrenci = ogrenciler["ogrNo"]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci["ad"]} soyadı: {ogrenci["soyad"]} ve telefonu ise {ogrenci["teleofon"]}")