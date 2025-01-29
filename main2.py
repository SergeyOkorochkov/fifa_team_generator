import random
from docx import Document
from datetime import datetime

# Списки игроков по позициям
goalkeepers = ['Акинфеев', 'Ноер', 'Куртуа', 'Навас', 'Де Хеа', 'Тер Штеген', 'Облак', 'Буффон']
defenders = ['Рамос', 'Марсело', 'Карвахаль', 'Рафаэл', 'Варан', 'Тьяго Силва', 'Компани', 'Дани Алвес', 'Алаба',
             'Маркос Алонсо', 'Рохо', 'Пике', 'Жорди Альба', 'Пепе', 'Лам', 'Валенсия', 'Смоллинг', 'Маскерано',
             'Давид Луиз', 'Марио Фернандес', 'Филиппе Луиз', 'Беллерин', 'Боатенг', 'Ругани', 'Годин', 'Умтити',
             'Сандро']
midfielders = ['Иньеста', 'Модрич', 'Кросс', 'Конте', 'Вильям', 'Бускетс', 'Дембеле', 'Эриксен', 'Сон', 'Алли', 'Озил',
               'Головин', 'Погба', 'Черышев', 'Ди Мария', 'Оскар', 'Алькантара', 'Де Брюйне', 'Ракитич', 'Иско',
               'Марко Ройс', 'Хамес', 'Сильва', 'Фабрегас', 'Матюиди', 'Касорла', 'Гуардадо', 'Сане', 'Стерлинг']
forwards = ['Азар', 'Неймар', 'Роналду', 'Дибала', 'Мбаппе', 'Кавани', 'Месси', 'Коутиньо', 'Дзюба', 'Дембеле',
            'Суарес', 'Агуэро', 'Левандовский', 'Кейн', 'Гризман', 'Лукаку', 'Салах', 'Фирмино', 'Промес', 'Коста',
            'Бэйл', 'Мане', 'Санчес', 'Икарди', 'Аубемейанг', 'Ляказетт', 'Джеко']

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

# Создаем документ Word
doc = Document()
doc.add_heading('Состав команд', 0)

# Команда Карачева
doc.add_heading('Команда Карачева', level=1)


# Функция для добавления таблицы игроков в два столбца
def add_players_table(doc, team_name, players):
    doc.add_heading(team_name, level=2)
    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'

    for i in range(0, len(players), 2):
        row = table.add_row().cells
        row[0].text = players[i]
        if i + 1 < len(players):
            row[1].text = players[i + 1]


# Добавляем составы команды Карачева в таблицы
add_players_table(doc, 'Вратари', team_karachev_goalkeepers)
add_players_table(doc, 'Защитники', team_karachev_defenders)
add_players_table(doc, 'Полузащитники', team_karachev_midfielders)
add_players_table(doc, 'Нападающие', team_karachev_forwards)

# Добавляем разрыв страницы перед командой Окорочкова
doc.add_page_break()

# Команда Окорочкова
doc.add_heading('Команда Окорочкова', level=1)

# Добавляем составы команды Окорочкова в таблицы
add_players_table(doc, 'Вратари', team_okorochkov_goalkeepers)
add_players_table(doc, 'Защитники', team_okorochkov_defenders)
add_players_table(doc, 'Полузащитники', team_okorochkov_midfielders)
add_players_table(doc, 'Нападающие', team_okorochkov_forwards)

# Генерируем уникальное имя файла с датой
date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"Составы_команд_{date_str}.docx"

# Сохраняем документ
try:
    doc.save(file_name)
    print(f"Состав команд сохранен в файл {file_name}")
except Exception as e:
    print(f"Ошибка при сохранении файла: {e}")
