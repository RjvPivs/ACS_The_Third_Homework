from Wisdom import Wisdom


class Proverb(Wisdom):
    def __init__(self, content, originCountry):
        self.content = content
        self.originCountry = originCountry

    def returnTheContent(self):
        return self.content

    def returnTheOwnField(self):
        return self.originCountry
