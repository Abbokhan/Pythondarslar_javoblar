print("Mahsulot va uning narhlarini siz bilan belgilab chiqazmiz!")
mahsulotlar = {}
n=1
ishora=True
while ishora:
    mahsulot=input(f"{n}-mahsulotni kiriting!\n>>>")
    narh=input(f"{mahsulot}ning narhini kiriting!\n>>>")
    mahsulotlar[mahsulot]=int(narh)
    n+=1
    
    javob=input("Yana mahsulot qo'shasizmi?\n>>>")
    if javob == "yo'q":
        ishora = False
        
#for mahsulot,narh in mahsulotlar.items():
#    print(f"{mahsulot.title()}ning narhi {narh}")




buyurtmalar=[]
print("Buyurtmalaringizni kiriting!")
n=1
while True:
    buyurtma=input(f"{n}-Buyurtmangizni kiriting!\n>>>")
    buyurtmalar.append(buyurtma)
    savol=input("Buyurtmangizni davom ettirasizmi? xa\yo'q\n>>>")
    if savol == "xa":
        n+=1
        continue
    else:
        break
#print("Dastur tugadi")


while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh=mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}ning narhi {narh} so'm")
    else:
        print(f"Bizda {buyurtma} mavjut emas!")