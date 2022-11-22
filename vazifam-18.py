#lugat={
#      'integer':'butun son',
#      'float':'qoldiqlik son',
#      'title':'xar bir so\'ning bosh harfini katta qiladi',
#      'input':'foydalanuvchidan ma\'lumot so\'rash',
#      'append':'ro\'yxatga o\'zgaruvchi qo\'shadi',
#      'string':'matn ko\'rinishidagi o\'zgaruvchi',
#      'capitalize':'gapning faqat bosh harfini katta qiladi',
#      'upper':'so\'zning hamma harfini katta qilib beradi',
#      'for':'uchun',
#     'in':'ichida'
#      }
#for a,b in sorted(lugat.items()):
#    print(f"{a}-{b}")

davlatlar={'Argentina':'Buanos Aeros',
              'O\'zbekiston':'Toshkent',
              'Portugaliya':'Lissabon',
              'Rossiya':'Moskva'
              }
#print('Davlatlar:')
#for a in sorted(davlatlatlar.keys()):
#    print(a.upper())
#print("\nDavlarlar poytaxtlari:")
#for b in sorted(davlatlatlar.values()):
#    print(b.title())

#davlat=input("Istalgan davlatni kiriting mensizga o'zimga bor ma'lumotdan foydalanib davlatning poytaxtini aytaman!\n>>>")
#if davlat.title() in davlatlar:
#    print(f"Siz so'ragan davlatning poytaxti {davlatlar[davlat.title()].title()}" )
#else:
#    print("Bizda bunday ma'lumot yo'q")

menu={'osh':'38000',
         'sho\'rvo':'10000',
         'somsa':'5000',
         'g\'elak':'7000',
         'manti':'3000',
         'tuxum-sasiska':'10000',
         }
buyurtma=[]
for b in range(3):
    buyurtma.append(input(f"{b+1}-buyurtmangizni kiriting!\n>>>"))
for c in buyurtma:
     if c.lower() in menu:
         print(f"{c.title()}-{menu[c.lower()]}")
     else:
         print(f"Bizda {c.title()} yo'q")