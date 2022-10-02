import math
x1 = int(input('Введите х1= '))
y1 = int(input('Введите y1= '))
x2 = int(input('Введите х2= '))
y2 = int(input('Введите y2= '))
x = (x1 - x2)**2
y = (y1 - y2)**2
d = math.sqrt(x + y)
print(round(d, 2))
