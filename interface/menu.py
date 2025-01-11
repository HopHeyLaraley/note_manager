from note_class import Note
from data.file_memory import load_statuses, load_notes, save_statuses, save_notes, delete_from_dict
from datetime import datetime
from utils.utils import *


class Menu:
    # тексты пунктов меню
    action_names = {
        1: "Добавить заметку",
        2: "Показать заметки",
        3: "Изменить заметку",
        4: "Удалить заметку",
        5: "Найти заметку",
        6: "Проверить дедлайны",
        0: "Выйти"
    }

    # словарь для хранения ссылок на функции для пунктов меню
    menu_actions = {}

    def __init__(self):
        load_notes()
        load_statuses()
        Menu.menu_actions = {
            1: self.add_note,  # Grade 1. Этап 3: Задание 1 - метод создания заметки
            2: self.show_note,  # Grade 1. Этап 3: Задание 3 - метод отображения заметок
            3: self.update_note,  # Grade 1. Этап 3: Задание 2 - метод обновления заметки
            4: self.delete_note,
            5: self.search_note,  # Grade 1. Этап 3: Задание 4 - метод поиска заметок
            6: self.check_deadlines,
        }
        self.main_menu()

    def main_menu_text(self):
        print('*' * 10)
        print('Выберите действие: ')
        for i, action_name in Menu.action_names.items():
            print(f'{i}.{action_name}')

    # Grade 1. Этап 3: Задание 5 - меню действий
    def main_menu(self):
        print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
        while True:
            self.main_menu_text()
            action = input()
            action = to_int(action)
            if action in self.menu_actions:
                self.menu_actions[action]()
                # после каждой опции сохраняем изменения в файл
                # не для всех опций это нужно, но не хотел дублировать
                # вызов в каждом методе опций меню
                save_notes()
            elif action == 0:
                return
            else:
                print("Выберите действие из предложенных\n")
                continue

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
            'issue': issue,
        }

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
            status = input()
            status = to_int(status)
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
        save_statuses()

    def input_date(self):
        while True:
            created_date = input(f'Введите срок выполнения (день-месяц-год): ')
            try:
                return datetime.strptime(created_date, '%d-%m-%Y')
            except ValueError:
                print("Введите корректную дату")
                continue

    # Grade 1. Этап 3: Задание 1 - добавление заметок
    def add_note(self):
        note = Note()
        data = self.input_note_data()
        note.create(data)

    def show_all(self):
        if not notes_exist():
            return
        for i in notes.keys():
            notes[i].show()

    def show_one(self, note_id):
        notes[note_id].show()

    # Grade 1. Этап 3: Задание 3 - показать заметки: 1-все, 2-по id
    def show_note(self):
        while True:
            print('Уточните действие:\n1.Показать все заметки\n2.Показать одну заметку\n0.Назад')
            choice = input()
            choice = to_int(choice)
            if choice == 1:
                self.show_all()
                break
            elif choice == 2:
                note_id = find_id()
                if note_id or note_id == 0:
                    self.show_one(note_id)
                break
            elif choice == 0:
                break
            else:
                print('Выберите действие из предложенных')
                continue
        return

    def search_by_status(self, search_status):
        result = {}
        for i, note in notes.items():
            if note.status == search_status:
                result[i] = note
        return result

    def search_by_keyword(self, user_keyword):
        result = {}

        for i, note in notes.items():
            if user_keyword in note.username or \
                    user_keyword in note.titles or \
                    user_keyword in note.content:
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
                result = self.search_by_status(search_status)
                break
            elif choice == 2:
                user_keyword = input('Введите ключевое слово\n')
                result = self.search_by_keyword(user_keyword)
                break
            elif choice == 0:
                return
            else:
                print('Выберите критерий из предложенных')
        return result

    # Grade 1. Этап 3: Задание 4 - поиск заметки
    def search_note(self):
        if not notes_exist():
            return
        result = self.search_menu()
        while True:
            if len(result.keys()) < 0:
                print(f'Не найдено заметок по ключевому слову')
            else:
                print(f'Найдено {len(result.keys())} заметок. Вывести их? (y/n или д/н)')
                a = input()  # временная переменная для хранения ответа пользователя
                if a.lower() == 'y' or a.lower() == 'д':
                    for i, note in result.items():
                        note.show()
                    break
                elif a.lower() == 'n' or a.lower() == 'н':
                    break
                else:
                    print('Я вас не понимаю')
                    continue
        return

    # Grade 1. Этап 3: Задание 2 - обновление заметки
    def update_note(self):
        note_id = find_id()
        if not note_id and note_id != 0:
            return
        new_data = {
            'username': None,
            'titles': None,
            'content': None,
            'status': None,
            'issue': None
        }
        while True:
            print('Текущие значения заметки:')
            self.show_one(note_id)
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
                new_data['username'] = input('Введите имя: ')
                break
            elif choice == 2:
                new_data['titles'] = self.input_titles()
                break
            elif choice == 3:
                new_data['content'] = input('Введите содержимое заметки: ')
                break
            elif choice == 4:
                new_data['status'] = self.input_status()
                break
            elif choice == 5:
                new_data['issue'] = self.input_date()
                break
            elif choice == 0:
                return
            else:
                print('Выберите поле из предложенных')
                continue
        notes[note_id].update(new_data)

    def delete_note(self):
        founded = self.search_menu()
        if len(founded.keys()) <= 0:
            print(f'Не найдено заметок по ключевому слову')
            return
        else:
            while True:
                print(f'Найдено {len(founded.keys())} заметок. Удалить их? (y/n или д/н)')
                a = input()  # временная переменная для хранения ответа пользователя
                if a.lower() == 'y' or a.lower() == 'д':
                    temp = {}
                    for i, note in notes.items():
                        if i in founded.keys():
                            temp[i] = note
                    delete_from_dict(temp)
                    break
                elif a.lower() == 'n' or a.lower() == 'н':
                    break
                else:
                    print('Я вас не понимаю')
                    continue
        return

    def check_deadlines(self):
        for i, note in notes.items():
            deadline = note.check_deadline()
            print(deadline)