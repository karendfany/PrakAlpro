#NAMA: Keren Dwi Fani Wulan Sari
#NIM: 71200559
#mencari banyaknya kata dalam suatu kalimat

#memasukkan variabel
karen=input("Masukkan kalimat: ")
cari=input("Masukkan kata yang ingin dicari: ")
karen=karen.lower()
cari_baru=cari.lower()
hasil=karen.count(cari_baru)
print("kata",cari,"ada",hasil,"buah")