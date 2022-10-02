x = int(input('Введите х= '))
y = int(input('Введите y= '))
if (x > 0 and y > 0):
    print('x и y находятся в I четверти')
elif (x < 0 and y > 0):
    print('x и y находятся во II четверти')
elif (x < 0 and y < 0):
    print('x и y находятся в III четверти')
else:
    print('x и y находятся в IV четверти')
