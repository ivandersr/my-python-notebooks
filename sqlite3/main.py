import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome VARCHAR,'
    'peso DECIMAL(3,2)'
    ')'
)

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 52))
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {
#         'nome': 'João',
#         'peso': 102
#     }
# )
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {
#         'id': None,
#         'nome': 'Danielle',
#         'peso': 121
#     }
# )

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {
#         'nome': 'Joana',
#         'id': 2
#     }
# )

# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {
#         'id': 2
#     }
# )

# conexao.commit()

cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso < :peso',
    {
        'peso': 100
    }
)

for nome, peso in cursor.fetchall():
    print(nome, peso)

cursor.close()
conexao.close()
