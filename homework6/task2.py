import random
L = int(input('Введите длину массива, L = '))
array = []
for i in range (L):
    array.append(random.randint(1, 100))
print('Массив:', array)
even_numbers = [y for x, y in enumerate(array) if x % 2 != 0]
print('Массив:', even_numbers)
def sum(x):
    sum = 0
    for i in range (len(x)):
        sum = sum + x[i]
    return sum
print('Сумма элементов, находящихся на нечетных позициях', sum(even_numbers))