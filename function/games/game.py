import random
while True:
  number_random = random.randint(1,4)
  bentuk_goa = "|_|"
  goa = [bentuk_goa] * 4
  goa_update = goa.copy() # Agar variabel goa original tidak terganggu
  goa_update[number_random-1] = "|0_0|"
  goa_update = ' '.join(goa_update)
  goa = ' '.join(goa)
  print("===========================================================")
  print(f'perhatikan goa dibawah ini \n {goa}')
  pilihan_user = int(input("Coba tebak di goa mana gajah bersembunyi [1/2/3/4]: "))
  while pilihan_user > 4 :
    print("Pilihan kamu melebihi batas broo")
    pilihan_user = int(input("isi ulang: "))

  print(f'Pilihan kamu adalah {pilihan_user}')

  if pilihan_user == number_random:
    print(f'{goa_update}\n kamu menang!')
  elif pilihan_user >= 1 and pilihan_user <=4:
    print(f'{goa_update} \n kamu kalah!')
  else:
      print("Angka yang dimasukkan melebihi batas")

  mau_lagi = input("Mau main lagi? [y/n]: ")
  if mau_lagi != "y":
        break
print("Program Selesai")