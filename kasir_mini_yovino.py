print(" =====KASIR MINI=====")
nama2 = input("Nama barang: ")
nama3 = int(input("Harga barang: "))
nama4 = int(input("Jumlah barang: "))
nama5 = int(input("Masukkan uang pembayaran:"))

Total = nama3 * nama4

print("====TOTAL PEMBAYARAN====")
print("Nama barang:", nama2)
print("Harga barang:", nama3)
print("Jumlah barang:", nama4)
print("Total:", nama3 * nama4)
print("Uang kembalian:",nama5 - Total)