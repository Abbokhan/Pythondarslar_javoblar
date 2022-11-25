davlatlar={
    'uzbekistan':{'poytaxt':'toshkent',
                  'aholisi':36000000,
                  'hududi':'448000 kv.m',
                  'pul birligi':'so\'m'},
    'xitoy':{'poytaxt':'pekin',
             'aholisi':1336000000,
             'hududi':'9.6 mln kv.m',
             'pul birligi':'yuan'},
    'aqsh':{'poytaxt':'new york',
            'aholisi':336000000,
            'hududi':'9.8 mln kv.m',
            'pul birligi':'aqsh dollar'}
    }
davlat=input("Xoxlagan davlatingizni kiriting:\n>>>").lower()
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"Poytaxti:{info['poytaxt']},\n"
          f"Aholisi:{info['aholisi']},\n"
          f"Hududi:{info['hududi']},\n"
          f"Pul birligi:{info['pul birligi']}")
else:
    print(f"Bizda {davlat} haqida ma'lumot yo'q!")