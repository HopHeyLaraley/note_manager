# 1: "Добавить заметку",
# 2: "Показать все заметки",
# 3: "Показать заметку по ID",
# 4: "Изменить статус заметки по ID",
# 5: "Удалить заметку",
# 6: "Проверить дедлайны",
# 7: "Изменить заметку по ID",
# 0: "Выйти"

from note_class import Note, notes
import update_note


def notes_exist():
    if not notes:
        print('Пока еще нет заметок')
        return 0
    return 1


# №1 меню - функция добавления заметки
def add_note():
    note = Note()
    class_id = note.get_id()
    notes[class_id] = note
    print('Заметка добавлена')


# №2 меню - функция вывода всех заметкок
def show_all():
    if not notes_exist():
        return
    for note_id in notes.keys():
        notes.get(note_id).show_note()


# функция для ввода корректного ID
def get_id():
    if not notes_exist():
        return
    while True:
        usr_input = input("Введите ID (или 'X' для возврата): ")
        if usr_input.lower() in ('x', 'х'):
            return None
        try:
            note_id = int(usr_input)
            if note_id in notes.keys():
                return note_id
            else:
                print("ID не существует\n")
        except ValueError:
            print("ID должно быть числом\n")
            continue


# №3 меню - функция вывода заметки по ID
def show_id():
    note_id = get_id()
    if note_id is None:
        return
    notes.get(note_id).show_note()


# №4 меню - функция изменения статуса заметки по ID
def change_by_id():
    note_id = get_id()
    if note_id is None:
        return
    notes.get(note_id).change_status_menu()


# дальше идут 3 функции для удаления заметок по 3 критериям
# 1 - функция для удаления по id
# задание delete_note
def del_by_id():
    note_id = get_id()
    if note_id is None:
        return
    notes.pop(note_id)
    print('Заметка удалена!')


# 2 - функция для удаления по имени пользователя
# задание delete_note
def del_by_username():
    name = input('Введите имя пользователя: ')
    del_count = 0
    del_indexes = []
    for i, val in notes.items():
        if val.username == name:
            del_indexes.append(i)
            del_count += 1
    for i in del_indexes:
        notes.pop(i)
    if del_count < 1:
        print('У этого пользователя не было заметок')
    else:
        print(f'Удалено заметок: {del_count}')


# 3 - функция для удаления по заголовкам
# задание delete_note
def del_by_title():
    ttl = input('Введите заголовок: ')
    del_count = 0
    del_indexes = []
    for i, val in notes.items():
        if ttl.lower() in val.titles:
            del_indexes.append(i)
            del_count += 1
    for i in del_indexes:
        notes.pop(i)
    if del_count < 1:
        print('Нет заметок с таким заголовком')
    else:
        print(f'Удалено заметок: {del_count}')


# №5 меню - функция удаления заметки по ID
# задание delete_note
def delete_note():
    if not notes_exist():
        return
    while True:
        print('По какому критерию удалить заметки?:\n1.По ID\n2.По имени пользователя\n3.По заголовку\n0.Вернуться')
        choice = input()

        try:
            choice = int(choice)
        except ValueError:
            print('Выберите из предложенных вариантов')

        if choice == 0:
            return
        elif choice == 1:
            del_by_id()
        elif choice == 2:
            del_by_username()
        elif choice == 3:
            del_by_title()
        else:
            print('Выберите из предложенных вариантов')


# №6 меню - функция вывода дедлайна заметки по ID
def check_deadline():
    note_id = get_id()
    if note_id is None:
        return
    print(notes.get(note_id).check_deadline())


# словарь для связи пунктов меню с функциями
# задание multiple_notes (все функции)
actions = {
    1: add_note,
    2: show_all,
    3: show_id,
    4: change_by_id,
    5: delete_note,
    6: check_deadline,
    7: update_note
}
