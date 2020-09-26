def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        return f'{tamanho:.0f}B'
    elif tamanho < mega:
        return f'{tamanho/kilo:.0f}K'
    elif tamanho < giga:
        return f'{tamanho/mega:.0f}M'
    elif tamanho < tera:
        return f'{tamanho/giga:.0f}G'
    elif tamanho < peta:
        return f'{tamanho/tera:.0f}T'
    else:
        return f'{tamanho/peta:.0f}P'