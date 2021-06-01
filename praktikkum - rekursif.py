#71200559_Keren Dwi Fani Wulan Sari

def jagaJarak(awal, listnya, hasil):
    if(hasil == 0):
        return True
    if(awal >= len(listnya)):
       return False
    if(jagaJarak(awal+2, listnya, hasil - listnya[awal])):
        return True
    return jagaJarak(awal + 1, listnya , hasil)

print(jagaJarak(0, [5, 7, 11, 4], 16))
print(jagaJarak(0, [5, 7, 11, 4], 15))
print(jagaJarak(0, [5, 7, 11, 4], 9))
print(jagaJarak(0, [5, 7, 11, 4], 18))
