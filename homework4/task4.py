from random import randint
import itertools
k = int(input('Задайте натуральную степень k: '))
array = list([randint(0, 101) for i in range(k+1)])
if array[0] == 0:
    array[0] = randint(1, 101)
def get_newArray(k, array):
    str1 = ['x^']*(k-1) + ['x']
    newArray = [[a, b, c] for a, b, c  in itertools.zip_longest(array, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in newArray:
        x.append(' + ') 
    newArray = list(itertools.chain(*newArray))
    newArray[-1] = ' = 0'
    return "".join(map(str, newArray)).replace('1x',' x')
list = get_newArray(k, array)
with open('task4.txt', 'w') as data:
    data.write(list)
