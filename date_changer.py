def input_note():
    username = input('Введите имя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите содержимое заметки: ')
    status = input('Введите статус заметки: ')
    created_date = input('Введите дату создания (день-месяц-год): ')
    issue_date = input('Введите срок выполнения (день-месяц-год): ')

    return {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date,
    }

def output_note(note):
    print(f'Имя пользователя: {note['username']}')
    print(f'Заголовок заметки: {note['title']}')
    print(f'Содержание заметки: {note['content']}')
    print(f'Статус: {note['status']}')
    print(f'Дата создания: {note['created_date']}')
    print(f'Срок выполнения: {note['issue_date']}')

note = input_note()
output_note(note)