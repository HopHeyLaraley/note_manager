from data.temp_memory import notes

def to_int(value):
    try:
        return int(value)
    except ValueError:
        return -1

def notes_exist():
    if not notes:
        print('Пока еще нет заметок')
        return 0
    return 1

def find_id():
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