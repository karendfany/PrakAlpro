#nama: keren dwi fani wulan sari
#nim: 712200559

#memasukkan variabel
bil = int(input("Masukkan bilangan: "))
bil*=2
for i in range(bil):
    print(" "*(bil-i-1),end="")
    if i != 0 and i != bil-1:
        for j in range(i*2+1):
            if j==0:
                print("*",end="")
            elif j==i*2:
                print("*")
            else:
                print(" ",end="")
    elif i==0:
        print("*")
    else:
        print("*"*(bil*2-1))
