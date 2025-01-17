import random
from docx import Document

# Список футболистов
Goalkeepers = ['Акинфеев', 'Малафеев', 'Карачев', 'Окорочков', 'Яшин',
               'Кан', 'Куртуа', 'Сафонов', 'Ноер', 'Кобель']

# Перемешиваем список игроков
random.shuffle(Goalkeepers)

# Инициализируем команды
Команда_Окорочкова = []
Команда_Карачева = []

# По очереди добавляем игроков в команды
for i, player in enumerate(Goalkeepers):
    if i % 2 == 0:
        Команда_Окорочкова.append(player)
    else:
        Команда_Карачева.append(player)

# Выводим состав команд
print("Команда 1:", Команда_Окорочкова)
print("Команда 2:", Команда_Карачева)

# Создаем документ Word
doc = Document()
doc.add_heading('Состав команд', 0)

# Добавляем команду 1
doc.add_heading('Команда 1', level=1)
for player in Команда_Окорочкова:
    doc.add_paragraph(player)

# Добавляем команду 2
doc.add_heading('Команда 2', level=1)
for player in Команда_Карачева:
    doc.add_paragraph(player)

# Сохраняем документ
doc.save("Составы команд.docx")

print("Состав команд сохранен в файл teams.docx")
