import view, model

def start():
    c = view.input_option()
    if c == 0:
        a = view.InputData('первое')
        model.set_first(a)
        while True:
            oper = view.InputOperator()
            if oper == '=': break
            b = view.InputData('второе')
            model.set_second(b)
            model.set_result(oper)
            result = model.get_result()
            if result == None:
                view.division_by_zero()
                break
            first = model.get_first()
            second = model.get_second()
            view.OutputResult(first, second, oper, result)
            model.set_first(result)
            break
    else:
        string = view.input_string()
        result = model.set_string(string)
        view.ResultStrict(string, result)
