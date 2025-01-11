import datetime

class Note:
    id = 0
    def __init__(self):
        self.__id = Note.id
        self.username = input('Введите имя: ')
        i = 0
        titles = []
        while True:
            elem = input(f'Введите заголовок заметки {i + 1} или пустую строку для пропуска: ')
            if elem == '':
                break
            else:
                titles.append(elem)
                i += 1
        self.titles = set(titles)
        self.content = input('Введите содержимое заметки: ')
        self.status = input('Введите статус заметки: ')
        self.created_date = self.__correct_date('created')
        self.issue_date = self.__correct_date('issue')
        Note.id += 1

    def __correct_date(self, date_of):
        if date_of == 'created':
            date_of = 'дату создания'
        elif date_of == 'issue':
            date_of = 'срок выполнения'
        while True:
            created_date = input(f'Введите {date_of} (день-месяц-год): ')
            try:
                created_date = [int(num) for num in created_date.split('-')]
                if len(created_date) != 3:
                    print("Введите корректную дату")
                    continue
                if created_date[0] > 31 or created_date[1] > 12:
                    print("Введите корректную дату")
                    continue
            except ValueError:
                print("Введите корректную дату")
                continue
            return {
                'day': created_date[0],
                'month': created_date[1],
                'year': created_date[2]
            }

    def show_note(self):
        print()
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовки заметки: ')
        print(f'{"\n".join("- " + elem for elem in self.titles)}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.status}')
        print(f'Дата создания: {self.created_date['day']}-{self.created_date['month']}{"-" + str(self.created_date['year']) if self.created_date['year'] != datetime.date.today().year else ""}')
        print(f'Срок выполнения: {self.issue_date['day']}-{self.issue_date['month']}{"-" + str(self.issue_date['year']) if self.issue_date['year'] != datetime.date.today().year else ""}')
        print()


note = Note()
note.show_note()