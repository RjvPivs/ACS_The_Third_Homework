from Wisdom import Wisdom


class Riddle(Wisdom):
    def __init__(self, content, answer):
        self.content = content
        self.answer = answer

    def returnTheContent(self):
        return self.content

    def returnTheOwnField(self):
        return self.answer
