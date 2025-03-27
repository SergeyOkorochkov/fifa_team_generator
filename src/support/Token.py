import os

from dotenv import load_dotenv


class Token(object):
    __token = None

    def __init__(self):
        # Загружаем переменные окружения
        load_dotenv()
        # Получаем токен
        self.__token = os.getenv("TOKEN")
        # Проверяем, загружен ли токен, если нет выдаст ошибку специально
        if not self.__token:
            raise ValueError("Ошибка: Токен не найден! Проверь .env-файл.")
        else:
            print("Токен успешно загружен!")

    def get(self):
        return self.__token
