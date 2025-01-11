import menu_actions
from menu_actions import *

# словарь с текстом для меню
action_names = {
    1: "Добавить заметку",
    2: "Показать все заметки",
    3: "Показать заметку по ID",
    4: "Изменить статус заметки по ID",
    5: "Удалить заметку",
    6: "Проверить дедлайны",
    7: "Изменить заметку по ID",
    0: "Выйти"
}


# функция с меню для удобного управления пользователя
# задание multiple_notes
def main_menu():
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
        print('\n' + '-' * 10)
        print('Выберите действие: ')
        for i, action_name in action_names.items():
            print(f'{i}: {action_name}')
        action = input()
        try:
            action = int(action)
        except ValueError:
            print("Выберите действие из предложенных\n")
            continue
        if action in menu_actions.actions:
            actions[action]()
        elif action == 0:
            return


main_menu()
