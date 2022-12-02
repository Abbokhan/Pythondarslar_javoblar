#def t_yil():
#    """Foydalanucchidan ism va yoshini so'rab tug'ilgan yilini chiqrib"""
#    """beruvchi funksiya"""
#ism=input("Ismningizni kiriting!\n>>>")
#yosh=int(input(f"{ism.title()} yoshingizni kiriting!\n>>>"))
#print(f"{ism.title()} siz {2022-yosh}-yilda tug'ilgansiz")

#t_yil()


#def kv_kub(son):
#    """Foydalanuvchidan son so'rab sonning kvdratini va kubini chiqarib"""
#    """beruvchi dastur"""
#    print(f"{son}ning kvadrati: {son**2}\n",
#      f"{son}ning kubi: {son}")

#kv_kub(1)

#kv_kub()

#def juft_toq(son):
#    """Foydalanuvchidan son so'rab sonning juft yoki toqligimi chiqarib beruvchi dastur"""
#    if son%2:
#        print("Kiritgan soningiz toq son")
#    else:
#        print("Kiritgan soningiz juft son")
   
#juft_toq(56)



#def son_kat_kich(son1,son2):
#    """Foydalanuvchidan ikkita son so'rab ularni qaysi kattaligini topib beruvchi funksiya"""
#    if son1>son2:
#      print(f"Kiritgan sonlarizdan kattasi {son1} ")
#    elif son2>son1:
#      print(f"Kiritgan sonlarizdan kattasi {son2} ")
#    elif son1==son2:
#      print("Kiritgan sonlariz teng! ")
    

#son_kat_kich(12,13)




#def daraja(x,y=2):
#    """ Foydalanuchidan ikkita x va y son so'rab x ning y darajasini topin beradigan funksiya """
#    print(f"{x}ning {y}-darajasi:{x**y}")



#daraja(5)

def q_son(son):
    """Foydalanuvchidan son so'rab sonning 2dan 10gacha bo'lgan sonlarga qoldiqsiz bo'linishini chiqarib beruvchi dastur"""
    for a in range(2,11):
        if not son%a:
            print(f"{son} {a}ga qoldiqsiz bo'linadi!")
q_son(64)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
