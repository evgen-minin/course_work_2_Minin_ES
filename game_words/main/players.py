class Player:

    def __init__(self, user_name):
        # имя пользователя
        self.user_name = user_name
        # использованные слова пользователя
        self.user_words_used = []

    # получение количества использованных слов
    def quantity_user_words_used(self) -> int:
        return len(self.user_words_used)

    # добавление слова в использованные слова
    def adding_a_word(self, user_word):
        self.user_words_used.append(user_word)

    # проверка использования данного слова до этого
    def checking_use_word(self, user_word) -> bool:
        return user_word in self.user_words_used

    def __repr__(self) -> str:
        return f"Player({self.user_name})"
