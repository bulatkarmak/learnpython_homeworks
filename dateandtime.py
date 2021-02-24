import locale
from datetime import datetime, timedelta

locale.setlocale(locale.LC_TIME, "ru_RU")

# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад

today = datetime.now()
today_formatted = today.strftime('%d %B %Y')

yesterday = today - timedelta(days=1)
yesterday_formatted = yesterday.strftime('%d %B %Y')

thirty_days = today - timedelta(days=30)
thirty_days_fomatted = thirty_days.strftime('%d %B %Y')

print(f'Вчера было {yesterday_formatted} года.\n'
        f'Сегодня {today_formatted} года.\n'
        f'30 дней назад было {thirty_days_fomatted} года.')

# Превратите строку "01/01/25 12:10:03.234567" в объект datetime

date_string = '01/01/25 12:10:03.234567'
date_string = date_string.replace('25', '2025')

dt_date = datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S.%f')