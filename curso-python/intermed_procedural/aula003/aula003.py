# var = 'valor'
#
#
# def func1():
#     print(var)
#
#
# def func2():
#     var = 'outro valor'
#     print(var)
#
#
# func1()
# func2()
# print(var)

def func1():
    var = 'valor no escopo local'
    return var


valor = func1()


def func2(arg):
    print(arg)


func2(valor)
