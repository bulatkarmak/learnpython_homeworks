# Задание 1

def hello_user():
    user_status = ''
    while user_status != 'Хорошо':
        try:
            user_status = input('Как дела? ')
        except KeyboardInterrupt:
            print('\nПока!')
            break

hello_user()

# Задание 2

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print('Приведение типов не сработало')

discounted(100, 50, 'абвгд')
discounted(100, 50, 100)
