hesapAli = {
    "ad": "Ali Umut Koçoğlu",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ekHesap": 2000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alınız.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı? (e/h)")
            
            if ekHesapKullanimi == "e":
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar 
                print("Paranızı alınız")
            else:
                print(f"{hesap['hesapNo']} noldu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
                print(f"{hesap['hesapNo']} noldu hesabınızda yeterli bakiye yok.")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(hesapAli, 3000)
bakiyeSorgula(hesapAli)
print("**********************")
paraCek(hesapAli, 2000)
bakiyeSorgula(hesapAli)
