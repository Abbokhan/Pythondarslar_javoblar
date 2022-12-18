#def katta_qil(ismlar):
#    ismlar1=[]
#    while ismlar:
#        ism=ismlar.pop()
#        ismlar1.append(ism.title())
#    return ismlar1
#a=['ali', 'bexruz', 'zafar', 'kamol']
#ismlar1=katta_qil(a[:])
#print(ismlar1)


#def katta_harf(ismlar):
#    ismlar=ismlar[:]
#    for a in range(len(ismlar)):
#        ismlar[a]=ismlar[a].title()
#    return ismlar

#ismlar=['ali','vali','samandar','guli']
#ismlar1=katta_harf(ismlar)
#print(ismlar)
#print(ismlar1)


#def katta_qil(ismlar):
#      ismlar=ismlar[:] 
#      for ism in range(len(ismlar)):
#        ismlar[ism]=ismlar[ism].title()
#      return ismlar


#ismlar=["abdulla qodiriy", 'amir temur', 'hulkar abdullayeva']
#talabalar=katta_qil(ismlar)
#print(ismlar)
#print(talabalar)




def bahola(ismlar):
        baholar = {}
        for a in ismlar:
            if ismlar:
                baho = input(f"Talaba {a.title()}ning bahosini kiriting: ")
                baholar[a]=int(baho)
            else:
                break
        return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)