class BasicWord:
    def __init__(self, original_word, valid_subwords):
        # исходное слово
        self.original_word = original_word
        # набор допустимых подслов
        self.valid_subwords = valid_subwords

    # проверка введенного слова в списке допустимых слов.
    def word_check(self, user_answer) -> bool:
        return user_answer in self.valid_subwords

    # подсчёт количества подслов.
    def quantity_subwords(self) -> int:
        return len(self.valid_subwords)

    def __repr__(self) -> str:
        return f"BasicWord({self.original_word}, {self.valid_subwords})"
