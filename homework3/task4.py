number = int(input('Введите десятичное число: '))
row = ''
while number > 0:
    row = str(number % 2) + row
    number = number // 2
print('Число в двочином виде:', row)