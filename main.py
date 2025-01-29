import random
from docx import Document

# Списки игроков по позициям
goalkeepers = ['Акинфеев', 'Ноер', 'Куртуа', 'Навас', 'Де Хеа', 'Тер Штеген', 'Облак', 'Буффон']
defenders = ['Рамос', 'Марсело', 'Карвахаль', 'Рафаэл', 'Варан', 'Тьяго Силва', 'Компани',
             'Дани Алвес', 'Алаба', 'Маркос Алонсо', 'Рохо', 'Пике', 'Жорди Альба',
             'Пепе', 'Лам', 'Валенсия', 'Смоллинг', 'Маскерано', 'Давид Луиз',
             'Марио Фернандес', 'Филиппе Луиз', 'Беллерин', 'Боатенг',
             'Ругани', 'Годин', 'Умтити', 'Сандро']
midfielders = ['Иньеста', 'Модрич', 'Кросс', 'Конте', 'Вильям', 'Бускетс', 'Дембеле',
               'Эриксен', 'Сон', 'Алли', 'Озил', 'Головин', 'Погба', 'Черышев', 'Ди Мария',
               'Оскар', 'Алькантара', 'Де Брюйне', 'Ракитич', 'Иско', 'Марко Ройс', 'Хамес',
               'Сильва', 'Фабрегас', 'Матюиди', 'Касорла', 'Гуардадо', 'Сане', 'Стерлинг']
forwards = ['Азар', 'Неймар', 'Роналду', 'Дибала', 'Мбаппе', 'Кавани', 'Месси', 'Коутиньо',
            'Дзюба', 'Дембеле', 'Суарес', 'Агуэро', 'Левандовский', 'Кейн', 'Гризман',
            'Лукаку', 'Салах', 'Фирмино', 'Промес', 'Коста', 'Бэйл', 'Мане', 'Санчес',
            'Икарди', 'Аубемейанг', 'Ляказетт', 'Джеко']

# Смешиваем игроков
random.shuffle(goalkeepers)
random.shuffle(defenders)
random.shuffle(midfielders)
random.shuffle(forwards)

# Инициализация команд
team_karachev = []
team_okorochkov = []

# Функция для деления игроков на команды
def divide_players(players):
    team_1 = []
    team_2 = []
    for i, player in enumerate(players):
        if i % 2 == 0:
            team_1.append(player)
        else:
            team_2.append(player)
    return team_1, team_2

# Разделение игроков на команды
team_karachev_goalkeepers, team_okorochkov_goalkeepers = divide_players(goalkeepers)
team_karachev_defenders, team_okorochkov_defenders = divide_players(defenders)
team_karachev_midfielders, team_okorochkov_midfielders = divide_players(midfielders)
team_karachev_forwards, team_okorochkov_forwards = divide_players(forwards)

# Выводим составы команд
print("Команда Карачева:")
print("Вратари:", team_karachev_goalkeepers)
print("Защитники:", team_karachev_defenders)
print("Полузащитники:", team_karachev_midfielders)
print("Нападающие:", team_karachev_forwards)

print("\nКоманда Окорочкова:")
print("Вратари:", team_okorochkov_goalkeepers)
print("Защитники:", team_okorochkov_defenders)
print("Полузащитники:", team_okorochkov_midfielders)
print("Нападающие:", team_okorochkov_forwards)

# Создаем документ Word
doc = Document()
doc.add_heading('Состав команд', 0)

# Команда Карачева
doc.add_heading('Команда Карачева', level=1)

# Вратари
doc.add_heading('Вратари', level=2)
for player in team_karachev_goalkeepers:
    doc.add_paragraph(player)

# Защитники
doc.add_heading('Защитники', level=2)
for player in team_karachev_defenders:
    doc.add_paragraph(player)

# Полузащитники
doc.add_heading('Полузащитники', level=2)
for player in team_karachev_midfielders:
    doc.add_paragraph(player)

# Нападающие
doc.add_heading('Нападающие', level=2)
for player in team_karachev_forwards:
    doc.add_paragraph(player)

# Команда Окорочкова
doc.add_heading('Команда Окорочкова', level=1)

# Вратари
doc.add_heading('Вратари', level=2)
for player in team_okorochkov_goalkeepers:
    doc.add_paragraph(player)

# Защитники
doc.add_heading('Защитники', level=2)
for player in team_okorochkov_defenders:
    doc.add_paragraph(player)

# Полузащитники
doc.add_heading('Полузащитники', level=2)
for player in team_okorochkov_midfielders:
    doc.add_paragraph(player)

# Нападающие
doc.add_heading('Нападающие', level=2)
for player in team_okorochkov_forwards:
    doc.add_paragraph(player)

# Сохраняем документ
try:
    doc.save("Составы команд.docx")
    print("Состав команд сохранен в файл Составы команд.docx")
except Exception as e:
    print(f"Ошибка при сохранении файла: {e}")
