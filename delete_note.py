import datetime
from datetime import datetime

class Note:
    id = 0

    dates_types = {
        'created': "дату создания",
        'issue': "срок выполнения",
    }

    statuses = {
        1: 'Выполнено',
        2: 'В процессе',
        3: 'Отложено',
    }

    def __init__(self):
        self.__id = Note.id
        self.username = input('Введите имя: ')
        self.titles = self.__input_titles()
        self.content = input('Введите содержимое заметки: ')
        self.status = self.__input_status()
        self.created_date = self.__correct_date('created')
        self.issue_date = self.__correct_date('issue')
        Note.id += 1

    def get_id(self):
        return self.__id

    def __add_new_status(self, status):
        last_key = list(Note.statuses.keys())[-1]
        Note.statuses[last_key+1] = status

    def __input_status(self):
        while True:
            try:
                print('Выберите статус')
                for i in Note.statuses.keys():
                    print(f'{i}.{Note.statuses.get(i)}')
                print('0.Добавить новый статус')
                status = int(input())
                if status in Note.statuses.keys():
                    return Note.statuses.get(status)
                elif status == 0:
                    status = input('Введите новый статус: ')
                    self.__add_new_status(status)
                else:
                    print('Выберите статус из предложенных')
            except ValueError:
                print('Выберите статус из предложенных')

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

    def __correct_date(self, date_of):
        date_of = Note.dates_types.get(date_of)
        while True:
            created_date = input(f'Введите {date_of} (день-месяц-год): ')
            try:
                return datetime.strptime(created_date, '%d-%m-%Y')
            except ValueError:
                print("Введите корректную дату")

    def __format_date(self, date):
        return date.strftime("%d-%m-%Y")

    def show_note(self):
        print()
        print(f'ID заметки: {self.__id}')
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки: ')
        print(f'{"\n".join("- "+elem for elem in self.titles)}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.status}')
        print(f'Дата создания: {self.__format_date(self.created_date)}')
        print(f'Срок выполнения: {self.__format_date(self.issue_date)}')
        print()

    def __change_status(self, new_status):
        self.status = new_status

    def change_status_menu(self):
        print()
        while True:
            print(f'Текущий статус: {self.status}')
            choice = input('Поменять статус (y/n)?: ')
            if choice.lower() == 'y':
                new_status = self.__input_status()
                self.__change_status(new_status)
                return
            elif choice.lower() == 'n':
                return
            else:
                print('Введите корректные данные')

    def __days_in_rus(self, n):
        if 11 <= n%100 <= 19:
            return 'дней'
        elif n%10 == 1:
            return 'день'
        elif 2 <= n%10 <= 4:
            return 'дня'
        else:
            return 'дней'

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


action_names = {
    1: "Добавить заметку",
    2: "Показать все заметки",
    3: "show id",
    4: "change id",
    5: "delete id"
}

notes = {}

def add_note():
    note = Note()
    id = note.get_id()
    notes[id] = note

def show_all():
    for id in notes.keys():
        notes.get(id).show_note()

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

def show_id():
    id = get_id()
    if id is None:
        return
    notes.get(id).show_note()

def change_by_id():
    id = get_id()
    if id is None:
        return
    notes.get(id).change_status_menu()

def delete_by_id():
    id = get_id()
    if id is None:
        return
    notes.pop(id)

actions = {
    1: add_note,
    2: show_all,
    3: show_id,
    4: change_by_id,
    5: delete_by_id
}

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