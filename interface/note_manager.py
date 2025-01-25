import json
from models import Note
from db import insert_note, select_note, update_note, delete_note, select_notes_by_keyword
from utils import validate_date, to_int, find_id


class InputNoteData:
    def input_titles(self):
        i = 0
        titles = []
        while True:
            elem = input(f'Введите заголовок заметки {i + 1} или пустую строку для пропуска: ')
            if elem == '':
                break
            else:
                titles.append(elem)
                i += 1
        return list(set(titles))

    def input_status(self, new_status_option=True):
        while True:
            print('Выберите статус:')
            # вывод списка статусов и чтение выбора
            for i, sts in Note.statuses.items():
                print(f'{i}.{sts}')
            if new_status_option:
                print('0.Добавить новый статус')
            status = to_int(input())
            if status in Note.statuses.keys():
                # выбран существующий статус - в заметке укажем этот статус
                return Note.statuses[status]
            elif status == 0 and new_status_option:
                self.add_new_status()
            else:
                print('Выберите статус из предложенных')

    def add_new_status(self):
        status = input('Введите новый статус: ')
        last_key = list(Note.statuses.keys())[-1]
        Note.statuses[last_key + 1] = status
        # save_statuses()

    def input_date(self):
        while True:
            created_date = input(f'Введите срок выполнения (день-месяц-год): ')
            valid_date = validate_date(created_date)
            if valid_date:
                return valid_date
            else:
                continue


class CreateNote(InputNoteData):
    # добавление заметок
    def main(self):
        fields = self.input_note_data()
        note = Note(fields)
        insert_note(note)

    # метод ввода полей новой заметки
    def input_note_data(self):
        name = input('Введите имя: ')
        titles = self.input_titles()
        content = input('Введите содержимое заметки: ')
        status = self.input_status()
        issue = self.input_date()
        return {
            'username': name,
            'titles': titles,
            'content': content,
            'status': status,
            'issue_date': issue,
        }


class ReadNote:
    # показать заметки: 1-все, 2-по id
    def main(self):
        self.read_all()
        return

    def show_note(self, id, data):
        note = Note(data, id)
        note.show()

    def read_all(self):
        notes = select_note()
        if not notes:
            print('Пока еще нет заметок')
            return
        for i, fields in notes.items():
            self.show_note(id=i, data=fields)

    def read_one(self, note_id):
        note = select_note(note_id)[note_id]
        self.show_note(id=note_id, data=note)


class UpdateNote(InputNoteData):
    # обновление заметки
    def main(self):
        note_id = find_id()
        if not note_id and note_id != 0:
            return
        new_data = {
            'username': None,
            'titles': None,
            'content': None,
            'status': None,
            'issue_date': None
        }
        field = None
        value = None
        while True:
            print('Текущие значения заметки:')
            ReadNote().read_one(note_id)
            print('Какое поле вы хотите изменить?:')
            print('1.Имя пользователя')
            print('2.Заголовки заметки')
            print('3.Содержимое заметки')
            print('4.Статус')
            print('5.Срок выполнения')
            print('0.Назад')
            print()
            choice = input()
            choice = to_int(choice)
            if choice == 1:
                field = 'username'
                new_data[field] = input('Введите имя: ')
                value = new_data[field]
                break
            elif choice == 2:
                field = 'titles'
                new_data[field] = self.input_titles()
                value = new_data[field]
                break
            elif choice == 3:
                field = 'content'
                new_data[field] = input('Введите содержимое заметки: ')
                value = new_data[field]
                break
            elif choice == 4:
                field = 'status'
                new_data[field] = self.input_status()
                value = new_data[field]
                break
            elif choice == 5:
                field = 'issue_date'
                new_data[field] = self.input_date()
                value = new_data[field]
                break
            elif choice == 0:
                return
            else:
                print('Выберите поле из предложенных')
                continue
        update_note(note_id, field, value)
        print('Данные успешно изменены')


class SearchNote(InputNoteData):
    # поиск заметки
    def main(self):
        notes = select_note()
        if not notes:
            print('Пока еще нет заметок')
            return
        result = self.search_menu()

        # print(result)
        while True:
            if len(result.keys()) == 0:
                print(f'Не найдено заметок по ключевому слову')
                break
            else:
                print(f'Найдено {len(result.keys())} заметок. Вывести их? (y/n или д/н)')
                a = input()  # временная переменная для хранения ответа пользователя
                if a.lower() == 'y' or a.lower() == 'д':
                    for i, fields in result.items():
                        note = Note(values=fields, key=i)
                        note.show()
                    break
                elif a.lower() == 'n' or a.lower() == 'н':
                    break
                else:
                    print('Я вас не понимаю')
                    continue
        return

    def search_by_status(self, search_status):
        result = {}
        notes = select_note()
        for i, note in notes.items():
            if note['status'] == search_status:
                result[i] = note
        return result

    def search_by_keyword(self, user_keyword):
        result = {}
        notes = select_note()
        for i, note in notes.items():
            if user_keyword in note['username'] or \
                    user_keyword in json.dumps(note['titles']) or \
                    user_keyword in note['content']:
                result[i] = note
        return result

    def search_menu(self):
        while True:
            print('По какому критерию искать заметки?')
            print('1.По статусу')
            print('2.По ключевому слову')
            print('0.Назад')
            choice = to_int(input())
            if choice == 1:
                search_status = self.input_status(new_status_option=False)
                result = select_notes_by_keyword(field='status', keyword=search_status)
                # result = self.search_by_status(search_status)
                break
            elif choice == 2:
                user_keyword = input('Введите ключевое слово\n')
                result = select_notes_by_keyword(field='titleandcontent', keyword=user_keyword)
                # result = self.search_by_keyword(user_keyword)
                break
            elif choice == 0:
                return
            else:
                print('Выберите критерий из предложенных')
        return result


class DeleteNote:
    def main(self):
        founded = SearchNote().search_menu()
        if len(founded.keys()) <= 0:
            print(f'Не найдено заметок по ключевому слову')
            return
        else:
            while True:
                print(f'Найдено {len(founded.keys())} заметок. Удалить их? (y/n или д/н)')
                a = input()  # временная переменная для хранения ответа пользователя
                if a.lower() == 'y' or a.lower() == 'д':
                    for note_id in founded.keys():
                        delete_note(note_id)
                    # temp = {}
                    # notes = select_note()
                    # for i, note in notes.items():
                    #     if i in founded.keys():
                    #         temp[i] = note
                    # delete_from_dict(temp)
                    break
                elif a.lower() == 'n' or a.lower() == 'н':
                    break
                else:
                    print('Я вас не понимаю')
                    continue
        return


class NoteUtils:
    def check_deadlines(self):
        notes = select_note()
        for i, note in notes.items():
            deadline = note.check_deadline()
            print(deadline)
