#nama: keren dwi fani wulan sari
#nim: 71200559

with open('mbox-short.txt','r') as f:
    dictionary = {}
    for kalimat in f:
        kata = kalimat.split()
        if 'From' in kata and len(kata)>2:
            if kata[1] not in dictionary:
                dictionary[kata[1]] = 1
            else:
                dictionary[kata[1]] += 1
print(dictionary)
