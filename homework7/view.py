def input_option():
    optionCalc = int(input('Вариант калькулятора: обычный(0) или инженерный(1)\nВведите: '))
    return optionCalc

def input_string():
    calc = input('Введите данные для вычисления: ')
    return calc

def InputData(string: str):
    number = int(input(f'Введите {string} число: '))
    return number

def OutputResult(a, b, oper, number):
    print(f'Результат операции: {a} {oper} {b} = {number}')

def InputOperator():
    oper = input(f'Введите оператор: ')
    return oper

def division_by_zero():
    print('Деление на 0!')

def ResultStrict(calc, result):
    print('Результат операции:', calc, '=', result)
