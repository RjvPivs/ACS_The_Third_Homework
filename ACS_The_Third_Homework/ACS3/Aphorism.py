from Wisdom import Wisdom


class Aphorism(Wisdom):
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def returnTheContent(self):
        return self.content

    def returnTheOwnField(self):
        return self.author
