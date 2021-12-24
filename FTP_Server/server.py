import shutil
import socket
import os


HOST = '127.0.0.1'
PORT = 8082
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
print(f'Мы на порту {PORT}')



class Settings(object):
    def __init__(self, path):
        os.chdir(path) # делаем path рабочей директорией


class FileManager(Settings):
    def __init__(self, path):
        super().__init__(path)

    def new_dir(self, name):
        try:
            os.mkdir(name)
            print(f"Папка {name} создана")
        except OSError:
            print("Директория уже существует!")

    def rm_dir(self, name):
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена")
        except OSError:
            print("Директории не существует!")

    def moving_dir(self, name):
        try:
            os.chdir(name)
        except OSError:
            print("Директории не существует!")

    def new_file(self, name):
        files = os.listdir(os.getcwd())
        if (name in files):
            print("Файл существует!")
            return 0
        with open(name, "w", encoding='utf-8') as file:
            pass

    def redirection(self, name):
        files = os.listdir(os.getcwd())
        if (name not in files):
            print("Файла не существует!")
            return 0
        with open(name, "a", encoding='utf-8') as file:
            text = str(input("Введите текст, который хотите добавить в файл: "))
            file.write(text)


    def my_cat(self, name):
        files = os.listdir(os.getcwd())
        if (name not in files):
            print("Файла не существует!")
            return 0
        with open(name, "r", encoding='utf-8') as file:
            text = file.read()
            print(text)

    def rm_file(self, name):
        try:
            os.remove(name)
            print("Файл", name, "удален!")
        except FileNotFoundError:
            print("Файл не найден!")

    def copy_file(self, file_name, finish_path):
        try:
            shutil.copy(file_name, finish_path)
            print(f"Файл {file_name} скопирован в {finish_path}!")
        except FileNotFoundError:
            print("Файл не найден!")

    def move_file(self, file_name, finish_path):
        try:
            shutil.move(file_name, finish_path)
            print(f"Файл {file_name} перемещен в {finish_path}")
        except (FileNotFoundError, shutil.Error):
            print("Файл не найден!")

    def rename_file(self, file_name, finish_name):
        try:
            os.rename(file_name, finish_name)
            print(f"Файл {file_name} переименован в {finish_name}")
        except FileNotFoundError:
            print("Файл не найден!")

    def get_address(self):
        return os.getcwd()

    def error (self, working_file, finish_name):
        if (working_file not in finish_name):
            print("Вы вышли за пределы рабочей директории")
            return 0
        else:
            return 1



def get_instructions():
    conn.send("1 - Создание папки (с указанием имени)\n2 - Удаление папки по имени\n3 - Переход между папками\n4 - Создание пустых файлов с указанием имени\n5 - Запись текста в файл\n6 - Просмотр содержимого файла\n7 - Удаление файлов по имени\n8 - Копирование файлов из одной папки в другую\n9 - Перемещение файлов\n10 - Переименование файлов".encode())

path = conn.recv(2054).decode()
file_manager = FileManager(path)
def main(a):
    x = a
    print(x)

    if(x == "1"):
        conn.send("Введите название новой папки: ".encode())
        x = conn.recv(2054).decode()
        file_manager.new_dir(x)

    if(x == "2"):
        conn.send("Введите название папки для удаления: ".encode())
        x = conn.recv(2054).decode()
        file_manager.rm_dir(x)

    if(x == "3"):
        conn.send("Введите имя директории, в которую хотите перейти: ".encode())
        x = conn.recv(2054).decode()
        file_manager.moving_dir(x)

    if(x == "4"):
        conn.send("Введите название нового файла: ".encode())
        x = conn.recv(2054).decode()
        file_manager.new_file(x)

    if(x == "5"):
        conn.send("Введите название файла, в который хотите записать: ".encode())
        x = conn.recv(2054).decode()
        file_manager.redirection(x)

    if(x == "6"):
        conn.send("Введите название файла для просмотра: ".encode())
        x = conn.recv(2054).decode()
        file_manager.my_cat(x)

    if(x == "7"):
        conn.send("Введите название файла для удаления: ".encode())
        x = conn.recv(2054).decode()
        file_manager.rm_file(x)

    if(x == "8"):
        conn.send("Введите имя файла, который хотите скопировать и Укажите конечный путь, куда вы хотите скопировать файл: ".encode())
        x = conn.recv(2054).decode()
        x = x.split(' ')
        file_manager.copy_file(x[0], x[1])

    if(x == "9"):
        conn.send("Введите имя файла, который хотите переместить и Укажите конечный путь, куда вы хотите переместить файл: ".encode())
        x = conn.recv(2054).decode()
        x = x.split(' ')
        file_manager.move_file(x[0], x[1])

    if(x == "10"):
        conn.send("Введите имя файла, который хотите переименовать и Укажите новое имя файла: ".encode())
        x = conn.recv(2054).decode()
        x = x.split(' ')
        file_manager.rename_file(x[0], x[1])

    if(x == "help"):
        get_instructions()

t = True
while t:
    x = conn.recv(2054).decode()
    if (x == "exit"):
        t = False
    else:
        main(x)
conn.close()