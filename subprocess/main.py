import subprocess

proc = subprocess.run([
    'ping',
    '127.0.0.1'
], capture_output=True, text=True)

saida = proc.stdout
saida = saida.replace('Resposta', 'Retorno')
print(saida)
