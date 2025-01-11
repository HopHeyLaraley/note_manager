from datetime import datetime
from data.temp_memory import notes


class Note:
    id = 0
    statuses = {
        # начальные 3 статуса заметки для выбора
        1: 'Выполнено',
        2: 'В процессе',
        3: 'Отложено',
    }

    def __init__(self):
        self.__id = Note.id
        self.username = None
        self.titles = None
        self.content = None
        self.status = None
        self.created_date = datetime.today()
        self.issue_date = None
        Note.id += 1

    def to_dict(self):
        return {
            'id': self.__id,
            'username': self.username,
            'titles': self.titles,
            'content': self.content,
            'status': self.status,
            'created': self.created_date.strftime('%Y-%m-%d %H:%M:%S.%f'),
            'issue': self.issue_date.strftime('%Y-%m-%d %H:%M:%S.%f')
        }

    def create(self, data):
        self.username = data['username']
        self.titles = data['titles']
        self.content = data['content']
        self.status = data['status']
        self.issue_date = data['issue']
        notes[self.__id] = self

    def load(self, data):
        if data['id'] > Note.id:
            Note.id = data['id']
        self.__id = data['id']
        self.username = data['username']
        self.titles = data['titles']
        self.content = data['content']
        self.status = data['status']
        self.created_date = data['created']
        self.issue_date = data['issue']
        notes[self.__id] = self

    def update(self, new_data):
        if new_data['username']:
            self.username = new_data['username']
        if new_data['titles']:
            self.titles = new_data['titles']
        if new_data['content']:
            self.content = new_data['content']
        if new_data['status']:
            self.status = new_data['status']
        if new_data['issue']:
            self.issue_date = new_data['issue']
        notes[self.__id] = self

    def show(self):
        titles = "\n".join("- " + elem for elem in self.titles)
        print()
        print(f'ID заметки: {self.__id}')
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки:\n {titles}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.status}')
        print(f'Дата создания: {self.created_date.strftime("%d-%m")}')
        print(f'Срок выполнения: {self.issue_date.strftime("%d-%m")}')
        print()

    def check_deadline(self):
        issue = self.issue_date.timestamp()
        today = datetime.today().timestamp()
        days_left = abs((self.issue_date.date() - datetime.today().date()).days)
        if today > issue:
            return f'ID: {self.__id} - Дедлайн прошел {days_left} дней назад'
        elif today == issue:
            return f'ID: {self.__id} - Дедлайн подходит к концу сегодня'
        else:
            return f'ID: {self.__id} - До дедлайна еще {days_left} дней'
