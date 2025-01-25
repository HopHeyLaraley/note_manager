from interface.note_manager import CreateNote, ReadNote, SearchNote, UpdateNote, DeleteNote, NoteUtils
from utils import to_int


class Menu:
    # тексты пунктов меню
    action_names = {
        1: "Добавить заметку",
        2: "Показать заметки",
        3: "Изменить заметку",
        4: "Удалить заметку",
        5: "Найти заметку",
        6: "Проверить дедлайны",
        0: "Выйти"
    }

    menu_actions = {}

    def __init__(self):
        Menu.menu_actions = {
            1: CreateNote().main,  # метод создания заметки
            2: ReadNote().main,  # метод отображения заметок
            3: UpdateNote().main,  # метод обновления заметки
            4: DeleteNote().main,
            5: SearchNote().main,  # метод поиска заметок
            6: NoteUtils().check_deadlines,
        }
        self.main_menu()

    def main_menu_text(self):
        print('*' * 10)
        print('Выберите действие: ')
        for i, action_name in Menu.action_names.items():
            print(f'{i}.{action_name}')

    # меню действий
    def main_menu(self):
        print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
        while True:
            self.main_menu_text()
            action = to_int(input())
            if action == 0:
                return
            elif action in self.action_names.keys():
                Menu.menu_actions[action]()
            else:
                print("Выберите действие из предложенных\n")
                continue