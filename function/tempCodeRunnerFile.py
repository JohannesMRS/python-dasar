
  goa = [bentuk_goa] * 4
  goa_update = goa.copy() # Agar variabel goa original tidak terganggu
  goa_update[number_random-1] = "|0_0|"
  goa_update = ' '.join(goa_update)
  goa = ' '.join(goa)