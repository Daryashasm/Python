N = int(input("Введите натуральное число N = "))
x = N
i = 2
array = []

while (i <= N):
    if (N % i == 0):
        array.append(i)
        N = N // i
        i = 2
    else:
        i = i + 1
print('Простые множители числа', x, ':', array)