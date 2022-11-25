#savol="Yaxshi ko'rgan kitobingizni kiriting"
#savol+="(Dasturni to'xtatish uchun stop deb yozing!\n>>>)"
#qiymat=" "
#while qiymat != "stop":
#    qiymat=input(savol)
#    qiymat=qiymat.lower()
#print("Dastur tugadi!")
#
#savol = 'Yoshingizni kiriting men sizga narhni belgilab beraman!\n'
#savol += "(Agar dasturni tugatmoqchi bo'lsangiz quit yoki exit deb yozing!)\n>>>"
#qiymat = True
#while qiymat:
#    qiymat=input(savol)
#    qiymat=qiymat.lower()
#    if qiymat =="exit" or qiymat == "quit":
#        qiymat=False
#    else:
#        if 0<int(qiymat)<7:
#            narh=2000
#            print(f"Siz uchun muzey bileti narhi {narh} so\'m")
#        elif 7<int(qiymat)<18:
#            narh=3000
#            print(f"Siz uchun muzey bileti narhi {narh} so\'m")
#        elif 18<int(qiymat)<65:
#            narh=8000
#            print(f"Siz uchun muzey bileti narhi {narh} so\'m")
#        else:
#            print('Siz uchun biletimiz bepul!')
#print('Dastur tugadi!')

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")