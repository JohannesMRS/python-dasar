# Numbers
# integer, float, complex

print("==== Int ====")
numberInt = 12 #integer
print(numberInt, type(numberInt))

numberInt = 12.0 #float
print(numberInt, type(numberInt))

numberInt = 12j #complex
print(numberInt, type(numberInt))


#Boolean

print( )
print("==== Boolean ====")
decision = True
print(decision, type(decision))

# String

print( )
print("==== String ====")
name = "Johannes"
print(name, type(name))

# Akses karakter string (indexing)
print(name[4])
# Akses beberapa karakter string (slicing)
print(name[4:])
print(name[4:7])

# Formatted String
# Memasukkan variabel ke dalam perintah eksekusi
print(f"Halo nama saya {name}")
print("Halo nama saya %s" % (name))
print("Halo nama saya {}" . format(name))


# Collection
# List
print()
print("==== List ====")
list1 =["Johannes", 2, True]
 

# Indexing
print(list1[0])
# indexing dari belakang
print(list1[-1])

 # Mengubah data di dalam list1
list1[1] = "AI Engineer"
print(list1, type(list1))

list2 = [1, 2, 3, 4, "jo", "ha", "nes"]

# Slicing
# Start:stop:step
# Start, dimulai dari mana, bersifat inklusif (a >= b)
# Stop, berhenti sampai mana, bersifat eksklusif (a > b)
# Step, mau melewati berapa data

print(list2[0: :2])
print(list2[2: ])
print(list2[:3 ])


# Tuple
print()
print("==== Tuple ====")

tup = (1, 'johannes', True, 0.2, 2j)
print(tup, type(tup))

# Indexing
print(tup[2])
print(tup[1:])


# Set
print()
print("==== Set ====")

set1 = {1,2,2,3,4,5,6,7,8,2,1,9}
print(set1, type(set))
set2 = {2, 3, 4, 5, 1, 7, 6, 8}
# Union (Gabungan)
union = set1.union(set2)
print("Union: ", union)

# Intersection (Irisan)
intersection = set.intersection(set2)
print("intersection: ", intersection)


# Dictionary
print()
print("==== Dictionary ====")

dict1 = {'Name': 'Johannes', 'Nim':'2405102086', 'Umur':'20'}
print(dict1, type(dict1))

# Menambah data baru
dict1['Alamat'] = 'Jl.Bahagia'
print(dict1)

# Mengahpus satu data
del dict1['Alamat']
print(dict1)

# update data

dict1['Name'] = 'Johannes M'
print(dict1)

print()
print("==== Konversi Tipe Data ====")

print(int(7.8)) # float to int
print(float(5)) # int to float
print(str(25)) # int to str
print(int("25")) # str to int
print(str(24.5)) # float to str
print(float("24.5")) # str to float

print(set([1,2,3])) # list to Set 
print(tuple({1,2,3})) # set to tuple
print(list('Hello')) # set to list

print(dict([["nama" , "johannes"], ["umur", "18"]])) # list to dictionary
print(dict([("alamat", "jl.bahagia"), ("email", "ch@gmail.com")])) # tuple in list to dictionary