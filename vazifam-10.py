#davlatlar=['Janubiy Amerika', 'Portugaliya', 'Ispaniya', 'Kanada']
#sorted(davlatlar)
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar).


#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)


j_sonlar=list(range(120,1200,2))
#a=sum(j_sonlar)
#print(a)

#a=max(j_sonlar)
#b=min(j_sonlar)
#c=a-b
#print(c)

#a=j_sonlar[0:20]
#b=j_sonlar[265:285]
#c=j_sonlar[520:542]
#print(a,
#      b,
#      c)


taomlar=['sho\'rva', 'osh', 'manti', 'somsa', 'grechka']
nonushta=taomlar[:]
nonushta.remove('sho\'rva')
nonushta.remove('osh')
nonushta.remove('manti')

nonushta.append('tuxum')
nonushta.append('sut')

#print(taomlar)
#print(nonushta)

nonushta=tuple(nonushta)


nonushta=list(nonushta)

nonushta[1]='qaymoq va non'
