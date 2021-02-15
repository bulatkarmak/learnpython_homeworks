# Задание 1

numbers_list = [3, 5, 7, 9, 10.5] # Создайте список из чисел 3, 5, 7, 9 и 10.5
print(numbers_list) # Выведите содержимое списка на экран
numbers_list.append('Python') # Добавьте в конец списка строку 'Python'
print(len(numbers_list)) # Выведите длину списка на экран


# Задание 2

print(numbers_list[0]) # Выведите на экран начальный элемент списка
print(numbers_list[-1]) # Выведите на экран последний элемент списка

# Напечатайте элементы списка со второго по четвёртый включительно:
print(numbers_list[1:4])

numbers_list.remove('Python') # Удалите из списка строку 'Python'
print(numbers_list)