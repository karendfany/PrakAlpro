import random

def duplikat(t):
    #Return True jika ada elemen muncul lebih dari sekali dalam (t)
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def ultah(n):
    #Return list berisi integer dari 1 dan 365, dengan panjang (n)
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def cocok(mahasiswa, sampel):
    #generalisasi sampel setiap orang, dan hitung berapa banyak dari mereka yang setidaknya memiliki 1 pasang orang dengan ultah yang sama
    hitung = 0
    for i in range(sampel):
        t = ultah(mahasiswa)
        if duplikat(t):
            hitung += 1
    return hitung

#Lakukan simulasi sebanyak 1000 kali dan print yang cocok
jumMahasiswa = 20
totalSimulasi = 1000
hitung = cocok(jumMahasiswa, totalSimulasi)

print('Setelah dilakukan simulasi sebanyak %d simulasi' % totalSimulasi)
print('Dengan total mahasiswa %d orang' % jumMahasiswa)
print('Ada %d simulasi dengan setidaknya 1 pasang mahasiswa ultah yang sama' % hitung)
 
