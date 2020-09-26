def funcao1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao2(arg):
    return arg


def funcao3(arg1, arg2):
    return arg1 + arg2


exec_func2 = funcao1(funcao2, 1)
exec_func3 = funcao1(funcao3, 3, 4)

print(exec_func2)
print(exec_func3)
