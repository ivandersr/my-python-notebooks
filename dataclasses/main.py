from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=False, repr=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Ivander', 'Salvador')
p2 = Pessoa('Ivander', 'Salvador')

print(p1)
print(p1 == p2)

print(asdict(p1))
print(astuple(p2))
