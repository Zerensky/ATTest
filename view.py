from controller import Controller
from model import Note
from datetime import datetime

commands = ['list', "create", "update", "delete", 'read', 'close', 'json', 'none']

class View:
    def __init__(self):
        self.controller = Controller()

    def open_notebook(self):
        print("Список комманд:")
        print(', '.join(commands))
        while True:
            input_command = input("Введите комманду: ")
            input_command = input_command.lower()
            if input_command == 'none':
                print("Ничего не произошло!")
            elif input_command == 'list':
                check = self.use_filter()
                if check == '0':
                    output = self.controller.read_all_notes()
                elif check == "1":
                    print("Неверный формат даты")
                    continue
                else:
                    output = self.controller.sort_notes(check)
                for key, val in output.items():
                    print(f'{key}: Заголовок: {val[0]}; Текст: {val[1]}; Дата изменения: {val[2]}')
            elif input_command == 'create':
                note = self.new_note()
                self.controller.saveNote(note)
                print("Заметка успешно сохранена")
            elif input_command == 'update':
                id = input("Введите номер заметки для обновления: ")
                check_id = self.controller.check_id(id)
                if check_id == '-1':
                    print("Идентификатор не найден")
                else:
                    note = self.new_note()
                    self.controller.update_note(id, note)
                    print('Заметка успешно обновлена')
            elif input_command == 'delete':
                id = input("Введите номер заметки для удаления: ")
                check_id = self.controller.check_id(id)
                if check_id == '-1':
                    print("Идентификатор не найден")
                else:
                    self.controller.delete_note(id)
                    print('Заметка удалена')
            elif input_command == 'read':
                id = input("Введите номер заметки, которую хотите прочитать: ")
                check_id = self.controller.check_id(id)
                if check_id == '-1':
                    print("Идентификатор не найден")
                else:
                    note = self.controller.read_note(id)
                    print(f'{id}: Заголовок: {note[0]}; Текст: {note[1]}; Дата изменения: {note[2]}')
            elif input_command == 'json':
                self.controller.save_json()
                print('Заметки сохранены в формате .json')
            elif input_command == 'close':
                print('Приложение закрыто')
                break
            else:
                print('Ничего не произошло!')
    

    def new_note(self):
        head = input("Введите заголовок: ")
        body = input("Напишите заметку: ")
        note = Note(head=head, body=body)
        return note

    def use_filter(self):
        q = input('Желаете выполнить сортировку по дате? Y/N: ')
        if q == 'y' or q == 'Y':
            try:
                d = input('Введите дату, в период которой вы хотите прочитать заметки (в формате YYYY MM DD): ')
                date = datetime.strptime(d, '%Y %m %d')
                return date
            except ValueError:
                return '1'
        else:
            return '0'


