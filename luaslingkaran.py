import math
fileread = open("inputlingkaran.txt", "r")
splitted = fileread.read().split(' ')
jari = list(map(float, splitted))
luas = math.pi*jari[0] * jari[1]
print("\nLuas Lingkaran: ",luas)