#j_son=int(input("Juft son kiriting!\n>>>"))
#if j_son%2:
#    print("Bu juft son emas")
#else:
#    print("Raxmat")


#yosh = int(input("Yoshingizni kiriting!\n>>>"))
#if yosh<4 or yosh>60:
#    print("Siz uchun chipta bepul")
#elif yosh<18:
#    print("Siz uchun chipta 10000 so'm")
#else:
#    print("Siz uchun chipta 20000 so'm")

#print("Ikkita sonni kiriting!")

#son=float(input("Birinchi sonni kiriting\n>>>"))
#son1=float(input("Ikkinchi sonni kiriting\n>>>"))

#if son==son1:
#    print(f'{son}={son1}')
#elif son>son1:
#    print(f'{son}>{son1}') 
#elif son<son1: 
#    print(f'{son}<{son1}')

mahsulotlar=['non', 'salat', 'osh', 'sho\'rva', 'manti', 'shovla', 'makaron','kabob', 'shashlik', 'choy']
savat=[]
print('Istemol qilmoqchi bo\'lgan 5ta taomingizni kiriting!')
savat.append(input("Istemol qilmoqchi bo'lgan 1-taomingizni kiriting!\n>>>"))
savat.append(input("Istemol qilmoqchi bo'lgan 2-taomingizni kiriting!\n>>>"))
savat.append(input("Istemol qilmoqchi bo'lgan 3-taomingizni kiriting!\n>>>"))
savat.append(input("Istemol qilmoqchi bo'lgan 4-taomingizni kiriting!\n>>>"))
savat.append(input("Istemol qilmoqchi bo'lgan 5-taomingizni kiriting!\n>>>"))

if savat:
    for mahsulot in savat:
        if mahsulot.lower() in mahsulotlar:
            print(f"{mahsulot} oshxonamizda mavjud !")
        else:
            print(f"{mahsulot} oshxonada mavjud emas!")