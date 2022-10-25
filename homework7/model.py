from operator import add, sub, mul, truediv, pow

first = 0
second = 0
result = 0

listOperator = {'*': lambda x,y: int(x) * int(y),
                '/': lambda x,y: int(x) / int(y),
                '+': lambda x,y: int(x) + int(y),
                '-': lambda x,y: int(x) - int(y),
                '^': lambda x,y: int(x)**int(y)}

listOperatorstring = {'+': add,
                      '-': sub,
                      '*': mul,
                      '/': truediv,
                      '^': pow}

def set_string(s):
    if s.isdigit():
        return int(s)
    for i in listOperatorstring.keys():
        left, operator, right = s.partition(i)
        if operator in listOperatorstring:
            return listOperatorstring[operator](set_string(left), set_string(right))

def set_first(number: int):
    global first
    first = number

def set_second(number: int):
    global second
    second = number

def set_result(oper: str):
    global result
    global second
    if (oper == '/') and (second == 0 or first == 0):
        result = None
    else:
        result = listOperator.get(oper)(first, second)

def get_first():
    global first
    return first

def get_second():
    global second
    return second

def get_result():
    global result
    return result