from uuid import uuid4
from datetime import datetime
from db import select_note


def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        print("Введите корректную дату")
        return 0


def date_format(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    if date.year != datetime.today().year and date.year % 100 == 0:
        return date.strftime('%d-%m-%Y')
    elif date.year != datetime.today().year and date.year % 100 != 0:
        return date.strftime('%d-%m-%y')
    return date.strftime('%d-%m')


def unique_id():
    return int(uuid4())


def to_int(value):
    try:
        return int(value)
    except ValueError:
        return -1


def find_id():
    notes = select_note()
    if not notes:
        print('Пока еще нет заметок')
        return
    while True:
        usr_input = input("Введите ID (или 'X' для возврата): ")
        if usr_input.lower() in ('x', 'х'):
            return None
        try:
            note_id = int(usr_input)
            if note_id in [i for i in notes.keys()]:
                return note_id
            else:
                print("ID не существует\n")
        except ValueError:
            print("ID должно быть числом\n")
            continue
