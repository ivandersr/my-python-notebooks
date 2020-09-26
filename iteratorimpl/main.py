class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        if not index < len(self.__items):
            raise IndexError('Invalid index')
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.__items[self.__index]
            self.__index += 1
            return current
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()


lista = MinhaLista()
lista.add(1)
lista.add(2)
lista[2] = 5
lista[0] = 3

del lista[1]

for valor in lista:
    print(valor)
