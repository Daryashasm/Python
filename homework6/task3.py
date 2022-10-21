import random
L = int(input('Введите размер массива: '))
array1 = []
array2 = []
x = 1
array1 = [random.randint(1, 10) for i in range(L)]
print('Исходный массив:', array1)
if L % 2 == 0:
    for i in range (L // 2):
        array2.append(array1[i] * array1[len(array1) - x])
        x = x + 1
else:
    for i in range((L + 1) // 2):
        array2.append(array1[i] * array1[len(array1) - x])
        x = x + 1
print('Массив произведений пар чисел:', array2)
