num_1 = 10
num_2 = 3

divisao = num_1 / num_2

nome = 'Ivander'
sobrenome = 'Salvador'
print(f'{divisao:.2f}')
print(f'{num_1:.2f}')
print(f'{num_1:0^10}')
print(f'{nome:#^20}')
print(f'{num_1:0>10.2f}')

print('{:@>30}'.format(nome))
print('{n:@>30} {n:@<20}'.format(n=nome))
print('{1:!^15}'.format(nome, sobrenome))
print(nome.ljust(20, '#'))
print(nome.rjust(15, '!'))
print(nome.center(20, '@'))
print(nome.lower())
print(nome.upper())
print(nome.title())
