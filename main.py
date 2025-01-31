from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import random
import os
from docx import Document
from datetime import datetime

# Ваш токен
TOKEN = '7847206496:AAGdiZkmjCgra_depXpOhK_K6sZgX0qVjoE'

# Состояния для бота
TEAM_NAMES, POSITIONS_COUNT, PROCESSING = range(3)

# Игроки по позициям
positions = {
    "Вратари": ['Акинфеев', 'Ноер', 'Куртуа', 'Навас', 'Де Хеа', 'Тер Штеген', 'Облак', 'Буффон'],
    "Защитники": ['Рамос', 'Марсело', 'Карвахаль', 'Рафаэл', 'Варан', 'Тьяго Силва', 'Компани', 'Дани Алвес',
                  'Алаба', 'Маркос Алонсо', 'Рохо', 'Пике', 'Жорди Альба', 'Пепе', 'Лам', 'Валенсия', 'Смоллинг',
                  'Маскерано', 'Давид Луиз', 'Марио Фернандес', 'Филиппе Луиз', 'Беллерин', 'Боатенг', 'Ругани',
                  'Годин', 'Умтити', 'Сандро'],
    "Полузащитники": ['Иньеста', 'Модрич', 'Кросс', 'Конте', 'Вильям', 'Бускетс', 'Дембеле', 'Эриксен', 'Сон', 'Алли',
                      'Озил', 'Головин', 'Погба', 'Черышев', 'Ди Мария', 'Оскар', 'Алькантара', 'Де Брюйне', 'Ракитич',
                      'Иско', 'Марко Ройс', 'Хамес', 'Сильва', 'Фабрегас', 'Матюиди', 'Касорла', 'Гуардадо', 'Сане',
                      'Стерлинг'],
    "Нападающие": ['Азар', 'Неймар', 'Роналду', 'Дибала', 'Мбаппе', 'Кавани', 'Месси', 'Коутиньо', 'Дзюба', 'Дембеле',
                   'Суарес', 'Агуэро', 'Левандовский', 'Кейн', 'Гризман', 'Лукаку', 'Салах', 'Фирмино', 'Промес',
                   'Коста', 'Бэйл', 'Мане', 'Санчес', 'Икарди', 'Аубемейанг', 'Ляказетт', 'Джеко']
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Введи название первой команды:")
    return TEAM_NAMES


async def team_names(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "team_1" not in context.user_data:
        context.user_data["team_1"] = update.message.text.strip()
        await update.message.reply_text("Теперь введи название второй команды:")
        return TEAM_NAMES

    context.user_data["team_2"] = update.message.text.strip()
    context.user_data["positions_count"] = {}
    context.user_data["current_position"] = list(positions.keys())[0]
    await update.message.reply_text(f"Сколько {context.user_data['current_position'].lower()} в каждой команде?")
    return POSITIONS_COUNT


async def positions_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    position = context.user_data["current_position"]
    try:
        count = int(update.message.text)
        max_count = len(positions[position]) // 2
        if 0 <= count <= max_count:
            context.user_data["positions_count"][position] = count
            keys = list(positions.keys())
            current_index = keys.index(position)
            if current_index + 1 < len(keys):
                context.user_data["current_position"] = keys[current_index + 1]
                await update.message.reply_text(
                    f"Сколько {context.user_data['current_position'].lower()} в каждой команде?")
                return POSITIONS_COUNT

            return await process_teams(update, context)
        else:
            await update.message.reply_text(f"Ошибка: нельзя выбрать больше {max_count} игроков на позицию {position}!")
    except ValueError:
        await update.message.reply_text("Введите целое число!")
    return POSITIONS_COUNT


async def process_teams(update: Update, context: ContextTypes.DEFAULT_TYPE):
    team_1, team_2 = {}, {}
    for position, players in positions.items():
        random.shuffle(players)
        count = context.user_data["positions_count"][position]
        selected_players = players[:count * 2]
        team_1[position], team_2[position] = selected_players[::2], selected_players[1::2]

    doc = Document()
    doc.add_heading('Состав команд', 0)

    def add_players_table(doc, team_name, players):
        doc.add_heading(team_name, level=2)
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'
        for i in range(0, len(players), 2):
            row = table.add_row().cells
            row[0].text = players[i]
            if i + 1 < len(players):
                row[1].text = players[i + 1]

    for team_name, team in [(context.user_data["team_1"], team_1), (context.user_data["team_2"], team_2)]:
        doc.add_heading(team_name, level=1)
        for position, players in team.items():
            add_players_table(doc, position, players)
        doc.add_page_break()

    file_path = f"teams_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx"
    doc.save(file_path)

    with open(file_path, "rb") as file:
        await update.message.reply_document(document=InputFile(file), filename=file_path)
    os.remove(file_path)
    return ConversationHandler.END


app = ApplicationBuilder().token(TOKEN).build()
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        TEAM_NAMES: [MessageHandler(filters.TEXT & ~filters.COMMAND, team_names)],
        POSITIONS_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, positions_count)],
    },
    fallbacks=[]
)
app.add_handler(conv_handler)
app.run_polling()
