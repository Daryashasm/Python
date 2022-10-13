# import math
# d = int(input('Задайте количество знаков после запятой, d = '))
# ans = round(math.pi, d)
# d = (d / d) / (10 ** d)
# print('Число π = ', ans,'с точностью d = ', d)

import math
d = float(input('Задайте точность числа, d = '))
a = d
count = 0
while d % 10 > 0:
    d = d * 10
    count = count + 1
ans = round(math.pi, count - 1)
print('Число π = ', ans, 'с точностью d = ', a)