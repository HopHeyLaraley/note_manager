class Note:
    def __init__(self):
        self.titles = []
        self.username = input('Введите имя: ')
        i = 0
        while True:
            elem = input(f'Введите заголовок заметки {i + 1} или пустую строку для пропуска: ')
            if elem == '':
                break
            else:
                self.titles.append(elem)
                i += 1
        self.content = input('Введите содержимое заметки: ')
        self.status = input('Введите статус заметки: ')
        self.created_date = self.__correct_date('created')
        self.issue_date = self.__correct_date('issue')

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
        print(f'Имя пользователя: {self.username}')
        print(f'Заголовок заметки: {self.titles}')
        print(f'Содержимое заметки: {self.content}')
        print(f'Статус: {self.status}')
        if self.created_date['year'] != self.issue_date['year']:
            print(f'Дата создания: {self.created_date['day']}-{self.created_date['month']}-{self.created_date['year']}')
            print(f'Срок выполнения: {self.issue_date['day']}-{self.issue_date['month']}-{self.issue_date['year']}')
        else:
            print(f'Дата создания: {self.created_date['day']}-{self.created_date['month']}')
            print(f'Срок выполнения: {self.issue_date['day']}-{self.issue_date['month']}')


note = Note()
note.show_note()