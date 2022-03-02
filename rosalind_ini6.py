'''
    Function
'''
def counter_words(string):
    result = ''
    for i in set(string):
        if i != '':
            result += i + ' ' + str(string.count(i)) + '\n'
    print(result)

data = './rosalind_ini6.txt'
file = open(data, 'r')
text = file.read().split()
file.close()

counter_words(text)
