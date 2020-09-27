""" При работе с категориями переменная k = True, если доход, false, если расход.
    При работе с категориями переменная u = True, если юзер записывает данные, false, если это делает программа.
"""
from ast import literal_eval as le

kategory_dohod = {}
kategory_rashod = {}

def add(x = '', y = 0, k = True, u = True):
    'Создание категории'
    if x == '' or x == ' ' and u:
        print('Вы не ввели данные!')
        return None
    if k:
        kategory_dohod[x] = y
        print('Добавлена категория {}'.format(x))
    else:
        kategory_rashod[x] = y
        print('Добавлена категория {}'.format(x))
def delete(x, k):
    'Удаление категории'
    if k:
        kategory_dohod.pop(x)
        print('Удалена категория {}'.format(x))
    else:
        kategory_rashod.pop(x)
        print('Удалена категория {}'.format(x))
def cost(x, y, k):
    'Прибавление расхода/дохода к категории'
    if y.isdigit():
        Cost = int(y)
    else:
        print('Введите число !')
        return None
    if k:
        kategory_dohod[x] += Cost
        print('В категорию {} добавлено {} рублей'.format(x, y))
    else:
        kategory_rashod[x] += Cost
        print('В категорию {} добавлено {} рублей'.format(x, y))
def read_txt():
    'Чтение файла и подгрузка данных по состоянию и наличию категорий.'
    try:
        txt = open('text.txt', 'r')
        global kategory_rashod, kategory_dohod
        kategory_dohod_sinh, kategory_rashod_sinh = (txt.read()).split('#&*#')
        print('Read_txt(): ' + kategory_dohod_sinh, kategory_rashod_sinh)
        txt.close()
    except:
        return None
    kategory_dohod = le(kategory_dohod_sinh)
    kategory_rashod = le(kategory_rashod_sinh)
def write_txt():
    'Обновления файла текущими категориями и их состояниями.'
    txt = open('text.txt', 'w')
    txt.write(str(kategory_dohod) + '#&*#' + str(kategory_rashod))
    print('Данные сохранены')
    txt.close()
def add_user():
    'Добавление пользователя. НЕ РАБОТАЕТ'
    pass
def delete_txt():
    'Очищает все категории'
    print('Вы точно уверены, что готовы удалить все данные о категориях ?\n' +
          'Для подтверждения введите \"Да\", \"Согласен\", \"Согласна\", \"Yes\", '
          '\"Yes, i do\", \"Yeah\": ', end=' ')
    proverka = input()
    Words_agree = ['Да', 'да', 'Yes', 'yes', 'Yes, i do', 'yes, i do', 'ДА', 'YES', 'YES, I DO',
         'YES I DO', 'yes i do', 'Yes i do', 'Yeah', 'YEAH', 'yeah', 'Согласен',
         'согласен', 'СОГЛАСЕН', 'Согласна', 'согласна', 'СОГЛАСНА']
    if proverka in Words_agree:
        global kategory_rashod, kategory_dohod
        txt = open('text.txt', 'w')
        txt.write('')
        kategory_rashod = {}
        kategory_dohod = {}
        print('Удаление завершено')
        txt.close()
    else:
        print('Удаление отменено')
def qr_code():
    'Считывание QR-code с чеков. НЕ РАБОТАЕТ'
    pass
def ls():
    'Список всех категорий доходов и расходов'
    view_dohod = str(kategory_dohod)
    view_rashod = str(kategory_rashod)
    print('Категории доходов: {}\nКатегории расходов: {}'.format(view_dohod, view_rashod))
