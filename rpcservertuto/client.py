from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3333')

if __name__ == '__main__':
    print(proxy.list_directory(r'/home/ivander'))
    print(proxy.hello_world())
    print(proxy.list_text())
