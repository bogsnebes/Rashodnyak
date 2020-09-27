import rash

rash.read_txt()
delete = ["Удалить", "удалить", "УДАЛИТЬ"]
add = ["Добавить", "ДОБАВИТЬ", "добавить"]
cost_rash = ["расход", 'РАСХОД', "Расход"]
cost_dohod = ['Доход', "ДОХОД", "доход"]
List = ["Список", "СПИСОК", "список"]
summa = ['СУММА', "СУМА", "сума", "Сума", "сумма", "Сумма"]

while True:
    rash.write_txt()
    print('Что вы желаете сделать ?')
    print('Введите \"Удалить\", \"Добавить\", \"Список\": ')
    view = input()
    if view in delete:
        print('Для удаление всех данных введите "Данные", для категории "Категорию":', end=' ')
        delete_data = ['Данные', "данные", "ДАННЫЕ"]
        delete_kat = ["категорию", "КАТЕГОРИЮ", "Категорию"]
        view_delete = input()
        if view_delete in delete_data:
            rash.delete_txt()
            continue
        elif view_delete in delete_kat:
            print('Вы желаете удалить категорию дохода или расхода ?\n Введите:', end=" ")
            k = input()
            if k in cost_rash:
                print('Введите название категории:', end=" ")
                rash.delete(input(), True)
                continue
            elif k in cost_dohod:
                print('Введите название категории:', end=" ")
                rash.delete(input(), False)
                continue
            else:
                print('Вы ввели неправильное число !')
                continue
    if view in add:
        print('Вы желаете добавить категорию дохода или расхода ?\n Введите:', end=" ")
        k = input()
        print('Добавить новую категорию или прибавить сумму ? Введите "Сумма" или "Добавить":', end=" ")
        m = input()
        if m in summa:
            if k in cost_dohod:
                print('Введите название категории:', end=" ")
                name = input()
                print('Введите количество рублей:', end=" ")
                rash.cost(name, input(), True)
                continue
            elif k in cost_rash:
                print('Введите название категории:', end=" ")
                name = input()
                print('Введите количество рублей:', end=" ")
                rash.cost(name, input(), False)
                continue
        elif m in add:
            if k in cost_dohod:
                print('Введите название категории:', end=" ")
                rash.add(input(), 0, True)
                continue
            elif k in cost_rash:
                print('Введите название категории:', end=" ")
                rash.add(input(), 0, False)
                continue
    if view in List:
        rash.ls()
        continue