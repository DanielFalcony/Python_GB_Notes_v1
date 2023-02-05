import json


def save_file(data):
    '''
    Записывает данные формата json в json файл.
    :param data: Данные типа dict
    :return: записывает в формат *.json значения (в одну строрку)
    '''
    try:
        temporary_data = json.load(open('notes.json', encoding='utf-8'))
    except:
        temporary_data = []

    temporary_data.append(data)

    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(temporary_data, file, indent=2, ensure_ascii=False)


def load_file(open_file='notes.json'):
    '''
    Читает данные формата json
    :param data: Данные типа dict
    :return: записывает в формат *.json значения (в одну строрку)
    '''
    with open(f'{open_file}', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            print(i)
