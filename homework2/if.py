# Практика: Возраст

def choose_your_destiny(age):
    if age < 2:
        raise ValueError(f'Слишком молодой – вряд ли ты сам мог сесть за комп ¯\_(ツ)_/¯')
    if age < 7:
        return 'В этом возрасте тебе самое место в садике'
    if age < 18:
        return 'О, да ты у нас школьник?'
    if age < 23:
        return 'Студентота, значит?'
    if age < 65:
        return 'Добро пожаловать во взрослую жизнь, работяга'
    else:
        return 'Дед, тебя же съели О_о'

user_age = int(input('Хай! Введи свой возраст: '))
function_result = choose_your_destiny(user_age)
print(function_result)

# Практика: Сравнение строк

def string_operations(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
        else:
            return 'К такому жизнь меня не готовила'
    else:
        return 0

print(f'\n{string_operations(1, 2)}') # Тип обоих параметров не string
print(string_operations(1, '2')) # Тип одного параметра не string
print(string_operations('1', '2')) # Оба параметра string, но не сооответствуют условиям из задания
print(string_operations('1', '1')) # Одинаковые параметры
print(string_operations('11', '1')) # Первый параметр длиннее второго
print(string_operations('1', '22')) # Второй параметр длиннее первого
print(string_operations('2', '1')) # Разные параметры одинаковой длины
print(string_operations('1', 'learn')) # Второй параметр со значением 'learn'
