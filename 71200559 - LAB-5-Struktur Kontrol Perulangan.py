#NAMA: Keren Dwi Fani Wulan Sari
#NIM: 71200559

def hitung_jumlah(string):
    total1=0
    total2=0
    total3=0
    for i in "abcdefghijklmnopqrstuvwxyz":
        jml1=string.count(i)
        total1+=jml1
    print("Jumlah huruf kecil :",total1)
    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        jml2=string.count(j)
        total2+=jml2
    print("Jumlah huruf besar :",total2)
    for k in " ":
        jml3=string.count(k)
        total3+=jml3
    print("Jumlah spasi :",total3)
karen=input("Masukkan kalimat: ")
hitung_jumlah(karen)
