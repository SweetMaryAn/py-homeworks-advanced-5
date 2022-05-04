import datetime

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

def logger(catalog):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(f'{catalog}logs.txt', 'a', encoding='utf8') as document:
                document.write(
                    f'Дата и время запуска: {datetime.datetime.today()},'
                    f' имя функции: {old_function.__name__},'
                    f' аргументы: {args},'
                    f' результат выполнения: {result}\n'
                )
            return result
        return new_function
    return _logger

@logger('directoire_1/directoire_2/')
def lists(document):
    for doc in document:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')

lists(documents)