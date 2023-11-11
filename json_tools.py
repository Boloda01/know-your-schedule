"""
Copyright (c) 2023 qdiaps

Програмне забеспечення поширюється з ліцензією MIT.
Детальніше дивіться у файлі LICENSE.
"""

import json

from os.path import isfile, os

#Додавання
def serialization(to_json, path):
	with open(path, 'w') as file:
		json.dump(to_json, file, ensure_ascii=False, sort_keys=True, indent=2)

def deserialization(path):
	if isfile(path):
		with open(path) as file:
			return json.load(file)
	else:
		print(f'Такого файлу немає: {path}')

#Видалення
def serialization(to_json, path):
    with open(path, 'w') as file:
        json.dump(to_json, file, ensure_ascii=False, sort_keys=True, indent=2)

def deserialization(path):
    if isfile(path):
        with open(path) as file:
            return json.load(file)
    else:
        print(f'Такого файлу немає: {path}')
        return {}

def remove_data_and_serialize(path, keys_to_remove):
    data = deserialization(path)
    for key in keys_to_remove:
        data.pop(key, None)
    serialization(data, path)

def delete_file(path):
    if isfile(path):
        try:
            os.remove(path)
            print(f'Файл видален: {path}')
        except Exception as e:
            print(f'Не вдалося видалити файл: {e}')
    else:
        print(f'Файл не знайден: {path}')