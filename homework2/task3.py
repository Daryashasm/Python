array = []
n = int(input('Введите n: ')) 
sum = 0
array = [round((1 + 1 / i)**i, 2) for i in range (1, n + 1)]
print('Последовательность:', array)
for i in range (n):
    sum = sum + array [i]
print('Сумма последовательности равна: ',sum)
