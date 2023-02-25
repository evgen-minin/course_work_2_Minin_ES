# импортируем библиотеку json
import json
# импортируем метод shuffle из библиотеки random
from random import shuffle
# импортируем класс BasicWord
from basic_word import BasicWord
from game_words.main.basic_word import BasicWord


def reader_json(filename) -> list:
    """Функция считывает данные из json файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        list_word = json.load(file)
    return list_word


def load_random_word(list_words) -> BasicWord:
    """Функция получает список слов, выбирает случайное, создаёт и возвращает экземпляр класса BasicWord"""

    shuffle(list_words)
    for word in list_words:
        words = BasicWord(
            original_word=word["word"],
            valid_subwords=word["subwords"]
        )
        return words
