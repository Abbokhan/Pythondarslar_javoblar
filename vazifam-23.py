dostlar={'ali':[],
         'vali':[],
         'hasan':[]
    }
print('3ta sevimli kinongizni kiriting')
for dost in range(3):
    dostlar['ali'].append(input(f'Ali {dost+1}-kinoni qo\'shing:'))
for dost in range(3):
    dostlar['vali'].append(input(f'Vali {dost+1}-kinoni qo\'shing:'))
for dost in range(3):
    dostlar['hasan'].append(input(f'Hasan {dost+1}-kinoni qo\'shing:'))

for dost,kinolar in dostlar.items():
    print(f"{dost.title()} quyidagi kinolarni yoqtirar ekan:")
    for kino in kinolar:
        print(kino)

    