#nama: keren dwi fani wulan sari
#nim: 71200559
#menghitung luas segiempat

def luas(x,y):
    hitung=0
    for i in range(x):
        for j in range(1,y+1):
            hitung+=1
            print(hitung,end="\t")
        print()
tinggi=int(input("Masukkan tinggi: "))
lebar=int(input("Masukkan lebar: "))
luas(tinggi,lebar)