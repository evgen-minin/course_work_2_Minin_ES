# импортируем метод Path из библиотеки pathlib
from pathlib import Path
# импортируем класс Player
from game_words.main.players import Player
# импортируем функции из файла utils
from game_words.main.utils import load_random_word, reader_json

# создаём переменную и указываем путь к файлу json
WORDS = Path("../files/words.json")


# создаём основную функцию
def main():
    user_name = input("Введите ваше имя\n").capitalize()
    player = Player(user_name)
    print(f"Привет, {player.user_name}!")
    question = load_random_word(reader_json(WORDS))
    print(f"Составьте {question.quantity_subwords()} слов из слова {question.original_word.upper()}")
    print("Слова должны быть не короче 3 букв")
    print("Что бы закончить игру, угадайте все слова или напишите 'стоп'")
    print("Поехали, ваше первое слово?")
    # запускаем цикл пока пользователь не введёт стоп слово или не закончатся слова.
    while player.quantity_user_words_used() < question.quantity_subwords():
        user_answer = input().lower()
        if "стоп" in user_answer.lower() or "stop" in user_answer.lower():
            break
        elif len(user_answer) < 3:
            print("слишком короткое слово")
        elif player.checking_use_word(user_answer):
            print("уже использовано")
            continue
        elif user_answer in question.valid_subwords:
            print("верно")
            player.adding_a_word(user_answer)
        elif not question.word_check(user_answer):
            print("неверно")
            continue
    print(f"Игра завершена, вы угадали {player.quantity_user_words_used()} слово!")


# запускаем основную функцию
if __name__ == '__main__':
    main()
