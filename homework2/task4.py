import random
N = int(input('Введите N: '))
array = []
repeat = [0] * 100
for i in range(N):
    array.append(random.randint(1, 99))
    repeat[array[i]] = repeat[array[i]] + 1
    while repeat[array[i]] > 1:
        array[i] = random.randint(1, 99)
print('Исходный массив:', array)
for i, value in enumerate(array):
    swap = random.randint(i, len(array) - 1)
    array[i], array[swap] = array[swap], value
print('Массив после перемешивания:', array)