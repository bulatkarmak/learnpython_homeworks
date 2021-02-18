# Задание 1

def hello_user():
    user_status = ''
    while user_status != 'Хорошо':
        user_status = input('Как дела? ')

hello_user()

# Задание 2

questions_dict = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Пойдешь гулять?': 'Вряд ли — дел много',
    'Какие планы?': 'Закончить курс и устроиться бэкендером',
    'Ответ на главный вопрос жизни, вселенной и всего такого?': '42 :-)',
}

def ask_usr():
    user_answer = ''
    print('** из программы можно выйти, написав «Выход» после «Программа:» **')
    while user_answer != 'Выход':
        user_answer = input('Пользователь: ')
        if user_answer in questions_dict:
            print(f'Программа: {questions_dict[user_answer]}')

ask_usr()
