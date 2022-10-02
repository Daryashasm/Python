N = int(input('Введите N: '))
array = []
x = 1
for i in range(N):
    array.append(x * (i + 1))
    x = array[i]
print('Произведение чисел от 1 до', N,':', array)