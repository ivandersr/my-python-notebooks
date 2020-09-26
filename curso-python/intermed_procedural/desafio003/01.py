# Sistema de perguntas e respostas
perguntas = {
    1: {
        'pergunta': 'Quanto é 1 + 1?',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    2: {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    }
}

respostas_corretas = 0

for key_perg, value_perg in perguntas.items():
    print(f'{key_perg}: {value_perg.get("pergunta")}')
    for key_resp, value_resp in value_perg.get('respostas').items():
        print(f'{key_resp}) {value_resp}')
    resp = input('Escolha a resposta: ')
    if resp == value_perg.get('resposta_certa'):
        print('Resposta correta!')
        respostas_corretas += 1
    else:
        print('Errooou :o')
    print()

nota = respostas_corretas / len(perguntas) * 10
print(f'Você acertou {respostas_corretas} respostas. Nota: {nota:.1f}.')
