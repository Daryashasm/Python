import random
L = int(input('Введите длину массива, L = '))
array = []
sum = 0

for i in range (L):
    array.append(random.randint(1, 100))
print('Массив:', array)

for i in range (L):
    if (i % 2 != 0):
        sum = sum + array[i]
print(sum)


