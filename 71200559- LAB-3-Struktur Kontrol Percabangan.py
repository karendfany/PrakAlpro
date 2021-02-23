#Keren Dwi Fani Wulan Sari  71200559
#Menghitung suhu badan pasien

print("===========MENHITUNG SUHU BADAN PASIEN============")
#masukkan inputan user

suhu_badan = input("Masukkan suhu badan: ")
try:
    suhu_badan = int(suhu_badan)
    if suhu_badan >=38:
        print ("Anda Demam")
    else:
        print("Anda tidak demam")
except:
    print("Masukkan suhu badan dalam bentuk angka! ")
