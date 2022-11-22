ticolar=[]
for a in range(5):
    yangi_mashina={
        'turi':"tico",
        'rangi':None,
        'narhi':0,
        'karobka':None
        }
    ticolar.append(yangi_mashina)
for tico in ticolar[:2]:
    tico['rangi']='oq'
    tico['karobka']='avto'
for tico in ticolar[2:]:
    tico['rangi']='qora'
    tico['karobka']='mexanik'
for tico in ticolar:
    if tico['rangi']=='oq':
     tico['narhi']=11000
    else:
     tico['narhi']=10000
print(ticolar)