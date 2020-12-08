fileread = open("inputsegitiga.txt", "r")
splitted = fileread.read().split(' ')
angka = list(map(float, splitted))
luas = angka[0] * angka[1]/2
print("\nLuas Segitiga: ",luas)