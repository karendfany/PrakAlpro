#NIM: 71200559 / Nama: Keren Dwi Fani Wulan Sari
#mencari total keuntungan pada reseller

print("==========TOTAL KEUNTUNGAN RESELLER==========")

#memasukan variabel

A = int(input("Harga normal hoodie: "))
B = int(input("Harga untuk reseller: "))
C = int(input("Jumlah hoodie perkarung: "))

#lalu rumus
total = (A*C)-(B*C)
print("Total keuntungan yang diperoleh reseller perkarung hoodie adalah Rp ",total)
