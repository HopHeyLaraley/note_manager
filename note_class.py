from datetime import datetime
from utils import *

# словарь для хранения всех записей
# ключ - ID заметки, значение - сама заметка
# задание multiple_notes
notes = {}


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
        self.titles = input_titles()
        self.content = input('Введите содержимое заметки: ')
        self.__status = self.__input_status()
        self.created_date = self.__correct_date('created')
        self.issue_date = self.__correct_date('issue')
        Note.id += 1

    # метод выбора статуса из предложенных или добавления новых статусов
    # задание update_status
    def __input_status(self):
        while True:
            self.__input_status_menu()
            status = self.__get_input_status()

            if status in Note.statuses.keys():
                # выбран существующий статус - в заметке укажем этот статус
                return Note.statuses[status]
            elif status == 0:
                self.__set_new_status()
            else:
                print('Выберите статус из предложенных')

    def __input_status_menu(self):
        print('Выберите статус:')
        # вывод списка статусов и чтение выбора
        for i in Note.statuses.keys():
            print(f'{i}.{Note.statuses.get(i)}')
        print('0.Добавить новый статус')

    def __get_input_status(self):
        try:
            return int(input())
        except ValueError:
            print('Выберите статус из предложенных')
            return -1

    # метод добавления нового статуса к существующим
    # задание update_status
    def __set_new_status(self):
        # добавление нового статуса
        status = input('Введите новый статус: ')
        last_key = list(Note.statuses.keys())[-1]
        Note.statuses[last_key + 1] = status

    # метод для изменения статуса заметки
    # задание update_status
    def change_status_menu(self):
        print()
        while True:
            print(f'Текущий статус: {self.__status}')
            choice = input('Поменять статус (y/n)?: ')
            if choice.lower() == 'y':
                self.__status = self.__input_status()
                print('Статус изменен!')
                return
            elif choice.lower() == 'n':
                return
            else:
                print('Введите корректные данные')

    def show_note(self):
        titles = "\n".join("- " + elem for elem in self.titles)
        print()
        print(f'ID заметки: {self.__id}')
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки:\n {titles}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.__status}')
        print(f'Дата создания: {format_date(self.created_date)}')
        print(f'Срок выполнения: {format_date(self.issue_date)}')
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
                continue

    # метод для проверки истечения срока дедлайна
    # задание check_deadline
    def check_deadline(self):
        issue = self.issue_date.timestamp()
        today = datetime.today().timestamp()
        days_left = abs((self.issue_date.date() - datetime.today().date()).days)
        if today > issue:
            return f'Дедлайн прошел {days_left} {days_in_rus(days_left)} назад'
        elif today == issue:
            return 'Дедлайн подходит к концу сегодня'
        else:
            return f'До дедлайна еще {days_left} {days_in_rus(days_left)}'

    # геттер для ID заметки
    def get_id(self):
        return self.__id
