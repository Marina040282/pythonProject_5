# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return filtering(data)


# Чтение данных из строки
def _read(csv):
    return [line.split(';') for line in csv.split('\n')]


# Сортировка по возрасту по возрастанию
def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))


# Фильтрация
def _filter(data):
    return [person for person in data if int(person[1]) < 10]


if __name__ == '__main__':
    print(get_users_list())
