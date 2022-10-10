k = int(input('Введите число: '))
fibo = []
a, b = 1, 1
for i in range (k):
    fibo.append(a)
    a, b = b, a + b
a, b = 0, 1
for i in range (k + 1):
    fibo.insert(0, a)
    a, b = b, a - b
print(fibo)