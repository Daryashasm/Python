import random
L = int(input('Введите длину массива, L = '))
array = [random.randint(1, 100) for i in range (L)]
print('Массив:', array)
even = [y for x, y in enumerate(array) if x % 2 != 0]
print('Массив:', even)
def sum(x):
    sum = 0
    for i in range (len(x)):
        sum = sum + x[i]
    return sum
print('Сумма элементов, находящихся на нечетных позициях', sum(even))