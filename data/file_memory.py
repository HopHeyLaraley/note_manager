from data.temp_memory import notes
from note_class import Note
from datetime import datetime
import json

notes_file_path = 'data/notes.json'
statuses_file_path = 'data/statuses.json'

def load_notes():
    try:
        with open(notes_file_path, 'r', encoding='utf-8') as file:
            if file.read().strip() != '':
                file.seek(0)
                j_file = json.load(file)
                for elem in j_file:
                    created_date = datetime.strptime(elem['created'], '%Y-%m-%d %H:%M:%S.%f')
                    issue_date = datetime.strptime(elem['issue'], '%Y-%m-%d %H:%M:%S.%f')
                    data = {
                        'id': elem['id'],
                        'username': elem['username'],
                        'titles': elem['titles'],
                        'content': elem['content'],
                        'status': elem['status'],
                        'created': created_date,
                        'issue': issue_date
                    }
                    note = Note()
                    note.load(data)
    except FileNotFoundError:
        with open(notes_file_path, 'w') as file:
            file.write('')
            print('!!! Файл с заметками не был найден !!!')
            print('!!! Был создан новый файл с заметками !!!')

def save_notes():
    notes_list = []
    for i, note in notes.items():
        note_dict = note.to_dict()
        notes_list.append(note_dict)
    with open(notes_file_path, 'w', encoding='utf-8') as file:
        json.dump(notes_list, file, indent=4, ensure_ascii=False)

def load_statuses():
    try:
        with open(statuses_file_path, 'r', encoding='utf-8') as file:
            if file.read().strip() != '':
                file.seek(0)
                j_file = json.load(file)
                last_status_id = 1
                for status in j_file:
                    Note.statuses[last_status_id] = status
                    last_status_id += 1
    except FileNotFoundError:
        with open(statuses_file_path, 'w') as file:
            file.write('')
            print('!!! Файл со статусами не был найден !!!')
            print('!!! Был создан новый файл с заметками !!!')

def save_statuses():
    statuses = []
    for i in Note.statuses.keys():
        statuses.append(Note.statuses[i])
    with open(statuses_file_path, 'w', encoding='utf-8') as file:
        json.dump(statuses, file, indent=4, ensure_ascii=False)

def delete_from_dict(temp):
    for i in temp.keys():
        notes.pop(i)