from models import User

first_user = User.query.first()
print(f'''Имя Фамилия: {first_user.name}
Зарплата: {first_user.salary} долларов
Email: {first_user.email}
''')