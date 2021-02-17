# Цикл 1

list_ = [1, 11, 3, 13, 5, 15, 7, 17, 9, 19]
for num in list_:
    print(f'{num} -> {num + 1}')

# Цикл 2

input_string = input('\nВведите какое-нибудь слово: ')
for letter in input_string:
    print(letter)

# Оценки

list_with_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '6a', 'scores': [2, 3, 3, 4, 1]},
    {'school_class': '8a', 'scores': [3, 2, 2, 1, 4]},
    {'school_class': '10a', 'scores': [5, 1, 2, 3, 4]},
]

average_score_school = 0

for score in list_with_scores:
    average_score_school += sum(score['scores'])

print(f'Средний балл по школе: {average_score_school}.')

for score in list_with_scores:
    average_score_class = sum(score['scores'])
    class_name = score['school_class']
    print(f'В {class_name} средний балл: {average_score_class}.')
