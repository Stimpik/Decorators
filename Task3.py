import datetime
import types


def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            with open(path, 'a', encoding='utf-8') as file:
                value = old_function(*args, **kwargs)
                file.writelines(f'Время вызова функции: {time} \n')
                file.write(f'Название функции: {old_function.__name__} \n')
                file.write(f'Аргументы функции: {args}, {kwargs}\n')
                file.write(f'Результат функции: {value}\n')

            return value

        return new_function

    return _logger
@logger('Generator.txt')
def flat_generator(list_of_lists):
    for items in list_of_lists:
        for item in items:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
