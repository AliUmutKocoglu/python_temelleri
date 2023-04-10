def notları_oku():
    with open("sinav_notlari.txt","r", encoding= "utf-8") as file:
       for satir in file:
           print(satir)
def notları_gir():
    ad = input("Öğrenci Adını Giriniz: ")
    soyad = input("Öğrenci Soyadını Giriniz: ")
    no = input("Öğrenci Okul Numarasını Giriniz: ")
    not1 = input("Öğrencinin Birinci Notunu Giriniz: ")
    not2 = input("Öğrencinin İkinci Notunu Giriniz: ")
    not3 = input("Öğrencinin Üçüncü Notunu Giriniz: ")

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write("Öğrenci Adı: " + ad + " " + soyad + " " + " Öğrenci Okul Numarası: " + no + "\n" + "Öğrencinin Birinci Notu: " + not1 + "\n" + "Öğrencinin İkinci Notu: " + not2 + "\n" + "Öğrencinin Üçüncü Notu: " + not3 + "\n")

while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Çıkış\n")

    if islem == "1":
        notları_oku()
    elif islem == "2":
        notları_gir()
    elif islem == "3":
        print("Çıkış yaptınız") 
        break
    else:
        print("Hatalı bir seçenek seçtiniz. Lütfen tekrar deneyiniz.")
        
