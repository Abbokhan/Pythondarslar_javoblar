#def sh_malumot(ism,familya,t_yil,t_joy,e_mail=None,tel_raqam=None):
#    """Foydalanuvchidan ma'lumot olib uni lug'at ko'rinishida qaytaruvchi funksiya"""
#    malumotlar={'ism' : ism,
#                'familya' : familya,
#                't_yil' : t_yil,
#                't_joy' : t_joy,
#                'e_mail' : e_mail,
#                'tel_raqam' : tel_raqam}
#    return malumotlar
        
#shaxs=sh_malumot('Abbos', "To'raqulov", 1997, "Koson")

#if shaxs['e_mail']==None and shaxs['tel_raqam']==None:
#    print(f"Ism:{shaxs['ism']}\n",
#          f"Familya:{shaxs['familya']}\n",
#          f"Tug'ilgan yili:{shaxs['t_yil']}\n",
#          f"Tug'ilgan joyi:{shaxs['t_joy']}\n")
#else:
#        print(f"Ism:{shaxs['ism']}\n",
#        f"Familya:{shaxs['familya']}\n",
#        f"Tug'ilgan yili:{shaxs['t_yil']}\n",
#        f"Tug'ilgan joyi:{shaxs['t_joy']}\n",
#        f"e_mail manzili:{shaxs['e_mail']}\n",
#        f"tel raqami:{shaxs['tel_raqam']}")


#mijozlar=[]
#while True:
#    print("Quyidagi ma'lumotlarni to'ldiring!")
#    ism=input("Ism: ")
#    familya=input("Familya: ")
#   t_yil=int(input("tug'ilgan yil: "))
#   t_joy=input("Tug'ilgan joyi: ")
#    e_mail=input("Emailingizni kiriting: ")
#    tel_raqam=input("Tel raqamingizni kiriting: ")
    
    
#    mijozlar.append(sh_malumot(ism,familya,t_yil,t_joy,e_mail=None,tel_raqam=None))
#    
#    javob=input("Mijoz qo'shasizmi yana? yes\no\n>>>")
#    if javob == 'no':
#        break
 

#def aylana_malumot(radius, pi=3.14):
#    aylana={
#        "radiusi":radius,
#        "diametri":2*radius,
#        "perimetri":2*radius*pi,
#        "yuzi":pi*radius**2}
#    return aylana
#print(aylana_malumot(4))   




def tub_sonlar1(x,y):
    tub_sonlar=[]
    for a in range(x,y+1):
        tub=True
        if a==1:
            tub=False
        if a==2:
            tub=True
        else:
            for b in range(2,a):
                if a%b==0:
                    tub=False
        if tub:
            tub_sonlar.append(a)
    return tub_sonlar

print(tub_sonlar1(4, 24))
        














