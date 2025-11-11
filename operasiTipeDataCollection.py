num =[1, 2, 3, 4, 5, 6, 7, 7]

print(len(num))


num2 = set([1, 2, 3, 4, 5, 6, 7, 7])
print(num2)
print(len(num2))

num3 = (1, 2 ,3, 4)
print(type(num3))


listData = [1, "johannes", "Boxer", 3]

num4, str1, str2, num5= listData
print(num4, str1, str2, num5)


jenis = listData[1]
print(f"halo nama saya {jenis}")


# Mengurutkan data (sort) bisa angka atau huruf

data = [2, 3, 4, 1, 8, 7, 10, 11, 1]
data.sort()
print(data)

dataHuruf = ["jo", "ha", "nes"]
dataHuruf.sort()
print(dataHuruf)

# Membalikkan Urutan
dataHuruf.sort(reverse=True)
print(dataHuruf)

# Tidak bisa mengurutkan jika angka dan huruf berada di list yg sama 
# dataMix = [1, "jo", 3]
# dataMix.sort()
# print(dataMix) // Output: Error


var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

print(len(var_list))

max = max(var_list)
print(max)

min = min(var_list)
print(min)

banyak = var_list.count(605132)
print(banyak)
print(dict([['name','Dicoding'],['age',17]]))