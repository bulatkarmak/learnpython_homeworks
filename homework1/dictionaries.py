# Создайте словарь: {'city': 'Москва', 'temperature': '20'}
weather = {
    'city': 'Москва',
    'temperature': '20',
}

print(weather['city']) # Выведите на экран значение ключа city

# Уменьшите значение 'temperature' на 5:
weather['temperature'] = str(int(weather['temperature']) - 5) 

print(weather) # Выведите на экран весь словарь

print(weather.get('country')) # Проверьте, есть ли в словаре ключ 'country'

# Выведите значение по-умолчанию "Россия" для ключа country:
print(weather.get('country', 'Россия'))

# Добавьте в словарь элемент date со значением "27.05.2019":
weather['date'] = '27.05.2019'

print(len(weather)) # Выведите на экран длину словаря