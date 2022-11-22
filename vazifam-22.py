royxat={
    'alisher_navoiy':{
    'ism_familya':'Alisher Navoiy',
    't_yil':1441,
    'kasbi':'shoir',
    't_joyi':'qobul',
    'v_yil':1501,
    'asar':['xayrat-ul abror','sabbai-sayyor','saddi-iskandari']
    },
'ozodbek_nazarbekov':{
    'ism_familya':'Ozodbek Nazarbekov',
    't_yil':1974,
    'kasbi':'sanatkor',
    't_joyi':'Andijon',
    'v_yil':'Xozirda hayot',
    'asar':['Rayhon','mendirman jaloliddin']
    },
'ortiq_otajonov':{
    'ism_familya':'Ortiq Otajonov',
    't_yil':'1947',
    'kasbi':'sanatkor',
    't_joyi':'Xorazm',
    'v_yil':2019,
    'asar':['lazgi','sevgi']
    },
'elon_mask':{
    'ism_familya':'Elon Musk',
    't_yil':1971,
    'kasbi':'shoir',
    't_joyi':'AQSH',
    'v_yil':'Xozirda hayot',
    'asar':['tesla','delta']
    }
}
for mashxur, asarlar in royxat.items():
    if asarlar['v_yil'] != str(asarlar['v_yil']):
        print(f"{asarlar['ism_familya'].title()} {asarlar['t_yil']}-yilda {asarlar['t_joyi'].title()}da tug'ilgan, kasbi {asarlar['kasbi'].title()},{asarlar['v_yil']}-yilda vafot etgan, uning eng mashxur asari:")
    else:
        print(f"{asarlar['ism_familya'].title()} {asarlar['t_yil']}-yilda {asarlar['t_joyi'].title()}da tug'ilgan, kasbi {asarlar['kasbi'].title()},{asarlar['v_yil']}, uning eng mashxur asari:")
    for asar in asarlar['asar']:
        print(f"{asar.title()}")