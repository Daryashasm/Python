x = input('Введите число, x = ')
sum = 0
for i in x:
    if i != '.':
        sum = sum + int(i)
print('Сумма цифр равна', sum)