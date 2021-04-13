#nama: Keren Dwi Fani Wulan Sari
#nim: 71200559

handle = open("soal.txt")
x = []
y = []
for baris in handle:
    baris = baris.rstrip()
    x += baris.split(" || ")
    baris2 = baris.lower()
    y += baris2.split(" || ")
x.pop(1)
x.pop(2)
x.pop(3)
x.pop(4)
x.pop(5)
print("nama file: soal.txt")
n=1
for i in x:
    print(i)
    ans = str(input("jawab: "))
    ans = ans.lower()
    if ans == y[n]:
        print("jawaban benar!")
    else:
        print("jawaban salah!")
    n+=2
