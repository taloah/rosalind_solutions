data = './rosalind_ini5.txt'

f = open(data, 'r')

lines = f.readlines()

for line in lines[1::2]:
        print(line)


f.close()
