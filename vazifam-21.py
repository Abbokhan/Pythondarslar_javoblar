alisher_navoiy={
    'ism_familya':'Alisher Navoiy',
    't_yil':1441,
    'kasbi':'shoir',
    't_joyi':'qobul',
    'v_yil':1501,
    'asar':['xayrat-ul abror','sabbai-sayyor','saddi-iskandari']
    }
ozodbek_nazarbekov={
    'ism_familya':'Ozodbek Nazarbekov',
    't_yil':1974,
    'kasbi':'sanatkor',
    't_joyi':'Andijon',
    'v_yil':'Xozirda hayot',
    'asar':['Rayhon','mendirman jaloliddin']
    }
ortiq_otajonov={
    'ism_familya':'Ortiq Otajonov',
    't_yil':'1947',
    'kasbi':'sanatkor',
    't_joyi':'Xorazm',
    'v_yil':2019,
    'asar':['lazgi','sevgi']
    }
elon_mask={
    'ism_familya':'Elon Musk',
    't_yil':1971,
    'kasbi':'shoir',
    't_joyi':'AQSH',
    'v_yil':'Xozirda hayot',
    'asar':['tesla','delta']
    }

mashxurlar=[alisher_navoiy,ozodbek_nazarbekov,ortiq_otajonov,elon_mask]
for mashxur in mashxurlar:
    if mashxur['v_yil'] != str(mashxur['v_yil']):
        print(f"{mashxur['ism_familya'].title()} {mashxur['t_yil']}-yilda {mashxur['t_joyi'].title()}da tug'ilgan, kasbi {mashxur['kasbi'].title()},{mashxur['v_yil']}-yilda vafot etgan, uning eng mashxur asari:")
    else:
        print(f"{mashxur['ism_familya'].title()} {mashxur['t_yil']}-yilda {mashxur['t_joyi'].title()}da tug'ilgan, kasbi {mashxur['kasbi'].title()},{mashxur['v_yil']}, uning eng mashxur asari:")
        
        