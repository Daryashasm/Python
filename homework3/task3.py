import math
import random
L = int(input('Введите длину массива, L = '))
array = []
max = 0
min = 1
diff = 0

for i in range (L):
    array.append(round(random.uniform(0, 100)*0.10, 2))
print('Массив:', array)

for i in range (L):
    whole = round(array[i] - int(array[i]), 2)
    if (whole >= max):
        max = whole
    elif (whole <= min and whole != 0):
        min = whole
print('Максимальное значение дробной части:', max)
print('Минимальное значение дробной части:', min)

diff = round(max - min, 2)
print('Разница между ними:', diff)