from datetime import datetime
from utils import unique_id, date_format


# вообще сам класс после создания БД как будто не нужен
class Note:
    statuses = {
        # начальные 3 статуса заметки для выбора
        1: 'Выполнено',
        2: 'В процессе',
        3: 'Отложено',
    }

    def __init__(self, values, key=None):
        if key is not None:
            self.__id = key
        else:
            self.__id = unique_id()  # после добавления БД стал бесполезным, надо как то использовать
        self.username = values['username']
        self.titles = values['titles']
        self.content = values['content']
        self.status = values['status']
        self.issue_date = values['issue_date']
        try:
            self.created_date = values['created_date']
        except KeyError:
            self.created_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    # def to_dict(self):
    #     return {
    #         'id': self.__id,
    #         'username': self.username,
    #         'titles': self.titles,
    #         'content': self.content,
    #         'status': self.status,
    #         'created_date': self.created_date.strftime('%Y-%m-%d %H:%M:%S.%f'),
    #         'issue_date': self.issue_date.strftime('%Y-%m-%d %H:%M:%S.%f')
    #     }

    def update(self, new_data):
        if new_data['username']:
            self.username = new_data['username']
        if new_data['titles']:
            self.titles = new_data['titles']
        if new_data['content']:
            self.content = new_data['content']
        if new_data['status']:
            self.status = new_data['status']
        if new_data['issue_date']:
            self.issue_date = new_data['issue_date']

    def show(self):
        titles = "\n".join("- " + elem for elem in self.titles)
        print()
        print(f'ID заметки: {self.__id}')
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки:\n {titles}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.status}')
        print(f'Дата создания: {date_format(self.created_date)}')
        print(f'Срок выполнения: {date_format(self.issue_date)}')
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

    def get_id(self):
        return self.__id
