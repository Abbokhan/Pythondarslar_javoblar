onam={
      'ism'  : 'Feruza',
      't_yil': '1973',
      't_joy': 'Koson'
      }
print(f"Onamning ismlari {onam['ism']}, {onam['t_yil']}-yilda {onam['t_joy']} shaxrida tug'ilganlar")

atir_gul={
    'rang':'qizil',
    'sifat':'chiroyli',
    'narh': '15000'
    }
print(f"Men bu {atir_gul['rang']} rangdagi {atir_gul['sifat']} atirgulni {atir_gul['narh']} so'm oldim.")


s_taomlar={
    'onam':'osh',
    'otam':'sho\'rva',
    'akam':'manti',
    'singlim':'mosh',
    'yangam':'makaron'
    }
print(f"Onam {s_taomlar['onam']}ni,\
otam {s_taomlar['otam']}ni,\
akam {s_taomlar['akam']}ni,\
yangam {s_taomlar['yangam']}ni yoqtirishadi.")


lugat={
      'integer':'butun son',
      'float':'qoldiqlik son',
      'title':'xar bir so\'ning bosh harfini katta qiladi',
      'input':'foydalanuvchidan ma\'lumot so\'rash',
      'append':'ro\'yxatga o\'zgaruvchi qo\'shadi',
      'string':'matn ko\'rinishidagi o\'zgaruvchi',
      'capitalize':'gapning faqat bosh harfini katta qiladi',
      'upper':'so\'zning hamma harfini katta qilib beradi',
      'for':'uchun',
      'in':'ichida'
      }

soz=input("Biror so'z kiriting!\n>>>")
if soz in lugat:
    print(f'{lugat[soz]}')
else:
    k_soz=lugat.get(f'{soz}','Bunday so\'z lug\'atda mavjud emas')
    print(k_soz)

