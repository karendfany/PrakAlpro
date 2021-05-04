#nama: keren dwi fani wulan sari
#nim:71200559

n = int(input("masukan jumlah kategori : "))
dict_kosong = dict()
for _ in range(n):
    kategori = input("Masukan nama kategori : ")
    set_kosong = set()
    for i in range(5):
        aplikasi = input("Nama Aplikasi : ")
        set_kosong.add(aplikasi)
    dict_kosong[kategori] = set_kosong


list_kosong = []

for i in dict_kosong.values():
    list_kosong.extend(i)

satu = set()
dua = set()

for j in set(list_kosong):
    if list_kosong.count(j) == 1:
        satu.add(j)
    elif list_kosong.count(j) == 2:
        dua.add(j)

    
if n > 2:
    print("Aplikasi yang sama tepat pada 2 kategori yaitu:", dua)

print("Aplikasi yang berbeda pada semua kategori yaitu:",satu)
