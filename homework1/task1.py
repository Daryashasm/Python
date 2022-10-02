number_day = int(input('Введите номер дня недели: '))
if number_day > 7 or number_day < 1:
    print('В неделе только 7 дней')
elif number_day == 6 or number_day == 7:
    print('Это выходной день')
else:
    print('Это будний день ')