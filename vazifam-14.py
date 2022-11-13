#mahsulotlar=["karam", 'sabzi', 'kola', 'jo\'xori', 'fanta', 'lavlagi', 'mandarin', 'guruch', 'go\'sht', 'olma']
#savat=[]
#print("Kamida 5ta mahsulot kiriting!")
#for mahsulot in range(5):
#    savat.append(input(f'{mahsulot+1}-mahsulotni qo\'shing\n>>>'))
#for mahsulot in savat:
#    if mahsulot.upper() in mahsulotlar:
#        print(f'{mahsulot} do\'konimizda bor')
#    else:
#        print(f'{mahsulot} do\'konimizda yo\'q')

#bor_mahsulotlar=[]
#mavjud_emas=[]
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#      bor_mahsulotlar.append(mahsulot)
#    else:
#      mavjud_emas.append(mahsulot)

#if mavjud_emas:
#    print("Quyidagi mahsulotlar do\'konimizda mavjud emas!")
#    for mahsulot in mavjud_emas:
#         print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud")




foydalanuvchilar=["Azim000", "Abbos4067",'Samandar','Qirol Artur', 'Portugal7']
print("Yangi login qo'shing!")
login=input("Loginingizni kiriting!\n>>>")
if login.title() in foydalanuvchilar:
        print("Bunday login avval band qilingan!")
else:
        print("Xush kelibsiz!!!")