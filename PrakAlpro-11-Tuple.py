#NAMA: Keren Dwi Fani Wulan Sari
#NIM: 71200559

data =('Keren Dwi Fani','71200559','Tulungagung')

#print tuple data
print('data\t\t:',data)
print()

#print tiap data berdasarkan indeks yang mau diambil
print('NIM\t\t:',data[1])
print('NAMA\t\t:',data[0])
print('ALAMAT\t\t:',data[2])
print()

#konversi string ke tuple lalu print
nim = tuple('71200559')
print('NIM\t\t:',nim)
print()

#nama depan kurang satu huruf
nama1 = tuple('Keren Dwi Fani')
print('NAMA DEPAN\t:',nama1[1:5])

#print tuple terbalik memakai indeks, bisa memakai reverse True
nama2 = ('Keren','Dwi','Fani')
terbalik = nama2[::-1]
print('NAMA TERBALIK\t:',terbalik)
