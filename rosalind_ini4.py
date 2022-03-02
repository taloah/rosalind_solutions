
suma = 0
data = './rosalind_ini4.txt'
f = open(data, 'r').readline().split()


numbers = [int(i) for i in f]

a, b = numbers

if a % 2 == 0:
    a += 1

while a <= b:
    suma += a
    a+=2

print(suma)
