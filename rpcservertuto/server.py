from xmlrpc.server import SimpleXMLRPCServer
import os
from xmlrpc.server import SimpleXMLRPCRequestHandler

server = SimpleXMLRPCServer(('localhost', 3333), logRequests=True)


class RequestClass:
    @staticmethod
    def list_directory(directory):
        return os.listdir(directory)

    @staticmethod
    def list_text():
        return server.get_request()

    @staticmethod
    def hello_world():
        return 'Hello World!'


server.register_instance(RequestClass)

if __name__ == '__main__':
    try:
        print('Servidor rodando!')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Finalizando servidor...')
