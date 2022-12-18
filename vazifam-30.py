def oraliq(min,max,farq=''):
    """Foydalanuvchi o'z ixtiyori bilan kiritigan sonlarining oralig'idagi sonlarning ro'yxatini beradiga funksiya"""
    a=[]
    while min<max:
        if farq:
            farq=int(farq)
            a.append(min)
            min+=farq
        else:
            a.append(min)
            min+=1
    return a
print(oraliq(3,87,12))