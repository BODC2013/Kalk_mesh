from server.server import Server

# создание экземпляра класса сервер
server = Server()

# вызывает экземпляр из файла server.py возвращает объект фастапи
app = server.get_app()

