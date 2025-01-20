from models import Note, notes
from datetime import datetime
import json

notes_file_path = 'data/notes.json'
statuses_file_path = 'data/statuses.json'


def load_notes(file_path = notes_file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
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
        return 1
    # Grade 1. Этап 4: Задание 3 -  Обработка ошибок при работе с файлами
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write('')
            print(f'!!! Файл {file_path} не был найден. Создан новый файл !!!')
        return 1
    except json.decoder.JSONDecodeError:
        print(f'Ошибка при чтении файла {file_path}. Проверьте его содержимое')
        return 0
    except PermissionError:
        print("Ошибка: Недостаточно прав для доступа к файлу.")
        return 0

def save_notes(file_path = notes_file_path):
    notes_list = []
    for i, note in notes.items():
        note_dict = note.to_dict()
        notes_list.append(note_dict)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notes_list, file, indent=4, ensure_ascii=False)
        return 1

def load_statuses(file_path = statuses_file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if file.read().strip() != '':
                file.seek(0)
                j_file = json.load(file)
                last_status_id = 1
                for status in j_file:
                    Note.statuses[last_status_id] = status
                    last_status_id += 1
        return 1
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write('')
            print(f'!!! Файл {file_path} не был найден. Создан новый файл !!!')
            return 1
    except json.decoder.JSONDecodeError:
        print(f'Ошибка при чтении файла {file_path}. Проверьте его содержимое')
        return 0
    except PermissionError:
        print("Ошибка: Недостаточно прав для доступа к файлу.")
        return 0

def save_statuses(file_path = statuses_file_path):
    statuses = []
    for i in Note.statuses.keys():
        statuses.append(Note.statuses[i])
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(statuses, file, indent=4, ensure_ascii=False)
        return 1

def delete_from_dict(temp):
    try:
        for i in temp.keys():
            notes.pop(i)
        return 1
    except KeyError:
        print('Попытка удалить несуществующие заметки')
        return 0

if __name__ == '__main__':
    delete_from_dict({1: Note()})