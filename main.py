def parsing_csv_file(filename) -> dict:
    """открываем файл и читаем построчно нужные нам столбцы"""
    d = {}
    with open(filename, encoding="utf8") as file:
        for line in file.readlines()[1:]:
            _, dept, group, _, _, salary = line.split(';')
            if dept not in d:
                d[dept] = {
                    'groups': set(),
                    'counter': 0,
                    'salaries': []
                }
            d[dept]['groups'].add(group)
            d[dept]['counter'] += 1
            d[dept]['salaries'].append(float(salary[:-1]))
    return d

def print_hierarchy(d: dict) -> None:
    """печатаем иерархию отделов"""
    for k, v in d.items():
        print(f'{k}:')
        for x in v['groups']:
            print("--", x)


def print_report(d: dict) -> None:
    """печатаем отчет"""
    for k, v in d.items():
        print(f'{k}:')
        print(f'-- Численность: {v["counter"]}')
        print(f'-- Мин. з/п: {min(v["salaries"])}')
        print(f'-- Макс. з/п: {max(v["salaries"])}')
        print(f'-- Средняя з/п: {round(sum(v["salaries"]) / v["counter"], 2)}')


def save_tpo_csv(d: dict) -> None:
    """делаем отчет и сохраняем его"""
    with open('Corp_Summary_res.csv', 'w', encoding="utf8") as file:
        file.write('Департамент;Численность;Минимальная з/п;Максимальная з/п;Средняя з/п\n')
        for k, v in d.items():
            file.write(
                f'{k};{v["counter"]};{min(v["salaries"])};{max(v["salaries"])};'
                f'{round(sum(v["salaries"]) / v["counter"], 2)}\n')


def menu() -> None:
    """открываем файл, делаем меню"""
    d = parsing_csv_file('Corp_Summary.csv')
    print(
        'Меню: \n'
        '1. Вывести в понятном виде иерархию команд \n'
        '2. Вывести сводный отчёт по департаментам \n'
        '3. Сохранить сводный отчёт \n'
    )
    options = {'1': 1, '2': 2, '3': 3}
    option = ''
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    if option in options:
        if options[option] == 1:
            print_hierarchy(d)
        elif options[option] == 2:
            print_report(d)
        elif options[option] == 3:
            save_tpo_csv(d)


if __name__ == '__main__':
    menu()
