import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()


# with conectar() as conexao:  # contexto para inserção simples
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) ' \
#               'VALUES (%s, %s, %s, %s)'
#         cursor.execute(
#             sql, ('Jack', 'Bauer', 32, 89.6)
#         )
#         conexao.commit()
#
# with conectar() as conexao:  # context para inserção múltipla
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) ' \
#               'VALUES (%s, %s, %s, %s)'
#         dados = [
#             ('Cliente', '1', 28, 56.6),
#             ('Cliente', '2', 15, 42.5)
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# with conectar() as conexao:  # contexto para exclusão múltipla
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.executemany(sql, [(8,), (7,), (6,)])
#         conexao.commit()

with conectar() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome = %s WHERE id = %s'
        cursor.execute(sql, ('Rogério', 4))
        conexao.commit()

with conectar() as conexao:  # contexto para listagem
    with conexao.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM clientes ORDER BY peso ASC LIMIT 100'
        )

        for line in cursor.fetchall():
            print(line)
