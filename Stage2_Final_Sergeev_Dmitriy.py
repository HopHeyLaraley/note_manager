import datetime
from datetime import datetime

class Note:
    id = 0
    dates_types = {
        'created': "дату создания",
        'issue': "срок выполнения",
    }
    statuses = {
        # начальные 3 статуса заметки для выбора
        1: 'Выполнено',
        2: 'В процессе',
        3: 'Отложено',
    }

    def __init__(self):
        self.__id = Note.id
        self.username = input('Введите имя: ')
        self.titles = self.__input_titles()
        self.content = input('Введите содержимое заметки: ')
        self.__status = self.__input_status()
        self.created_date = self.__correct_date('created')
        self.issue_date = self.__correct_date('issue')
        Note.id += 1

    # метод цикличного ввода заголовков
    # задание add_titles_loop
    def __input_titles(self):
        i = 0
        titles = []
        while True:
            elem = input(f'Введите заголовок заметки {i + 1} или пустую строку для пропуска: ')
            if elem == '':
                break
            else:
                titles.append(elem)
                i += 1
        return set(titles)

    # метод выбора статуса из предложенных или добавления новых статусов
    # задание update_status
    def __input_status(self):
        while True:
            try:
                print('Выберите статус:')
                # вывод списка статусов и чтение выбора
                for i in Note.statuses.keys():
                    print(f'{i}.{Note.statuses.get(i)}')
                print('0.Добавить новый статус')
                status = int(input())
                if status in Note.statuses.keys():
                    # выбран существующий статус - в заметке укажем этот статус
                    return Note.statuses.get(status)
                elif status == 0:
                    # добавление нового статуса
                    status = input('Введите новый статус: ')
                    self.__add_new_status(status)
                else:
                    print('Выберите статус из предложенных')
            except ValueError:
                print('Выберите статус из предложенных')

    # метод добавления нового статуса к существующим
    # задание update_status
    def __add_new_status(self, status):
        last_key = list(Note.statuses.keys())[-1]
        Note.statuses[last_key+1] = status

    # метод для изменения статуса заметки
    # задание update_status
    def change_status_menu(self):
        print()
        while True:
            print(f'Текущий статус: {self.__status}')
            choice = input('Поменять статус (y/n)?: ')
            if choice.lower() == 'y':
                new_status = self.__input_status()
                self.__status = new_status
                print('Статус изменен!')
                return
            elif choice.lower() == 'n':
                return
            else:
                print('Введите корректные данные')

    def show_note(self):
        print()
        print(f'ID заметки: {self.__id}')
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки: ')
        print(f'{"\n".join("- "+elem for elem in self.titles)}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.__status}')
        print(f'Дата создания: {self.__format_date(self.created_date)}')
        print(f'Срок выполнения: {self.__format_date(self.issue_date)}')
        print()

    # дальше методы для дат
    # метод ввода даты создания и срока выполнения с проверкой на правильность ввода
    def __correct_date(self, date_of):
        date_of = Note.dates_types.get(date_of)
        while True:
            created_date = input(f'Введите {date_of} (день-месяц-год): ')
            try:
                return datetime.strptime(created_date, '%d-%m-%Y')
            except ValueError:
                print("Введите корректную дату")

    def __format_date(self, date):
        return date.strftime("%d-%m")

    # метод для проверки истечения срока дедлайна
    # задание check_deadline
    def check_deadline(self):
        issue = self.issue_date.timestamp()
        today = datetime.today().timestamp()
        if today > issue:
            days_left = -(self.issue_date.date() - datetime.today().date()).days
            return f'Дедлайн прошел {days_left} {self.__days_in_rus(days_left)} назад'
        elif today == issue:
            return 'Дедлайн подходит к концу сегодня'
        else:
            days_left = (self.issue_date.date() - datetime.today().date()).days
            return f'До дедлайна еще {days_left} {self.__days_in_rus(days_left)}'

    # вспомогательный метод для склонения слова "день" для N дней
    # задание check_deadline
    def __days_in_rus(self, n):
        if 11 <= n%100 <= 19:
            return 'дней'
        elif n%10 == 1:
            return 'день'
        elif 2 <= n%10 <= 4:
            return 'дня'
        else:
            return 'дней'

    # геттер для ID заметки
    def get_id(self):
        return self.__id


# №1 меню - функция добавления заметки
def add_note():
    note = Note()
    id = note.get_id()
    notes[id] = note
    print('Заметка добавлена')

# №2 меню - функция вывода всех заметкок
def show_all():
    for id in notes.keys():
        notes.get(id).show_note()

# функция для ввода корректного ID
def get_id():
    while True:
        usr_input = input("Введите ID (или 'X' для возврата): ")
        if usr_input in ('x','х'):
            return None
        try:
            id = int(usr_input)
            if id in notes.keys():
                return id
            else:
                print("ID не существует\n")
        except ValueError:
            print("ID должно быть числом\n")
            continue

# №3 меню - функция вывода заметки по ID
def show_id():
    id = get_id()
    if id is None:
        return
    notes.get(id).show_note()

# №4 меню - функция изменения статуса заметки по ID
def change_by_id():
    id = get_id()
    if id is None:
        return
    notes.get(id).change_status_menu()

# дальше идут 3 функции для удаления заметок по 3 критериям
# 1 - функция для удаления по id
# задание delete_note
def del_by_id():
    id = get_id()
    if id is None:
        return
    notes.pop(id)
    print('Заметка удалена!')

# 2 - функция для удаления по имени пользователя
# задание delete_note
def del_by_username():
    name = input('Введите имя пользователя: ')
    del_count = 0
    del_indexes = []
    for i, val in notes.items():
        if val.username == name:
            del_indexes.append(i)
            del_count += 1
    for i in del_indexes:
        notes.pop(i)
    if del_count < 1:
        print('У этого пользователя не было заметок')
    else:
        print(f'Удалено заметок: {del_count}')

# 3 - функция для удаления по заголовкам
# задание delete_note
def del_by_title():
    ttl = input('Введите заголовок: ')
    del_count = 0
    del_indexes = []
    for i, val in notes.items():
        if val.username == ttl:
            del_indexes.append(i)
            del_count += 1
    for i in del_indexes:
        notes.pop(i)
    if del_count < 1:
        print('У этого пользователя не было заметок')
    else:
        print(f'Удалено заметок: {del_count}')

# №5 меню - функция удаления заметки по ID
# задание delete_note
def delete_note():
    while True:
        print('По какому критерию удалить заметки?:\n1.По ID\n2.По имени пользователя\n3.По заголовку\n0.Вернуться')
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print('Выберите из предложенных вариантов')
        if choice == 0:
            return
        elif choice == 1:
            del_by_id()
        elif choice == 2:
            del_by_username()
        elif choice == 3:
            del_by_title()
        else:
            print('Выберите из предложенных вариантов')

# №6 меню - функция вывода дедлайна заметки по ID
def check_deadline():
    id = get_id()
    if id is None:
        return
    print(notes.get(id).check_deadline())

# словарь с текстом для меню
action_names = {
    1: "Добавить заметку",
    2: "Показать все заметки",
    3: "Показать заметку по ID",
    4: "Изменить статус заметки по ID",
    5: "Удалить заметку",
    6: "Проверить дедлайны"
}

# словарь для связи пунктов меню с функциями
# задание multiple_notes (все функции)
actions = {
    1: add_note,
    2: show_all,
    3: show_id,
    4: change_by_id,
    5: delete_note,
    6: check_deadline
}

# словарь для хранения всех записей
# ключ - ID заметки, значение - сама заметка
# задание multiple_notes
notes = {}

# функция с меню для удобного управления пользователя
# задание multiple_notes
def main_menu():
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
        print('\n'+'-'*10)
        print('Выберите действие: ')
        for i, action_name in action_names.items():
            print(f'{i}: {action_name}')
        action = input()
        try:
            action = int(action)
        except ValueError:
            print("Выберите действие из предложенных\n")
            continue
        if action in actions:
            actions[action]()

main_menu()