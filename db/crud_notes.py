import sqlite3
from .db_conf import db_path, table_name
import json

'''
данные заметок хранятся используются в коде в формате:
{
    *id: {
        'username': 'Имя',
        'titles': '["тег1", "тег2", ...]',
        'content': 'Текст заметки',
        'status': 'Статус',
        'created_date': '*дата_создания',
        'issue_date': '*дедлайн'
    }
}
*id - ID заметки в БД
*дата_создания, *дедлайн - Даты в формате дд-мм-гггг

В БД дата храниться в виде гггг-мм-дд
'''


# на вход приходят данные в виде строк (список - в виде json в кавычках)
def from_db_to_dict(fields, rows):
    note_dict = {}  # словарь для хранения значения полей под ключем - id
    for row in rows:
        note_fields = {}  # словарь для значений полей
        for i in range(1, len(fields)):
            note_fields[fields[i]] = row[i]  # пропускаем 0, т.к. там id
        note_dict[row[0]] = note_fields  # в row[0] хранится id, в него записываем поля
        note_dict[row[0]]['titles'] = json.loads(note_dict[row[0]]['titles'])  # список раскрываем из кавычек
    return note_dict


def insert_note(note):
    data = (
        note.username,
        json.dumps(note.titles),  # для хранения списка в БД, окружаем список кавычками
        note.content,
        note.status,
        note.created_date,
        note.issue_date
    )
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = f'''
    insert into {table_name}
    (username, titles, content, status, created_date, issue_date)
    values (?, ?, ?, ?, ?, ?);
    '''
    cur.execute(sql, data)
    conn.commit()
    conn.close()


def select_note(id=None):  # может выводить все заметки или одну - по id
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if id is not None:
        sql = f'select * from {table_name} where id={id};'
    else:
        sql = f'select * from {table_name};'

    cur.execute(sql)
    field_names = []
    for i in cur.description:
        field_names.append(i[0])
    rows = cur.fetchall()
    conn.close()

    return from_db_to_dict(field_names, rows)  # нормализация данных из БД


def update_note(id, field_name, value):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = f'update {table_name} set {field_name}=? where id=?'
    cur.execute(sql, (value, id))
    conn.commit()
    conn.close()


def delete_note(id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = f'delete from {table_name} where id=?'
    cur.execute(sql, id)
    conn.commit()
    conn.close()
