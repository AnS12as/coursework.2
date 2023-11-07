class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def is_valid_subword(self, subword):
        return subword in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return self.word
