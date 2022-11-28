buyurtmalar=[]
n=1
while True:
    buyurtma=input(f"{n}-Buyurtmangizni kiriting!\n>>>")
    buyurtmalar.append(buyurtma)
    savol=input("Buyurtma qilishda davom etaszmi? (xa\yo'q)\n>>>")
    n+=1
    if savol != 'xa':
        break


e_bozor={}

print("Elektron bozorimiz uchun mahsulot va mahsulot narhlarini kiritamiz!")
while True:
    mahsulot=input("Mahsulotni kiriting!\n>>>")
    narh=int(input(f"{mahsulot.title()}ning narhini kiriting!\n>>>"))
    e_bozor[mahsulot]=narh
    savol=input("Yana mahsulot haqida ma'lumot kiritasizmi? (xa\yo'q)\n>>>")
    if savol != 'xa':
        break

while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in e_bozor.keys():
        narh=e_bozor[buyurtma]
        print(f"Bizda {buyurtma} mavjud, uning narhi {narh} so'm!")
    else:
        print(f"Bizda {buyurtma} mavjud emas!")