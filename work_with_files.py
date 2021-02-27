# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as rd:
    rd_text = ''
    words_count = 0
    for line in rd:
        rd_text += line
        rd_text = rd_text.replace('.', '!')
        temp_list = line.split()
        words_count += len(temp_list)
    print(f'Количество символов: {len(rd_text)}')
    print(f'Количество слов: {words_count}')
    with open('referat2.txt', 'w', encoding='utf-8') as wt:
        wt.write(rd_text)
