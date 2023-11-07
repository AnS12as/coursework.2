class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def get_used_words_count(self):
        return len(self.used_words)

    def add_used_word(self, word):
        self.used_words.append(word)

    def has_used_word(self, word):
        return word in self.used_words

    def __repr__(self):
        return self.name
