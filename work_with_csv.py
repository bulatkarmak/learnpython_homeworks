import csv

# Создайте список словарей
my_list = [
    {'name': 'Маша', 'age': '25', 'job': 'Scientist'},
    {'name': 'Вася', 'age': '8', 'job': 'Software Developer'},
    {'name': 'Эдуард', 'age': '48', 'job': 'Big Boss'},
]

# Запишите содержимое списка словарей в файл в формате csv
with open('my_list.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in my_list:
        writer.writerow(user)