from data.temp_memory import notes
from note_class import Note
from datetime import datetime
import json

notes_file_path = 'data/notes.json'
statuses_file_path = 'data/statuses.json'

# Grade 1. Этап 4: Задание 2 - Загрузка заметок из файла
# разве что не выполняется критерий оценивания "2.Функция возвращает список словарей"
# но вместо этого создаются объеты, которые уже сохраняются в словарь
# состояния чтения файла (1 или 0) используются в файле interface/menu.py в __init__() для
# продолжения работы или прекращения, если ошибку не исправить
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
        return 1
    # Grade 1. Этап 4: Задание 3 -  Обработка ошибок при работе с файлами
    except FileNotFoundError:
        with open(notes_file_path, 'w') as file:
            file.write('')
            print(f'!!! Файл {notes_file_path} не был найден. Создан новый файл !!!')
        return 1
    except json.decoder.JSONDecodeError:
        print(f'Ошибка при чтении файла {notes_file_path}. Проверьте его содержимое')
        return 0
    except PermissionError:
        print("Ошибка: Недостаточно прав для доступа к файлу.")
        return 0

# Grade 1. Этап 4: Задание 1 - Сохранение заметок в файл
# Grade 1. Этап 4: Задание 4 сюда добавить не смог, так как добавление в JSON,
# может сломать данные, а как это решить, чтобы использовать режим работы 'a', я не понял
# но и этот код добавляет новые заметки в файл
# Grade 1. Этап 4: Задание 5 - все сразу сохраняется в JSON
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
        return 1
    except FileNotFoundError:
        with open(notes_file_path, 'w') as file:
            file.write('')
            print(f'!!! Файл {statuses_file_path} не был найден. Создан новый файл !!!')
            return 1
    except json.decoder.JSONDecodeError:
        print(f'Ошибка при чтении файла {statuses_file_path}. Проверьте его содержимое')
        return 0
    except PermissionError:
        print("Ошибка: Недостаточно прав для доступа к файлу.")
        return 0

def save_statuses():
    statuses = []
    for i in Note.statuses.keys():
        statuses.append(Note.statuses[i])
    with open(statuses_file_path, 'w', encoding='utf-8') as file:
        json.dump(statuses, file, indent=4, ensure_ascii=False)

def delete_from_dict(temp):
    for i in temp.keys():
        notes.pop(i)