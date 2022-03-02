file = open('./rosalind_ini3.txt', 'r').readlines()

words = file[0]
numbers = file[1].split()

numbers = [int(i) for i in numbers]

a, b, c, d = numbers

file.close()
print(words[a:b + 1] + ' ' + words[c:d + 1])
