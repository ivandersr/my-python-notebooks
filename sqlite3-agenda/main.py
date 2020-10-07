import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, cod):
        consulta = 'UPDATE OR IGNORE agenda SET nome = ?, telefone = ? WHERE cod = ?'
        self.cursor.execute(consulta, (nome, telefone, cod))
        self.conn.commit()

    def excluir(self, cod):
        consulta = 'DELETE FROM agenda WHERE cod = ?'
        self.cursor.execute(consulta, (cod,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)

        for registro in self.cursor.fetchall():
            print(registro)

    def buscar(self, substring):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{substring}%',))

        for registro in self.cursor.fetchall():
            print(registro)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.buscar('a')
