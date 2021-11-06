import shutil
import os

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
    print("1 - Создание папки (с указанием имени)")
    print("2 - Удаление папки по имени")
    print("3 - Переход между папками")
    print("4 - Создание пустых файлов с указанием имени")
    print("5 - Запись текста в файл")
    print("6 - Просмотр содержимого файла")
    print("7 - Удаление файлов по имени")
    print("8 - Копирование файлов из одной папки в другую")
    print("9 - Перемещение файлов")
    print("10 - Переименование файлов")

def main():
    flag = 0

    while True:
        if(flag == 0):
            #path = str(input("Укажите путь до рабочей директории: "))
            path = "C:/Users/amirs/Desktop/Financial University/Practice/File_manager/Home"
            file_manager = FileManager(path)
            flag = 1
        print("Рабочая директория:", file_manager.get_address())
        x = str(input("Введите команду (help для вызова инструкции): "))
        if(x == "1"):
            x = str(input("Введите название новой папки: "))
            file_manager.new_dir(x)
            continue
        if(x == "2"):
            x = str(input("Введите название папки для удаления: "))
            file_manager.rm_dir(x)
            continue
        if(x == "3"):
            x = str(input("Введите имя директории, в которую хотите перейти: "))
            file_manager.moving_dir(x)
            continue
        if(x == "4"):
            x = str(input("Введите название нового файла: "))
            file_manager.new_file(x)
            continue
        if(x == "5"):
            x = str(input("Введите название файла, в который хотите записать: "))
            file_manager.redirection(x)
            continue
        if(x == "6"):
            x = str(input("Введите название файла для просмотра: "))
            file_manager.my_cat(x)
            continue
        if(x == "7"):
            x = str(input("Введите название файла для удаления: "))
            file_manager.rm_file(x)
            continue
        if(x == "8"):
            x = str(input("Введите имя файла, который хотите скопировать: "))
            y = str(input("Укажите конечный путь, куда вы хотите скопировать файл: "))
            file_manager.copy_file(x, y)
            continue
        if(x == "9"):
            x = str(input("Введите имя файла, который хотите переместить: "))
            y = str(input("Укажите конечный путь, куда вы хотите переместить файл: "))
            file_manager.move_file(x, y)
            continue
        if(x == "10"):
            x = str(input("Введите имя файла, который хотите переименовать: "))
            y = str(input("Укажите новое имя файла: "))
            file_manager.rename_file(x, y)
            continue
        if(x == "help"):
            get_instructions()
        if(x == "exit"):
            break

if __name__ == "__main__":
    main()