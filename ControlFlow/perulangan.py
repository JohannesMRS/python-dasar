
lanjutkan = True
while lanjutkan:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    operasi = input("pilih operasi (+, -, /, *): ")
    if operasi == "+":
        tambah = angka1 + angka2
        print("hasil penjumlahan: ", tambah)
    elif operasi == "-":
        kurang = angka1 - angka2
        print("hasil penjumlahan: ", kurang)
    elif operasi == "/":
        bagi = angka1 / angka2
        print("hasil penjumlahan: ", bagi)
    elif operasi == "*":
        kali = angka1 * angka2
        print("hasil penjumlahan: ",    kali)
    else:
        print("error")

    tanya = input("lagi? (y, t): ").lower()
    if tanya == "t":
        lanjutkan=False

