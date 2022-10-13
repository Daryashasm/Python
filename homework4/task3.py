array = list(map(int, input("Введите последовательность цифр через пробел: ").split()))
newArray = [i for i in array if array.count(i)==1]
print(newArray)



