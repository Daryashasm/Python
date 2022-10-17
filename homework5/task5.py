def archive(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def unpacking(text):
    num = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            num += text[i]
        else:
            res = res + text[i] * int(num)
            num = ''
    return res

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

welcome = int(input('Будем сжимать (0) или восстанавливать (1) данные? Введи число: '))

x = input('Введите текст: ')
write_file("task5_text.txt", x)

if welcome == 0:
    print('Текст после кодировки: ', archive(x))
    write_file("task5_archive.txt", archive(x))
else:
    print('Текст после дешифровки: ', unpacking(x))
    write_file("task5_unpacking.txt", unpacking(x))