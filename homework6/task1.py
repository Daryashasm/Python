N = int(input('Введите N: '))
composition = lambda x: 1 if x == 0 else x * composition(x - 1)
print('Произведение чисел от 1 до', N,':', composition(N))