'''BINER adalah ekspresi yang berisi dua operand yang di jalankan dengan operator'''
'''UNER adalah ekspresi yang berisi satu operand '''


# Biner
a = 5
b = 6
c = a + b
print("Hasil Biner: ", c)


# Uner
d = 2
d += 1
print("Hasil Uner: ", d)

nilai = int(input("masukkan nilai: "))

if nilai >= 90 and nilai <=100:
    print("Nilai A")
elif nilai >= 80 and nilai <90:
    print("Nilai B")
else:
    print("error")