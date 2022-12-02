def t_yil():
    """Foydalanuvchidan ism va yoshini so'rab tug'ilgan"""
    """yilini chiqarib beradigan dastur"""
    ism=input("Ismingizni kiriting!\n>>>")
    yosh=int(input(f"{ism.title()} yoshingizni ham kiriting!\n>>>"))
    print(f"{ism.title()} Sizning tug'ilgan yilingiz {2022-yosh}")
t_yil()


#def son():
#    """Foydalanuvchidan son olib, uning kvadrati va kubini hisoblaydigan funksiya"""
#    son1=int(input("Biror sonni kiriting\n>>>"))
#    print(f"{son1}ning kvadrati {son1**2}",
#          f"{son1}ning kubi {son1**3}")
#son()