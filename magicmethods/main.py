class A:
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(key, value)


a = A()
a.nome = 'Ivander'
print(a.nome)