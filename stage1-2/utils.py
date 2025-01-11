# функция цикличного ввода заголовков
# задание add_titles_loop
def input_titles():
    i = 0
    titles = []
    while True:
        elem = input(f'Введите заголовок заметки {i + 1} или пустую строку для пропуска: ')
        if elem == '':
            break
        else:
            titles.append(elem)
            i += 1
    return set(titles)

def format_date(date):
    return date.strftime("%d-%m")


# вспомогательная функция для склонения слова "день" для N дней
# задание check_deadline
def days_in_rus(n):
    if 11 <= n % 100 <= 19:
        return 'дней'
    elif n % 10 == 1:
        return 'день'
    elif 2 <= n % 10 <= 4:
        return 'дня'
    else:
        return 'дней'