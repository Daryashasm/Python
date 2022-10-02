x = float(input('Введите число, x = '))
sum = 0
while(x > 0):
    y = x % 10
    sum = sum + y
    x = x//10
print('Сумма цифр равна:', sum)  

