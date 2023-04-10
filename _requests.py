import requests

bozulanDoviz = input("Bozulan Döviz Türü Nedir?(USD,TRY) ")
alınanDoviz = input("Alınan Döviz Türü Nedir?(USD,TRY) ")
bozulanDovizMik = input("Ne kadar USD Doları bozdurmak istiyorsunuz? ")

if bozulanDoviz == alınanDoviz:
    print("Her iki tarafta aynı olduğu için işlem gerçekleşmedi")
        
if bozulanDoviz == "USD":
    for i in bozulanDovizMik:

        if int(bozulanDovizMik) <= 0:
            print("Yanlış bir değer girdiniz")
            break

        elif int(bozulanDovizMik) >= 0: 
            continue

islem = int(bozulanDovizMik) * 17,56

if alınanDoviz == "TRY":
    print("1 USD Doları: 17,56 TRY")
    print(f"{islem} kadar TRY sahibisiniz.")
   


            
if bozulanDoviz == "TRY":
    pass

if alınanDoviz == "USD":
    pass

