class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

class TitlePage(Page):
    def output(self):
        title = super().output()
        return title.upper()

title = TitlePage(0, 'Python Practice Book')
print(title.output())

class Length(float):
    def to_cm(self):
        return super().__str__() + 'cm'

pencil_length = Length(16)
print(pencil_length.to_cm())