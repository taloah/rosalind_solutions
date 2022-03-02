import math
'''
    Path of dataset
'''
data = './rosalind_ini2.txt'


'''
    Function that receives two sides and return the square of hyp
'''
def square(a,b):
    return math.pow(a,2) + math.pow(b, 2)

'''
    Open file to read the dataset
'''
file = open(data, 'r')
content = file.read()

'''
    Get the content of dataset and put on a list... and convert the list of strings to integers
'''
list_numbers = content.split()
list_numbers = [int(i) for i in list_numbers]

'''
    Don't forget close the file
'''
file.close()

'''
    Print the result
'''
print(square(list_numbers[0], list_numbers[1]))
