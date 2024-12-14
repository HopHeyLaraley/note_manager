def print_note(username, title, content, status, created_date, issue_date):
    print(f'Имя пользователя: {username}')
    print(f'Заголовок заметки: {title}')
    print(f'Содержание заметки: {content}')
    print(f'Статус: {status}')
    print(f'Дата создания: {created_date}')
    print(f'Срок выполнения: {issue_date}')

username = 'Сергеев Дмитрий'
title = 'Выполнить задание'
content = '\n1. Написать код\n2. Протестировать\n3. Загрузить на Гитхаб\n4. Отправить ссылку'
status = 'В работе'
created_date = '14-12-2024'
issue_date = '16-12-2024'

print_note(username, title, content, status, created_date, issue_date)